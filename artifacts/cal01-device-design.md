---
title: "CAL-01 Phase 1 — Device Design"
date: "2026-07-23"
status: "complete"
parent: "CAL-01 Transmon Anharmonicity Measurement Program"
parent_doc: "CAL-01-transmon-measurement-program.md"
---

# CAL-01 Phase 1 — Device Design

**Date:** 2026-07-23
**Status:** COMPLETE
**Deliverable:** Device parameter set, junction/capacitor geometry, EM simulation specs, mask layout specs

---

## 1. Finalized 8-Device Parameter Set

### 1.1 Design Strategy

All 8 devices share the same target qubit frequency $\omega_{01}/2\pi \approx 5.0$ GHz to enable
a single readout chain (common JPA/TWPA bandwidth, single LO frequency).
The ratio $E_J/E_C$ is varied from 50 to 1500 by independently controlling $E_J$ (via
junction critical current $I_c$) and $E_C$ (via shunt capacitance $C_\Sigma$).

For a fixed $\omega_{01}$ target, $E_J$ and $E_C$ are determined by the Koch relation:

$$\omega_{01} \approx \sqrt{8E_J E_C} - E_C$$

With $E_C = E_J/(E_J/E_C)$, we solve for $E_J$:

$$E_J = \frac{\omega_{01}}{\sqrt{8/(E_J/E_C)} - 1/(E_J/E_C)}$$

### 1.2 Computed Parameters ($J_c = 1.0$ kA/cm² baseline)

| ID | $E_J/E_C$ | $E_J/h$ (GHz) | $E_C/h$ (MHz) | $\omega_{01}/2\pi$ (GHz) | $\vert\alpha\vert/2\pi$ (MHz) | $\alpha_r$ | $\nu$ (Koch) | $\nu$ (SC) | $I_c$ (nA) | $A_j$ ($\mu$m²) | $C_\Sigma$ (fF) | $\varepsilon_{\text{disp}}$ |
|:---|:--------:|:----------:|:----------:|:----------:|:-----------:|:------:|:--------:|:--------:|:-------:|:----------:|:---------:|:--------------:|
| A-050 | 50 | 13.2 | 263.2 | 5.000 | 263.2 | 0.050000 | 0.550000 | 0.542364 | 26 | 0.0027 | 73.6 | $2.1\times 10^{-9}$ |
| A-100 | 100 | 18.3 | 183.3 | 5.000 | 183.3 | 0.035355 | 0.535355 | 0.530695 | 37 | 0.0037 | 105.7 | $5.2\times 10^{-13}$ |
| A-200 | 200 | 25.6 | 128.2 | 5.000 | 128.2 | 0.025000 | 0.525000 | 0.522223 | 52 | 0.0052 | 151.1 | $4.2\times 10^{-18}$ |
| A-350 | 350 | 33.7 | 96.3 | 5.000 | 96.3 | 0.018898 | 0.518898 | 0.517097 | 68 | 0.0068 | 201.1 | $1.0\times 10^{-23}$ |
| A-500 | 500 | 40.2 | 80.3 | 5.000 | 80.3 | 0.015811 | 0.515811 | 0.514453 | 81 | 0.0081 | 241.1 | $3.4\times 10^{-28}$ |
| A-750 | 750 | 49.0 | 65.4 | 5.000 | 65.4 | 0.012910 | 0.512910 | 0.511930 | 99 | 0.0099 | 296.2 | $2.3\times 10^{-34}$ |
| A-1000 | 1000 | 56.5 | 56.5 | 5.000 | 56.5 | 0.011180 | 0.511180 | 0.510405 | 114 | 0.0114 | 342.6 | $1.4\times 10^{-39}$ |
| A-1500 | 1500 | 69.1 | 46.1 | 5.000 | 46.1 | 0.009129 | 0.509129 | 0.508574 | 139 | 0.0139 | 420.5 | $2.7\times 10^{-48}$ |

**Key observations:**
- All $\omega_{01}/2\pi = 5.000 \pm 0.001$ GHz — single readout chain feasible
- $\vert\alpha\vert/2\pi$ ranges from 263 MHz (A-050, easily resolvable) to 46 MHz (A-1500, challenging but measurable with Ramsey + two-tone)
- $\nu$ ranges from 0.5500 to 0.5091 — wide dynamic range for fitting
- $\Delta\nu$ (SC − Koch) ranges from $-7.6 \times 10^{-3}$ to $-5.5 \times 10^{-4}$ — distinguishing models requires $\sigma_\nu < 0.002$ at low $E_J/E_C$
- Charge dispersion $\varepsilon_{\text{disp}} < 2 \times 10^{-9}$ for ALL devices — charge noise negligible

### 1.3 Expected Spectroscopic Features

| ID | $\omega_{01}/2\pi$ (GHz) | $\omega_{12}/2\pi$ (GHz) | $\omega_{23}/2\pi$ (GHz) | $g_{01}$ (MHz) | Leakage risk |
|:---|:-------:|:-------:|:-------:|:-----:|:-----|
| A-050 | 5.000 | 4.737 | 4.211 | — | Low |
| A-100 | 5.000 | 4.817 | 4.451 | — | Low |
| A-200 | 5.000 | 4.872 | 4.616 | — | Low |
| A-350 | 5.000 | 4.904 | 4.711 | — | Low |
| A-500 | 5.000 | 4.920 | 4.760 | — | Low |
| A-750 | 5.000 | 4.935 | 4.804 | — | Low |
| A-1000 | 5.000 | 4.944 | 4.831 | — | Very low |
| A-1500 | 5.000 | 4.954 | 4.862 | — | Very low |

At $E_J/E_C > 500$, $\omega_{12}$ is within 80 MHz of $\omega_{01}$ — requires
narrowband filtering to separate $\vert 0\rangle \rightarrow \vert 1\rangle$ and
$\vert 1\rangle \rightarrow \vert 2\rangle$ transitions. A Purcell filter with
bandwidth $\sim$50 MHz is recommended.

---

## 2. Junction Geometry Design

### 2.1 Al/AlO$_x$/Al Tunnel Junctions

**Fabrication method:** Dolan-bridge shadow evaporation (standard for Al junctions).

**Critical current density $J_c$:** Tunable via oxidation pressure $P_{\text{O}_2}$ and time $t_{\text{ox}}$:

$$J_c \propto \exp\left(-\alpha \sqrt{P_{\text{O}_2} \cdot t_{\text{ox}}}\right)$$

| Oxidation Regime | $P_{\text{O}_2}$ (mbar) | $t_{\text{ox}}$ (min) | $J_c$ (kA/cm²) | Application |
|:---|:---:|:---:|:---:|:---|
| Light | 0.01–0.1 | 5–15 | 5–20 | High-$I_c$ junctions (A-500+) |
| Standard | 0.1–1.0 | 10–30 | 1–5 | Mid-range (A-100–A-350) |
| Heavy | 1.0–10 | 20–60 | 0.1–1 | Low-$I_c$, large area (A-050) |

### 2.2 Junction Dimensions

Junction area $A_j = I_c / J_c$. Using $J_c = 1.0$ kA/cm² as baseline:

| ID | $I_c$ (nA) | $A_j$ ($\mu$m²) | Side (nm, square) | $J_c$ alt (kA/cm²) | $A_j$ alt ($\mu$m²) | Side alt (nm) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| A-050 | 26 | 0.0027 | 52 | 0.5 | 0.0053 | 73 |
| A-100 | 37 | 0.0037 | 61 | 0.5 | 0.0074 | 86 |
| A-200 | 52 | 0.0052 | 72 | 0.5 | 0.0103 | 102 |
| A-350 | 68 | 0.0068 | 83 | 0.5 | 0.0136 | 117 |
| A-500 | 81 | 0.0081 | 90 | 2.0 | 0.0041 | 64 |
| A-750 | 99 | 0.0099 | 100 | 2.0 | 0.0050 | 71 |
| A-1000 | 114 | 0.0114 | 107 | 2.0 | 0.0057 | 76 |
| A-1500 | 139 | 0.0139 | 118 | 2.0 | 0.0070 | 84 |

**Alternative column** shows dimensions using $J_c = 0.5$ kA/cm² for low-$E_J/E_C$ devices
(easier fabrication with larger junctions, lower $I_c$ drift) and $J_c = 2.0$ kA/cm²
for high-$E_J/E_C$ devices (smaller junctions for higher $E_J$ with manageable area).

**Fabrication note:** All junction dimensions are within standard e-beam lithography
capability ($\geq 50$ nm minimum feature). The smallest junction (52 nm) at $J_c = 1.0$
kA/cm² is at the edge of routine fabrication; using the alternative $J_c = 0.5$ kA/cm²
for A-050 through A-350 increases the minimum feature to 73 nm for better yield.

### 2.3 Junction Resistance at Room Temperature

Ambegaokar-Baratoff relation at $T = 0$:

$$I_c R_n = \frac{\pi\Delta}{2e} \approx 320\ \mu\text{V} \quad (\text{Al}, \Delta \approx 200\ \mu\text{eV})$$

At 300 K, the subgap resistance is dominated by thermally activated quasiparticles.
Room-temperature junction resistance $R_n(300\ \text{K})$ provides a screening
measurement to verify $I_c$ before cooldown:

| ID | $I_c$ (nA) | $R_n(0)$ (k$\Omega$) | $R_n(300\text{K})$ (k$\Omega$) | Screening pass |
|:---|:---:|:---:|:---:|:---:|
| A-050 | 26 | 12.3 | 8–12 | Yes |
| A-100 | 37 | 8.7 | 5–9 | Yes |
| A-200 | 52 | 6.2 | 4–6 | Yes |
| A-350 | 68 | 4.7 | 3–5 | Yes |
| A-500 | 81 | 4.0 | 2.5–4 | Yes |
| A-750 | 99 | 3.2 | 2–3.5 | Yes |
| A-1000 | 114 | 2.8 | 1.8–3 | Yes |
| A-1500 | 139 | 2.3 | 1.5–2.5 | Yes |

$R_n(300\text{K})$ is typically $0.6–0.9 \times R_n(0)$ due to thermal smearing.
Measured $R_n$ within ±20% of target indicates correct junction area.

---

## 3. Capacitor Geometry Design

### 3.1 Shunt Capacitance Design

$C_\Sigma = C_{\text{shunt}} + C_j + C_{\text{parasitic}}$, where:
- $C_j \approx 1–5$ fF is the intrinsic junction capacitance (negligible for large shunts)
- $C_{\text{parasitic}} \approx 1–5$ fF from wiring and pad coupling
- $C_{\text{shunt}}$ is the designed interdigitated or parallel-plate capacitor

**Dominant contribution:** $C_{\text{shunt}}$, realized as an interdigitated capacitor
(IDC) on the qubit island, coupled to a ground plane.

### 3.2 Interdigitated Capacitor (IDC)

For an IDC on a sapphire ($\varepsilon_r = 9.4–11.5$) or high-resistivity silicon
($\varepsilon_r = 11.7$) substrate, the capacitance per unit length is:

$$C_{\text{IDC}} \approx \varepsilon_0 \cdot \frac{(1 + \varepsilon_r)}{2} \cdot \frac{K(k')}{K(k)} \cdot (N-1) \cdot L$$

where $K(k)$ is the complete elliptic integral of the first kind,
$k = \tan^2(\pi w/4(w+g))$, $k' = \sqrt{1-k^2}$, $N$ = number of fingers,
$L$ = finger length, $w$ = finger width, $g$ = gap between fingers.

**Practical design (sapphire substrate, $\varepsilon_r = 10$):**

| ID | $C_\Sigma$ (fF) | $N$ fingers | $L$ ($\mu$m) | $w$ ($\mu$m) | $g$ ($\mu$m) | Area ($\mu$m²) | Geometry |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| A-050 | 73.6 | 20 | 200 | 5 | 5 | $200 \times 200$ | Compact IDC |
| A-100 | 105.7 | 20 | 300 | 5 | 5 | $200 \times 300$ | IDC |
| A-200 | 151.1 | 20 | 400 | 5 | 5 | $200 \times 400$ | IDC |
| A-350 | 201.1 | 24 | 400 | 5 | 5 | $240 \times 400$ | IDC |
| A-500 | 241.1 | 28 | 400 | 5 | 5 | $280 \times 400$ | IDC |
| A-750 | 296.2 | 32 | 400 | 5 | 5 | $320 \times 400$ | IDC |
| A-1000 | 342.6 | 36 | 400 | 5 | 5 | $360 \times 400$ | IDC |
| A-1500 | 420.5 | 44 | 400 | 5 | 5 | $440 \times 400$ | IDC |

**Design rules:**
- Finger width $w = 5\ \mu$m (well above lithography limit, low kinetic inductance)
- Gap $g = 5\ \mu$m (avoids significant fringe-field cross-coupling)
- Finger length $L = 200–400\ \mu$m (keeps total capacitor footprint compact)
- $N$ adjusted to achieve exact $C_\Sigma$ target
- All designs fit within $500 \times 500\ \mu$m² chip area per qubit

### 3.3 Alternative: Parallel-Plate Capacitor

For the highest-$E_J/E_C$ devices (A-750 through A-1500), a parallel-plate design
with a $100$ nm thick amorphous silicon ($a$-Si:H) dielectric may simplify layout:

$$C = \varepsilon_0 \varepsilon_r \frac{A}{d}$$

With $\varepsilon_r(a\text{-Si:H}) \approx 11$, $d = 100$ nm:

| ID | $C_\Sigma$ (fF) | Plate area ($\mu$m²) | Side ($\mu$m) |
|:---|:---:|:---:|:---:|
| A-750 | 296 | $3.0 \times 10^2$ | 17 |
| A-1000 | 343 | $3.5 \times 10^2$ | 19 |
| A-1500 | 421 | $4.3 \times 10^2$ | 21 |

**Trade-off:** Parallel-plate is more compact, but $a$-Si:H introduces TLS (two-level
system) defects at the dielectric interfaces, degrading $T_1$. IDC (no deposited
dielectric, uses substrate $\varepsilon_r$) is preferred for low-loss operation.
**Recommendation: use IDC for all devices.**

### 3.4 Capacitor Cross-Talk Mitigation

- Minimum 200 $\mu$m center-to-center spacing between adjacent qubit capacitors
- Ground plane between qubits ($\geq 50\ \mu$m wide)
- Staggered finger orientation (alternate 0°/90° between neighbors) to minimize
  mutual inductance

---

## 4. Readout Resonator Design

### 4.1 Dispersive Readout

Each qubit is capacitively coupled to a $\lambda/4$ coplanar waveguide (CPW)
readout resonator. In the dispersive regime ($\vert\Delta\vert \gg g$):

$$\chi = \frac{g^2}{\Delta}$$

where $\Delta = \omega_q - \omega_r$ is the qubit-resonator detuning and $g/2\pi$
is the coupling strength.

**Design targets:**

| Parameter | Value | Rationale |
|:---|:---:|:---|
| $\omega_r/2\pi$ | $6.5$–$7.0$ GHz | Detuned $\sim 1.5$–$2.0$ GHz above $\omega_{01}$ |
| $\Delta/2\pi$ | $1.5$–$2.0$ GHz | Dispersive shift $> 1$ MHz for all $\vert\alpha\vert$ |
| $g/2\pi$ | $100$–$150$ MHz | Moderate coupling; strong enough for readout, weak enough for dispersive |
| $\kappa/2\pi$ (linewidth) | $1$–$5$ MHz | Fast readout ($\kappa^{-1} \sim 30$–$160$ ns) |
| $\chi/2\pi$ | $5$–$15$ MHz | Resolvable with JPA |

**Single readout chain:** All 8 qubits share the same readout frequency band
because all $\omega_{01} \approx 5.0$ GHz. A common feedline with frequency-multiplexed
resonators ($\omega_r$ spaced by $50$–$100$ MHz at $6.5$–$7.2$ GHz) enables
simultaneous readout.

### 4.2 Purcell Filter

For the deep-transmon devices (A-500 through A-1500), the Purcell-limited $T_1$
is especially important because $\vert\alpha\vert$ is small and leakage to $\vert 2\rangle$
must be controlled:

$$T_1^{\text{Purcell}} \approx \frac{(\Delta/g)^2}{\kappa}$$

For $\Delta/2\pi = 1.5$ GHz, $g/2\pi = 150$ MHz, $\kappa/2\pi = 5$ MHz:

$$T_1^{\text{Purcell}} \approx \frac{(1500/150)^2}{5\ \text{MHz}} = \frac{100}{3.14 \times 10^7} \approx 3\ \mu\text{s}$$

**Recommendation:** Add a Purcell bandpass filter (quarter-wave stub or
lumped-element LC) on the readout line to achieve $T_1^{\text{Purcell}} > 50\ \mu$s.

---

## 5. Electromagnetic Simulation Specifications

### 5.1 Simulation Scope

| Parameter | Tool | Mesh | Frequency Range |
|:---|:---|:---|:---|
| IDC capacitance | Sonnet EM | $1\ \mu$m cell, adaptive | DC–10 GHz |
| Junction inductance extraction | HFSS eigenmode | $0.5\ \mu$m near junction | 4–8 GHz |
| Qubit-resonator coupling $g$ | HFSS driven modal | $2\ \mu$m adaptive | 5–7 GHz |
| Cross-talk (capacitive + inductive) | Sonnet EM | $2\ \mu$m cell | DC–10 GHz |
| Chip-mode analysis (package resonances) | HFSS eigenmode | $50\ \mu$m adaptive | DC–15 GHz |
| Flux-bias line mutual inductance | FastHenry / HFSS | $1\ \mu$m adaptive | DC–1 GHz |

### 5.2 Material Properties for Simulation

| Material | Layer | Thickness | $\varepsilon_r$ | $\tan\delta$ | $\sigma$ (S/m) | Notes |
|:---|:---|:---:|:---:|:---:|:---:|:---|
| Sapphire | Substrate | $430\ \mu$m | 9.4 (∥c) / 11.5 (⊥c) | $2\times 10^{-6}$ | — | Low-loss at mK |
| Al (superconducting) | Metal | $80$ nm | — | — | $\lambda_L \approx 50$ nm | London penetration |
| AlO$_x$ | Tunnel barrier | $\sim 2$ nm | $\sim 8$ | $\sim 10^{-3}$ | — | Model as lumped $C_j$ |
| Si (if HR-Si) | Substrate | $500\ \mu$m | 11.7 | $5\times 10^{-5}$ | $10^{-4}$ (depleted) | Alternative substrate |
| Photoresist | Spacer | $1.5\ \mu$m | 3.0 | 0.02 | — | Remove before cold test |

### 5.3 Simulation Checklist

1. **[ ] IDC capacitance:** Extract S-parameters from Sonnet layout → fit to $C_\Sigma$
2. **[ ] Junction inductance:** Verify $E_J/h$ from $I_c$ (cannot simulate tunnel
   barrier directly; treat as lumped $L_J = \Phi_0/(2\pi I_c)$)
3. **[ ] $\omega_{01}$ verification:** Eigenmode simulation of full qubit+readout
   layout → confirm $\omega_{01} \approx 5.0 \pm 0.1$ GHz
4. **[ ] $\alpha$ from eigenmodes:** Extract $\omega_{12} - \omega_{01}$ from
   first 3 eigenmodes (E + EPR method) → cross-check against Koch theory
5. **[ ] Readout coupling:** Driven modal simulation → extract external $Q_e$,
   verify $\kappa/2\pi = 1$–$5$ MHz
6. **[ ] Cross-talk matrix:** Simulate all 8 qubits + resonators simultaneously →
   verify nearest-neighbor coupling $< 100$ kHz
7. **[ ] Package modes:** Eigenmode of chip + sample holder → verify no box modes
   within $4$–$8$ GHz
8. **[ ] Flux bias line:** Simulate mutual $M$ to SQUID loop → verify $M < 0.5$ pH

### 5.4 Expected Simulation Outputs

| Output | Format | Purpose |
|:---|:---|:---|
| $C_\Sigma$ per device | CSV table | Verifies capacitor geometry achieves target $E_C$ |
| $\omega_{01}$, $\omega_{12}$ per device | CSV table | Cross-check against analytic Koch theory |
| $g$ per qubit-resonator pair | CSV table | Verifies dispersive regime condition |
| Cross-talk matrix $M_{ij}$ | $8 \times 8$ CSV | Identifies problematic pairs needing layout revision |
| S-parameter sweep | Touchstone (.sNp) | Full RF characterization of feedline |

---

## 6. Mask Layout Specifications

### 6.1 Chip Architecture

**Chip size:** $5 \times 5$ mm² (standard for 8-qubit cQED chips)
**Substrate:** C-plane sapphire, $430\ \mu$m thick, double-side polished
**Qubit count:** 8 transmons + 8 readout resonators

### 6.2 Layout Floorplan

```
┌─────────────────────────────────────────────────┐
│  ┌─────┐    ┌─────┐    ┌─────┐    ┌─────┐       │
│  │A-050│    │A-100│    │A-350│    │A-750│       │
│  └──┬──┘    └──┬──┘    └──┬──┘    └──┬──┘       │
│     │          │          │          │          │
│  ┌──┴──────────┴──────────┴──────────┴──┐       │
│  │         COMMON FEEDLINE              │       │
│  └──┬──────────┬──────────┬──────────┬──┘       │
│     │          │          │          │          │
│  ┌──┴──┐    ┌──┴──┐    ┌──┴──┐    ┌──┴──┐       │
│  │A-100│    │A-200│    │A-500│    │A-1500│      │
│  └─────┘    └─────┘    └─────┘    └──────┘       │
│                                                  │
│  [LAUNCH]──────────FEEDLINE──────────[LAUNCH]    │
└─────────────────────────────────────────────────┘
```

- 8 qubits in 2 rows × 4 columns, spaced $600\ \mu$m center-to-center
- Single CPW feedline running between rows with capacitive coupling taps
- Each qubit couples to its own $\lambda/4$ readout resonator
- Resonator frequencies staggered: $6.5, 6.6, 6.7, 6.8, 6.9, 7.0, 7.1, 7.2$ GHz
- Individual flux-bias lines (Z-control) for each qubit (SQUID tuning)
- Individual XY-drive lines with $20$ dB attenuation per line
- Bond pad array at chip edges for wire-bonding to PCB

### 6.3 GDSII Layer Table

| Layer | GDS Number | Purpose | Notes |
|:---|:---:|:---|:---|
| **Junction bottom** | 1 | Al bottom electrode (first evaporation) | $30$ nm Al, $0\degree$ angle |
| **Junction top** | 2 | Al top electrode (second evaporation) | $50$ nm Al, $+29\degree$ angle |
| **IDC + resonator** | 3 | IDC fingers, CPW resonator, ground plane | $80$ nm Al |
| **Feedline** | 4 | Common CPW feedline | $80$ nm Al, $50\ \Omega$ impedance |
| **Flux bias** | 5 | On-chip flux-bias lines (DC–100 MHz) | $80$ nm Al, low-pass filtered |
| **XY drive** | 6 | Capacitively coupled drive lines | $80$ nm Al |
| **Bond pads** | 7 | Wire-bond pads ($100 \times 100\ \mu$m²) | Al + Au flash (optional) |
| **Alignment marks** | 8 | E-beam alignment crosses | $5\ \mu$m feature, global + local |
| **Dicing marks** | 9 | Chip boundary, dicing streets | $100\ \mu$m scribe lanes |
| **Text labels** | 10 | Device IDs, orientation markers | Human-readable verification |

### 6.4 Critical Dimensions

| Feature | Min | Target | Max | Tolerance |
|:---|:---:|:---:|:---:|:---:|
| Junction overlap area | $50 \times 50$ nm | See §2.2 | $200 \times 200$ nm | $\pm 10$ nm |
| IDC finger width | $3\ \mu$m | $5\ \mu$m | $10\ \mu$m | $\pm 50$ nm |
| IDC finger gap | $3\ \mu$m | $5\ \mu$m | $10\ \mu$m | $\pm 50$ nm |
| CPW center conductor | $10\ \mu$m | $15\ \mu$m | $20\ \mu$m | $\pm 50$ nm |
| CPW gap | $5\ \mu$m | $8\ \mu$m | $12\ \mu$m | $\pm 50$ nm |
| Bond pad | $80\ \mu$m | $100\ \mu$m | $120\ \mu$m | $\pm 2\ \mu$m |
| Qubit-qubit spacing | $400\ \mu$m | $600\ \mu$m | $800\ \mu$m | $\pm 10\ \mu$m |

### 6.5 Fabrication Process Flow

| Step | Process | Tool | Parameters |
|:---|:---|:---|:---|
| 1 | Substrate clean | Solvent + O$_2$ plasma | Acetone/IPA, 5 min O$_2$ ash |
| 2 | E-beam resist coat | Spin-coater | PMMA 950K A4, 180°C bake |
| 3 | E-beam lithography (bottom electrode) | EBL tool | 100 kV, 500 $\mu$C/cm² dose |
| 4 | Develop + descum | MIBK:IPA 1:3 | 60 s develop, 10 s O$_2$ descum |
| 5 | 1st Al evaporation | E-beam evaporator | $30$ nm Al, $0\degree$, $5\times 10^{-7}$ mbar |
| 6 | **Oxidation** (static) | Load-lock | $P_{\text{O}_2}$, $t_{\text{ox}}$ per §2.2 |
| 7 | 2nd Al evaporation | E-beam evaporator | $50$ nm Al, $+29\degree$, $5\times 10^{-7}$ mbar |
| 8 | Lift-off | Acetone soak | $60\degree$C, 2 hr |
| 9 | Photoresist coat (IDC/resonator) | Spin-coater | S1813 or LOR/AZ bilayer |
| 10 | Photolithography (IDC + resonator + feedline) | Mask aligner | 365 nm UV, hard contact |
| 11 | Develop | MF-319 | 60 s |
| 12 | Al deposition (thick) | E-beam evaporator | $80$ nm Al |
| 13 | Lift-off | Remover PG | $80\degree$C, 1 hr |
| 14 | Dicing | Dicing saw | $100\ \mu$m blade, $50\ \mu$m depth |
| 15 | Wire bonding | Wedge bonder | $25\ \mu$m Al wire, ultrasonic |
| 16 | Room-temperature screening | Probe station | $R_n$ measurement (§2.3) |

### 6.6 Test Structures (on-chip)

Include on the same $5 \times 5$ mm² chip:

| Structure | Count | Purpose |
|:---|:---:|:---|
| Single junction (bare) | 4 | Measure $I_c$, $R_n$ directly ($R_n$ test) |
| IDC-only test structures | 4 | Measure $C_\Sigma$ at room temperature |
| CPW resonator (no qubit) | 2 | Characterize internal $Q_i$ of fabrication |
| Through-line (no devices) | 2 | Calibrate feed line insertion loss |
| Daisy-chain via test | 2 | Verify galvanic contacts |

---

## 7. Design Trade-offs and Risk Mitigation

### 7.1 Competing Design Constraints

| Constraint | Drive direction | Affected devices | Mitigation |
|:---|:---|:---|:---|
| Large $E_J$ → large junction | Increase $I_c$, increase area | A-1000, A-1500 | Use higher $J_c$ (2–5 kA/cm²) |
| Small $E_C$ → large $C_\Sigma$ | Increase capacitor area | A-1000, A-1500 | Parallel-plate capacitor; accept larger footprint |
| Small $\vert\alpha\vert$ → spectral crowding | $\omega_{12} \approx \omega_{01}$ | A-500+ | Narrowband filtering; Ramsey for precision |
| Junction aging ($I_c$ drift) | $I_c$ increases 5–20% over months | All | Characterize $I_c$ at screening + before each cooldown |
| TLS loss in large capacitors | $T_1$ degradation | A-750+ | IDC (metal-on-sapphire) preferred over deposited dielectric |

### 7.2 J_c Tunability as Design Freedom

The junction oxidation parameters provide $\pm 5\times$ tunability in $J_c$,
enabling:
- **Larger junctions for yield:** Use $J_c = 0.5$ kA/cm² (heavier oxidation)
  for A-050 through A-350 → junction area increases $2\times$
- **Smaller junctions for high $E_J$:** Use $J_c = 2.0$–$5.0$ kA/cm² (lighter
  oxidation) for A-500 through A-1500 → maintains manageable junction area
- **Multiple $J_c$ on one chip:** Possible by varying dose during e-beam write
  or using localized oxidation (O$_2$ plasma through shadow mask). Simpler:
  use two separate oxidation steps for two chip halves.

### 7.3 Fabrication Yield Strategy

| Yield risk | Likelihood | Mitigation |
|:---|:---:|:---|
| Junction short | 5–10% per junction | Redundant devices (3 per design); screen by $R_n$ |
| Junction open (lift-off failure) | 2–5% | Redundant devices |
| IDC short (metal bridge) | 1–2% | Optical inspection; redundant devices |
| Resonator frequency off-target | 10–20% | Tune with flux bias (SQUID frequency adjustment) |

**Target:** $\geq 6$ of 8 device designs measured successfully. With 3 copies per
design ($24$ qubits total on chip) and $80$% individual junction yield, expected
completed designs: $8 \times (1 - (1 - 0.8)^3) \approx 8 \times 0.992 = 7.9$.

---

## 8. Deliverables Checklist

| WBS | Deliverable | Status |
|:---|:---|:---:|
| 1.1 | 8-device parameter set (this document §1) | ✅ |
| 1.2 | Junction geometries and $J_c$ options (§2) | ✅ |
| 1.3 | Capacitor geometries (IDC + parallel-plate options) (§3) | ✅ |
| 1.4 | EM simulation specifications (§5) | ✅ |
| 1.5 | Mask layout specs, GDSII layer table, process flow (§6) | ✅ |
| — | Readout resonator design (§4) | ✅ |
| — | Risk register and trade-off analysis (§7) | ✅ |

**Next Phase:** Phase 2 — Fabrication partner identification, first fabrication run.

---

## 9. References

1. Koch, J., et al. "Charge-insensitive qubit design derived from the Cooper pair box."
   *Physical Review A* **76**, 042319 (2007).
2. Krantz, P., et al. "A quantum engineer's guide to superconducting qubits."
   *Applied Physics Reviews* **6**, 021318 (2019).
3. Blais, A., et al. "Circuit quantum electrodynamics."
   *Reviews of Modern Physics* **93**, 025005 (2021).
4. Wang, Z., et al. "Systematic study of high $E_J/E_C$ transmon qudits up to $d = 12$."
   *Physical Review Applied* **23**, 034046 (2025).
5. Quni-Gudzinas, R.B. "The Harmonic Paradigm V4.0." Zenodo, DOI: 10.5281/zenodo.21505993 (2026).
6. Simons, R.N. "Coplanar Waveguide Circuits, Components, and Systems." Wiley (2001). — IDC design formulas.

---

*Document version 1.0 — 2026-07-23*
*Next action: Phase 2 Fabrication — partner identification + first fabrication run*
