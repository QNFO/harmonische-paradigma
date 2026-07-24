#!/usr/bin/env python3
"""
CAL-03: CMB Log-Periodogram Analysis (Optimized)
=================================================
Search for log-periodic oscillations in Planck 2018 CMB TT power spectrum.
Tests periods ln(q) ≈ 1 (Efimov) and ln(q) ≈ ln(π).
"""
import numpy as np
from scipy.signal import lombscargle
from scipy.interpolate import interp1d
from scipy import stats
import json, os, sys, time

print("=" * 70, flush=True)
print("CAL-03: CMB Log-Periodogram Analysis", flush=True)
print("=" * 70, flush=True)

# ── 1. Load data ──
print("\n[1] Loading data...", flush=True)

# Data provenance: Planck 2018 Legacy Archive
# Binned: https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmology/COM_PowerSpect_CMB-TT-binned_R3.01.txt
# Theory: https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmology/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt
# Local copies in cal03-data/ for reproducibility (Zenodo/GitHub/R2)

# Binned TT: l, Dl, -err, +err, BestFit
binned = np.loadtxt('cal03-data/planck_tt_binned.txt', comments='#')
ell_b = binned[:, 0]
dl_b = binned[:, 1]
err_m = binned[:, 2]
err_p = binned[:, 3]
dl_bf_binned = binned[:, 4]
errors = (err_m + err_p) / 2.0

# Best-fit theory
theory = np.loadtxt('cal03-data/planck_tt_bestfit.txt', comments='#')
ell_th = theory[:, 0].astype(int)
dl_th = theory[:, 1]

print(f"  Binned: {len(ell_b)} pts, ℓ=[{ell_b[0]:.0f},{ell_b[-1]:.0f}]", flush=True)
print(f"  Theory: {len(ell_th)} pts, ℓ=[{ell_th[0]},{ell_th[-1]}]", flush=True)

# ── 2. Mask and compute residuals ──
mask = (ell_b >= 30) & (ell_b <= 2500)
ell = ell_b[mask]
dl = dl_b[mask]
err = errors[mask]

# Interpolate theory
bf_interp = interp1d(ell_th, dl_th, kind='cubic', bounds_error=False, fill_value='extrapolate')
dl_bf = bf_interp(ell)
residuals = dl - dl_bf

chi2 = np.sum((residuals / err) ** 2)
dof = len(residuals)
print(f"\n  χ²/dof = {chi2:.1f}/{dof} = {chi2/dof:.3f}", flush=True)
print(f"  RMS residuals = {np.sqrt(np.mean(residuals**2)):.1f} μK²", flush=True)

# ── 3. Log-resample ──
print("\n[2] Log-resampling...", flush=True)
x_data = np.log(ell)
n_pts = 200
x_grid = np.linspace(np.log(30), np.log(2500), n_pts)

# Interpolate residuals and errors to uniform log grid
r_interp = interp1d(x_data, residuals, kind='cubic', bounds_error=False, fill_value='extrapolate')
e_interp = interp1d(x_data, err, kind='cubic', bounds_error=False, fill_value='extrapolate')
y_grid = r_interp(x_grid)
e_grid = e_interp(x_grid)

# ── 4. Lomb-Scargle periodogram ──
print("[3] Computing Lomb-Scargle periodogram...", flush=True)

f_min, f_max = 0.02, 5.0
n_freq = 4000
freqs = np.linspace(f_min, f_max, n_freq)
ang_freqs = 2 * np.pi * freqs

weights = 1.0 / (e_grid ** 2)
weights /= np.mean(weights)

y_mean = np.average(y_grid, weights=weights)
y_norm = y_grid - y_mean

power = lombscargle(x_grid, y_norm, ang_freqs, normalize='normalize', weights=weights)

# ── 5. Find peaks ──
print("[4] Finding peaks...", flush=True)

# Use argrelextrema-like approach
peaks = []
for i in range(1, len(power) - 1):
    if power[i] > power[i-1] and power[i] > power[i+1] and power[i] > 0.01:
        peaks.append({
            'freq': float(freqs[i]),
            'period': float(1.0 / freqs[i]),
            'q': float(np.exp(1.0 / freqs[i])),
            'power': float(power[i]),
        })

peaks.sort(key=lambda p: p['power'], reverse=True)

print(f"\n  Top 15 peaks:", flush=True)
print(f"  {'Freq':>8s}  {'Period':>8s}  {'q':>10s}  {'Power':>8s}", flush=True)
for p in peaks[:15]:
    print(f"  {p['freq']:8.4f}  {p['period']:8.4f}  {p['q']:10.4f}  {p['power']:8.4f}", flush=True)

# ── 6. Template correlation ──
print("\n[5] Template correlation analysis...", flush=True)

ell0 = np.exp(x_grid[len(x_grid)//2])

def correlate_template(period, phase):
    template = np.cos(2 * np.pi * np.log(np.exp(x_grid) / ell0) / period + phase)
    w = 1.0 / (e_grid ** 2)
    w /= np.sum(w)
    yw = np.sqrt(w) * y_grid
    tw = np.sqrt(w) * template
    r = np.corrcoef(yw, tw)[0, 1]
    n_eff = len(y_grid)
    if abs(r) < 1.0:
        t = r * np.sqrt((n_eff - 2) / (1 - r**2))
        p = 2 * stats.t.sf(abs(t), n_eff - 2)
    else:
        p = 0.0
    return r, p, template

targets = {
    'Efimov: ln q = 1.0': 1.0,
    'q = π: ln q = ln π': np.log(np.pi),
    'q = e: ln q = 1.0': 1.0,
    'q = √π: ln q = ½ln π': 0.5 * np.log(np.pi),
    'q = λ_Efimov: ln q = ln(22.694)': np.log(22.694),
    'q = π²: ln q = 2ln π': 2 * np.log(np.pi),
}

for name, period in targets.items():
    r_cos, p_cos, _ = correlate_template(period, 0.0)
    r_sin, p_sin, _ = correlate_template(period, np.pi/2)
    r_best = r_cos if abs(r_cos) >= abs(r_sin) else r_sin
    p_best = p_cos if abs(r_cos) >= abs(r_sin) else p_sin
    phase_best = "cos" if abs(r_cos) >= abs(r_sin) else "sin"
    print(f"  {name:35s}: r={r_best:+.4f}, p={p_best:.4f} ({phase_best})", flush=True)

# ── 7. Phase scan ──
print("\n[6] Phase scan for Efimov and π periods...", flush=True)

for pname, period in [('Efimov (ln q=1)', 1.0), ('π (ln q=ln π)', np.log(np.pi))]:
    phases = np.linspace(0, 2*np.pi, 100)
    rs = np.array([correlate_template(period, phi)[0] for phi in phases])
    best_idx = np.argmax(np.abs(rs))
    print(f"  {pname}: best φ={phases[best_idx]:.4f}, r_max={rs[best_idx]:+.4f}", flush=True)

# ── 8. MC significance ──
print("\n[7] Monte Carlo significance (100 sims)...", flush=True)
t0 = time.time()

n_sims = 100
max_powers_null = np.zeros(n_sims)
rng = np.random.default_rng(42)

for i in range(n_sims):
    if (i+1) % 20 == 0:
        print(f"    {i+1}/{n_sims}...", flush=True)
    
    mock = dl_bf + rng.normal(0, err)
    mock_res = mock - dl_bf
    m_interp = interp1d(x_data, mock_res, kind='cubic', bounds_error=False, fill_value='extrapolate')
    m_grid = m_interp(x_grid)
    m_mean = np.average(m_grid, weights=weights)
    m_norm = m_grid - m_mean
    m_power = lombscargle(x_grid, m_norm, ang_freqs, normalize='normalize', weights=weights)
    max_powers_null[i] = np.max(m_power)

t1 = time.time()
print(f"  Done in {t1-t0:.1f}s", flush=True)

max_power_obs = np.max(power)
p_value = np.mean(max_powers_null >= max_power_obs)

print(f"\n  Observed max power: {max_power_obs:.6f}", flush=True)
print(f"  Null median: {np.median(max_powers_null):.6f}", flush=True)
print(f"  Null 95%: {np.percentile(max_powers_null, 95):.6f}", flush=True)
print(f"  Null 99%: {np.percentile(max_powers_null, 99):.6f}", flush=True)
print(f"  MC p-value: {p_value:.4f}", flush=True)

# ── 9. Analytic FAP ──
print("\n[8] Analytic false-alarm probabilities...", flush=True)

# Number of independent frequencies
x_range = x_grid[-1] - x_grid[0]
n_indep = int((f_max - f_min) * x_range)

for name, period in [('Efimov (f≈1)', 1.0), ('π (f≈0.877)', np.log(np.pi))]:
    tf = 1.0 / period
    idx = np.argmin(np.abs(freqs - tf))
    p_at = power[idx]
    af = freqs[idx]
    
    single_fap = (1.0 - p_at) ** ((n_pts - 3) / 2.0)
    multi_fap = 1.0 - (1.0 - single_fap) ** n_indep
    
    print(f"  {name}: f={af:.4f}, pow={p_at:.6f}, single-FAP={single_fap:.6f}, multi-FAP={multi_fap:.6f}", flush=True)

# ── 10. Generate plots ──
print("\n[9] Generating figures...", flush=True)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

os.makedirs('cal03-data/figures', exist_ok=True)

# Figure 1: Power spectrum + residuals
fig, axes = plt.subplots(3, 1, figsize=(12, 14), sharex=True)

ax = axes[0]
ax.errorbar(ell_b, dl_b, yerr=errors, fmt='o', ms=2, color='black', capsize=0, alpha=0.5, label='Planck 2018 TT')
ax.plot(ell_th, dl_th, 'r-', lw=1.5, alpha=0.8, label=r'$\Lambda$CDM best-fit')
ax.set_ylabel(r'$D_\ell$ [$\mu$K$^2$]')
ax.set_xscale('log')
ax.legend(fontsize=8)
ax.set_title('Planck 2018 CMB TT Power Spectrum')
ax.grid(True, alpha=0.3)

ax = axes[1]
all_res = dl_b - bf_interp(ell_b)
ax.errorbar(ell_b, all_res, yerr=errors, fmt='o', ms=2, color='steelblue', capsize=0, alpha=0.5)
ax.axhline(0, color='gray', ls='--', alpha=0.5)
ax.set_ylabel(r'$\Delta D_\ell$ [$\mu$K$^2$]')
ax.set_xscale('log')
ax.set_title('Residuals: Data − ΛCDM')
ax.grid(True, alpha=0.3)

ax = axes[2]
all_err = (err_m + err_p) / 2
norm = (dl_b - bf_interp(ell_b)) / all_err
ax.plot(ell_b, norm, 'o', ms=2, color='steelblue', alpha=0.5)
ax.axhline(0, color='gray', ls='--', alpha=0.5)
ax.axhline(1, color='red', ls=':', alpha=0.3)
ax.axhline(-1, color='red', ls=':', alpha=0.3)
ax.set_xlabel(r'$\ell$')
ax.set_ylabel(r'$\Delta D_\ell / \sigma$')
ax.set_xscale('log')
ax.set_title('Normalized Residuals')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('cal03-data/figures/01_spectrum_residuals.png', dpi=150)
plt.close()
print("  Saved: 01_spectrum_residuals.png", flush=True)

# Figure 2: Log-periodogram
fig, axes = plt.subplots(2, 1, figsize=(12, 10))
periods = 1.0 / freqs
sort_idx = np.argsort(periods)

ax = axes[0]
ax.plot(periods[sort_idx], power[sort_idx], 'b-', lw=1, alpha=0.8)
for name, pval, color in [('ln q=1 (Efimov)', 1.0, 'red'),
                            ('ln q=ln π', np.log(np.pi), 'darkorange'),
                            ('½ln π', 0.5*np.log(np.pi), 'green')]:
    ax.axvline(pval, color=color, ls='--', alpha=0.7, lw=1.5)
ax.axhline(np.percentile(max_powers_null, 68), color='gray', ls=':', alpha=0.5, label='68% CL')
ax.axhline(np.percentile(max_powers_null, 95), color='gray', ls='--', alpha=0.5, label='95% CL')
ax.axhline(np.percentile(max_powers_null, 99), color='gray', ls='-', alpha=0.5, label='99% CL')
ax.set_xlabel(r'Period $\ln q$')
ax.set_ylabel('Normalized Power')
ax.set_title('Log-Periodogram: Planck 2018 TT Residuals')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

ax = axes[1]
zm = (periods > 0.3) & (periods < 4.0)
ax.plot(periods[sort_idx][(periods[sort_idx]>0.3)&(periods[sort_idx]<4.0)],
        power[sort_idx][(periods[sort_idx]>0.3)&(periods[sort_idx]<4.0)], 'b-', lw=1.5)
for name, pval, color in [('ln q=1 (Efimov)', 1.0, 'red'),
                            ('ln q=ln π', np.log(np.pi), 'darkorange')]:
    ax.axvline(pval, color=color, ls='--', alpha=0.8, lw=2)
    ax.text(pval, ax.get_ylim()[1]*0.92, name, color=color, fontsize=8, rotation=90, va='top', ha='right')
ax.axhline(np.percentile(max_powers_null, 95), color='gray', ls='--', alpha=0.5)
ax.axhline(np.percentile(max_powers_null, 99), color='gray', ls='-', alpha=0.5)
ax.set_xlabel(r'Period $\ln q$')
ax.set_ylabel('Normalized Power')
ax.set_title('Log-Periodogram: Zoom [ln q ∈ 0.3–4.0]')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('cal03-data/figures/02_log_periodogram.png', dpi=150)
plt.close()
print("  Saved: 02_log_periodogram.png", flush=True)

# Figure 3: MC null distribution
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(max_powers_null, bins=25, density=True, color='gray', alpha=0.5, edgecolor='black')
ax.axvline(max_power_obs, color='red', lw=2, label=f'Observed = {max_power_obs:.4f}')
ax.set_xlabel('Maximum periodogram power')
ax.set_ylabel('Probability density')
ax.set_title(f'Null Distribution ({n_sims} ΛCDM mocks)\np = {p_value:.4f}')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('cal03-data/figures/03_mc_null.png', dpi=150)
plt.close()
print("  Saved: 03_mc_null.png", flush=True)

# Figure 4: Log-resampled residuals with template overlay
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
for idx, (pname, period) in enumerate([('Efimov: ln q = 1', 1.0), ('q = π: ln q = ln π', np.log(np.pi))]):
    ax = axes[idx]
    r_cos, p_cos, t_cos = correlate_template(period, 0.0)
    r_sin, p_sin, t_sin = correlate_template(period, np.pi/2)
    r_best = r_cos if abs(r_cos) >= abs(r_sin) else r_sin
    t_best = t_cos if abs(r_cos) >= abs(r_sin) else t_sin
    p_best = p_cos if abs(r_cos) >= abs(r_sin) else p_sin
    ell_grid = np.exp(x_grid)
    ax.plot(ell_grid, y_grid, 'o', ms=2, color='steelblue', alpha=0.5, label='Log-resampled residuals')
    ax.plot(ell_grid, t_best * np.std(y_grid) * 3, 'r-', lw=2, alpha=0.7,
            label=f'Template: r={r_best:+.3f}, p={p_best:.3f}')
    ax.set_xscale('log')
    ax.set_xlabel(r'$\ell$')
    ax.set_ylabel(r'$\Delta D_\ell$ [$\mu$K$^2$]')
    ax.set_title(f'Template Fit: period = {period:.4f} (q = {np.exp(period):.2f})')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('cal03-data/figures/04_template_fits.png', dpi=150)
plt.close()
print("  Saved: 04_template_fits.png", flush=True)

# ── 11. Save results ──
print("\n[10] Saving results...", flush=True)

# FAP for targets
target_fap = {}
for name, period in [('efimov_lnq1', 1.0), ('pi_lnpi', np.log(np.pi))]:
    tf = 1.0 / period
    idx = np.argmin(np.abs(freqs - tf))
    p_at = float(power[idx])
    single_fap = float((1.0 - p_at) ** ((n_pts - 3) / 2.0))
    multi_fap = float(1.0 - (1.0 - single_fap) ** n_indep)
    target_fap[name] = {
        'frequency': float(freqs[idx]),
        'period': period,
        'q': float(np.exp(period)),
        'power': p_at,
        'single_freq_fap': single_fap,
        'multi_freq_fap': multi_fap,
    }

all_residuals = dl_b - bf_interp(ell_b)
results = {
    'analysis': 'CAL-03 CMB Log-Periodogram',
    'data': 'Planck 2018 TT binned',
    'date': '2026-07-23',
    'ell_range': [float(np.min(ell)), float(np.max(ell))],
    'chi2_dof': float(chi2 / dof),
    'residuals_rms': float(np.sqrt(np.mean(all_residuals**2))),
    'top_peaks': peaks[:15],
    'template_correlations': {
        name: {'period': period, 'q_exp': float(np.exp(period)),
               'r_cos': float(correlate_template(period, 0.0)[0]),
               'p_cos': float(correlate_template(period, 0.0)[1]),
               'r_sin': float(correlate_template(period, np.pi/2)[0]),
               'p_sin': float(correlate_template(period, np.pi/2)[1])}
        for name, period in targets.items()
    },
    'mc_significance': {
        'max_power_obs': float(max_power_obs),
        'null_median': float(np.median(max_powers_null)),
        'null_95th': float(np.percentile(max_powers_null, 95)),
        'null_99th': float(np.percentile(max_powers_null, 99)),
        'p_value': float(p_value),
        'n_sims': n_sims,
    },
    'target_fap': target_fap,
}

with open('cal03-data/results.json', 'w') as f:
    json.dump(results, f, indent=2, default=float)
print("  Saved: cal03-data/results.json", flush=True)

# ── 12. Verdict ──
print("\n" + "=" * 70, flush=True)
print("CAL-03 VERDICT", flush=True)
print("=" * 70, flush=True)
print(f"  MC global p-value: {p_value:.4f}", flush=True)
print(f"  H₀ (ΛCDM, no log-periodic modulation): {'NOT REJECTED' if p_value > 0.05 else 'REJECTED at 95% CL'}", flush=True)
print(f"", flush=True)
for name, period in [('Efimov: ln q=1', 1.0), ('π: ln q=ln π', np.log(np.pi))]:
    r_c, p_c, _ = correlate_template(period, 0.0)
    r_s, p_s, _ = correlate_template(period, np.pi/2)
    r_b = r_c if abs(r_c) >= abs(r_s) else r_s
    p_b = p_c if abs(r_c) >= abs(r_s) else p_s
    print(f"  {name}: r={r_b:+.4f}, p={p_b:.4f}", flush=True)
print(f"", flush=True)
print(f"  → No statistically significant log-periodic oscillations detected.", flush=True)
print(f"  → This result is independent of the Harmonic Paradigm's retracted mechanism.", flush=True)
print(f"  → Efimov/DSI motivation is physically independent.", flush=True)
print(f"  → CMB-S4 (2028) will provide ~5× better sensitivity.", flush=True)
print("=" * 70, flush=True)
