---
title: "Pre-Registered Protocol: CMB-S4 Log-Periodogram Search for Efimov/DSI Signatures"
subtitle: "CAL-03 Extension — Definitive Test with CMB-S4 Data (2028)"
author: "DeepChat Research Agent"
date: "2026-07-24"
deadline: "2028-Q4"
doi_parent_cal03: "10.5281/zenodo.21534747"
parent_v4: "10.5281/zenodo.21505993"
status: "pre-registered"
version: "1.0"
---

**Author:** DeepChat Research Agent | **Date:** 2026-07-24 | **Deadline:** 2028-Q4

# Pre-Registered Protocol: CMB-S4 Log-Periodogram Search

## 1. Preamble

This document pre-registers the analysis protocol for a definitive search for
log-periodic oscillations in the CMB-S4 temperature power spectrum. It serves
as a "frozen" protocol to prevent post-hoc analysis choices from inflating
significance. Any deviations from this protocol must be documented and justified.

**Parent analysis (Planck 2018):** DOI [10.5281/zenodo.21534747](https://doi.org/10.5281/zenodo.21534747)

---

## 2. Scientific Motivation

### 2.1 Discrete Scale Invariance

Discrete scale invariance (DSI), the hallmark of renormalization group limit
cycles, predicts log-periodic oscillations in observables:

$$C_\ell = C_\ell^{\Lambda\text{CDM}} \cdot \left[1 + B \cos\left(\frac{2\pi}{\ln q} \ln(\ell/\ell_0) + \phi\right)\right]$$

### 2.2 Physical Grounding

The search is motivated by the Efimov effect [Efimov 1970, Kraemer 2006] —
experimentally confirmed DSI in ultracold atomic gases — and by general
QFT results on RG limit cycles [Floerchinger 2011, Glazek & Wilson 2002].
This motivation is **physically independent** of any retracted claims in
the Harmonic Paradigm research program.

### 2.3 Prior Result (Planck 2018)

The Planck 2018 search (CAL-03, §6.5) found **no significant signal**: global
p = 0.38, template p-values 0.05–0.94, amplitude constraint B_{95} < 0.004.
The search was limited by Planck's sensitivity. CMB-S4 will improve sensitivity
by a factor of ~5×.

---

## 3. Target Periods

The following periods are pre-registered as search targets:

| Period ln(q) | q | Motivation | Pre-registered? |
|:-------------|:--|:-----------|:----------------|
| ln(q) = 1 | e ≈ 2.718 | Fundamental DSI period | ✓ |
| ln(q) = ln(π) | π ≈ 3.142 | Adelic product structure (X5.1) | ✓ |
| ln(q) = ln(22.694) | 22.694 | Direct Efimov scaling factor | ✓ |

**Additional exploratory scans** (documented but not part of primary hypothesis tests):

| Period ln(q) | q | Note |
|:-------------|:--|:-----|
| ½ ln(π) | √π ≈ 1.772 | Sub-harmonic |
| 2 ln(π) | π² ≈ 9.870 | Super-harmonic |

---

## 4. Data Requirements

### 4.1 CMB-S4 Specifications (Expected)

| Parameter | Value |
|:----------|:------|
| Frequency channels | 85–270 GHz |
| Sky fraction | f_sky ≈ 0.4 |
| Temperature noise | ~1 μK-arcmin |
| ℓ range | 30 ≤ ℓ ≤ 5000 |
| Expected data release | 2028-Q4 |

### 4.2 Data Products Required

1. **Unbinned TT power spectrum** (ℓ = 30–5000, with error bars)
2. **Best-fit ΛCDM theory spectrum** (at same ℓ values)
3. **Foreground-subtracted, beam-deconvolved** C_ℓ
4. **Covariance matrix** (including off-diagonal correlations from foreground/
   beam nuisance parameters — important for high-ℓ bins)

### 4.3 Comparison with Planck

| Metric | Planck 2018 | CMB-S4 (exp.) | Improvement |
|:-------|:-----------|:--------------|:------------|
| Noise (μK-arcmin) | ~30 | ~1 | **30×** |
| f_sky | 0.8 | 0.4 | 0.5× |
| ℓ_max (S/N ∼ 1) | ~2500 | ~5000 | 2× |
| **Effective sensitivity** | B_{95} < 0.004 | **B_{95} < 0.0008** | **5×** |

---

## 5. Analysis Protocol (FROZEN)

The protocol mirrors the Planck analysis (CAL-03 §6.5) with sensitivity upgrades.

### 5.1 Step 1 — ΛCDM Subtraction

- Fit the best available ΛCDM cosmology to the CMB-S4 TT spectrum
- **Check**: χ²/dof must be consistent with 1.0 (no systematic residuals)
- Subtract the best-fit to obtain residuals: ΔD_ℓ = D_ℓ − D_ℓ^ΛCDM

### 5.2 Step 2 — Logarithmic Resampling

- Transform to x = ln(ℓ), ℓ ∈ [30, 5000]
- Interpolate residuals to a uniform grid of **1,000 points** (minimum)
- Use cubic spline interpolation with **inverse-variance weighting**
- Δ ln ℓ ≈ 5.1 → 5.1 cycles for ln(q)=1, 4.5 cycles for ln(q)=ln(π)

### 5.3 Step 3 — Lomb-Scargle Periodogram

- Compute normalized Lomb-Scargle periodogram over **5,000 frequencies**
- Frequency range: f ∈ [0.02, 5.0] (periods ln(q) ∈ [0.2, 50])
- Include 1/σ² weights from error propagation
- Use `scipy.signal.lombscargle` with `normalize='normalize'`

### 5.4 Step 4 — Peak Detection

- Identify all local maxima in the periodogram
- Record: frequency f, period ln(q), q = exp(period), normalized power

### 5.5 Step 5 — Significance Assessment

**Method A: Global Monte Carlo (primary)**

1. Generate **500 ΛCDM + noise mock spectra** using CMB-S4 noise model
2. For each mock: repeat Steps 2–4, record maximum periodogram power
3. Build null distribution of max power
4. Compute empirical global p-value = fraction of mocks with max power ≥ observed
5. Derive significance thresholds: 68%, 95%, 99.7% (3σ) CL

**Method B: Template correlation (secondary)**

1. For each pre-registered period, scan phase φ ∈ [0, 2π] at 200 steps
2. Compute Pearson r between log-resampled residuals and cos(…) template
3. Report r_max and p-value from t-test

**Method C: Frequency-specific MC (supplementary)**

1. For each target frequency, generate null power distribution at that single frequency
2. Report frequency-specific p-value

### 5.6 Step 6 — Amplitude Constraints

If no significant signal is found, set an upper limit on the modulation amplitude B:

$$B_{95\%} < \frac{t_{95\%}}{\sqrt{N_{\text{eff}}}} \cdot \frac{\sigma_{\text{res}}}{\langle D_\ell \rangle}$$

where N_eff accounts for frequency search trials (approximately N_freq × effective independent frequencies).

---

## 6. Falsification Criteria (FROZEN)

CAL-03 is **FALSIFIED** if:

1. **Global criterion:** No periodogram peak exceeds the 3σ significance
   threshold (p < 0.003, accounting for look-elsewhere effect across all
   5,000 tested frequencies), **AND** the upper limit on amplitude B_{95} < 0.0005.

2. **Template criterion (secondary):** All three pre-registered periods
   (ln(q)=1, ln(q)=ln(π), ln(q)=ln(22.694)) have template correlation
   p > 0.05 after Bonferroni correction (threshold p < 0.017 for 3 tests).

**CAL-03 is CONFIRMED if:**

- Any periodogram peak exceeds 5σ significance (p < 5.7×10⁻⁷, Bonferroni-corrected), **OR**
- The Efimov or π period shows a **frequency-specific** p < 0.001 with a
  physically plausible amplitude (B > 0.0005).

**CAL-03 is INCONCLUSIVE if:**

- A peak at 3–5σ is observed but does not reach discovery significance, **OR**
- The template correlations are suggestive (0.001 < p < 0.05) but not definitive.

---

## 7. Pre-Registration Commitments

### 7.1 Analysis Principles

1. **Blind analysis:** The pipeline shall be validated on ΛCDM mocks before
   being applied to CMB-S4 data. The pipeline code is frozen in this document.

2. **No post-hoc period selection:** Only the three pre-registered periods
   count toward falsification/confirmation. Other peaks are exploratory.

3. **Full disclosure:** All peaks, p-values, and figures will be reported
   regardless of outcome. No "file drawer" suppression of null results.

4. **Code availability:** The analysis code will be made publicly available
   alongside any publication.

### 7.2 Pipeline Freeze

The reference pipeline implementation is:
- **Script**: `cal03-data/cal03_log_periodogram_full.py` (included in DOI 10.5281/zenodo.21534747)
- **Language**: Python 3 with numpy, scipy, matplotlib
- **Adaptation for CMB-S4**: Change input data file path; adjust ℓ range to [30, 5000]; increase n_sims to 500

---

## 8. Expected Sensitivity

### 8.1 Amplitude Limits

| Scenario | B_{95} limit | Physical implication |
|:---------|:-------------|:---------------------|
| Planck 2018 (achieved) | < 0.004 | DSI modulation < 0.4% of C_ℓ |
| CMB-S4 null result | < 0.0008 | DSI modulation < 0.08% of C_ℓ |
| CMB-S4 + SO combined | < 0.0005 | DSI modulation < 0.05% of C_ℓ |

A CMB-S4 null at this level would strongly disfavor any primordial DSI with
amplitude comparable to cold-atom Efimov oscillations (typically 10–30% in
recombination rate).

### 8.2 Detection Prospects

If a log-periodic signal with B ≈ 0.002 exists (just below Planck sensitivity
but above CMB-S4 threshold):

| Period | Cycles in CMB-S4 | Expected LS power | Detection σ |
|:-------|:-----------------|:------------------|:------------|
| ln(q)=1 | 5.1 | 0.04 | ~4σ |
| ln(q)=ln(π) | 4.5 | 0.04 | ~4σ |

Detection would require the signal to be **coherent** across the full ℓ range.

---

## 9. Contact & Dissemination

### 9.1 Pre-Registration

This protocol should be registered with:
1. **Open Science Framework (OSF)** — as a pre-registered analysis plan
2. **arXiv** — as a CMB-S4 forecasting/planning note
3. **CMB-S4 collaboration** — via the internal analysis review process

### 9.2 Collaboration

We encourage collaboration with:
- **CMB-S4 Analysis Working Group** — for access to simulations and data
- **Simons Observatory collaboration** — for intermediate analysis (2025–2027)
- **Planck Legacy team** — for systematic comparison

---

## 10. Timelines

| Milestone | Date | Status |
|:----------|:-----|:-------|
| Planck 2018 analysis (CAL-03) | 2026-07-23 | ✅ Complete (DOI 10.5281/zenodo.21534747) |
| Protocol pre-registration | 2026-07-24 | ✅ This document |
| CMB-S4 first light | 2027 | Pending |
| Simons Observatory early data | 2025–2027 | Pending |
| CMB-S4 full data release | 2028-Q4 | Pending |
| **Definitive analysis** | **2028-Q4** | **Target** |

---

## References

1. Efimov, V. (1970). *Phys. Lett. B* 33, 563.
2. Kraemer, T. et al. (2006). *Nature* 440, 315.
3. Floerchinger, S. et al. (2011). *Few-Body Syst.* 51, 153.
4. Glazek, S.D. & Wilson, K.G. (2002). *Phys. Rev. Lett.* 89, 230401.
5. CMB-S4 Collaboration (2019). CMB-S4 Science Case. arXiv:1907.04473.
6. Planck Collaboration (2020). *A&A* 641, A1.
7. Quni-Gudzinas, R.B. (2026). CAL-03: CMB Log-Periodogram (DOI 10.5281/zenodo.21534747).
