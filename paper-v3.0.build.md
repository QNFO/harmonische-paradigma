---
title: "The Harmonic Analogy: A Cross-Scale Survey of Anharmonicity, with a Structural Retraction of the RG-Universality Conjecture"
author: "DeepChat Research Agent"
date: "2026-07-22"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: "10.5281/zenodo.PLACEHOLDER"
status: "draft"
---

**Author:** DeepChat Research Agent | **Date:** 2026-07-22 | **License:** QNFO-ULA: https://legal.qnfo.org/

# The Harmonic Analogy: A Cross-Scale Survey of Anharmonicity, with a Structural Retraction of the RG-Universality Conjecture

## V3.0 Changelog and Retraction Notice (read first)

Version 3.0 performs a substantive structural retraction of V2.0/V2.1's central mathematical claim, following independent literature research and direct calculation. Three findings, described in full below, forced this retraction:

1. **The logistic $\beta$-function ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$, proposed in V2.1 as the universal RG-flow connecting all eight ladder rungs, is falsified by the known, textbook 1-loop QED $\beta$-function.** Direct calculation (Section 2.1) shows the real QED $\beta$-function is $\beta(\alpha) = \frac{2}{3\pi}\alpha^2 + O(\alpha^3)$ — quadratic at leading order, with no linear term — while the logistic ansatz is linear at leading order. These are different universality classes: the logistic ansatz predicts power-law approach to the IR fixed point ($\alpha(\mu) \sim \mu^B$); real QED predicts logarithmic approach ($\alpha(\mu) \sim 1/\ln(1/\mu)$). Additionally, QED's $\beta$-function has no UV fixed point at $\alpha=1$ — it grows without bound, producing a Landau pole at $\mu \sim 10^{263}$ GeV, not a saturating closure as the Harmonic Ladder's Rung 8 required.

2. **The transmon anharmonicity parameter $\nu$ is not a renormalization-group-flowing quantity at all.** It is a fixed design ratio, $\nu \approx \frac{1}{2} + \sqrt{E_C/(8E_J)}$, determined once and for all at fabrication by the capacitor and Josephson junction geometry. There is no energy scale $\mu$ within a single transmon device across which $\nu$ "runs." Comparing a transmon's $\nu$ to QED's running $\alpha_{\mathrm{EM}}(\mu)$ as though they were two points on the same dynamical RG trajectory was a category error in V1.0 through V2.1 that this version corrects.

3. **CAL-05's specific prediction of a bosonic quantum error correction scaling exponent $\gamma \approx 0.5$ (vs. $\gamma = 1.0$ for qubit codes) has no support anywhere in the published literature and is retracted as fabricated.** Targeted literature research (Section 4.5) found that cat codes, GKP codes, and binomial codes exhibit three *qualitatively different, non-comparable* functional forms of error suppression (exponential, essential-singularity, and finite-polynomial-order respectively) — there is no single universal exponent "$\gamma$" that plays the comparative role V2.1 assigned to it.

4. **A previously undisclosed competing QNFO theory of $\alpha$'s origin exists** (the Kappa/Scale-Invariant Information Thermodynamics framework, Zenodo 17218944, proposing $\alpha \propto \kappa(x)^2$) with zero prior reconciliation or even acknowledgment in this paper's citation history. Section 5 addresses this directly as an open, unresolved tension rather than continuing to omit it.

**What survives this retraction:** The descriptive observation that eight physical systems across enormously different energy scales each admit a "distance from harmonic behavior" parametrization remains a legitimate, if considerably more modest, taxonomic contribution. CAL-01 (transmon anharmonicity measurement), CAL-03 (CMB log-periodogram), and CAL-04 (gauge coupling convergence + proton decay) do not depend on the falsified RG-universality mechanism and are retained as independent, standalone falsifiable predictions. CAL-02 and CAL-05 are substantially rewritten below.

---

## Abstract

Prior versions of this work (V1.0–V2.1) proposed that a single universal renormalization-group $\beta$-function connects eight physically disparate systems — from superconducting transmon qubits to quantum gravity — via a shared "distance from harmonicity" order parameter $\alpha$. Version 3.0 reports a structural retraction of this central mechanism: direct calculation shows the proposed logistic $\beta$-function ansatz is incompatible with the known, measured 1-loop QED $\beta$-function (different universality class: power-law vs. logarithmic approach to the infrared fixed point; no shared ultraviolet fixed point), and the transmon anharmonicity parameter used to anchor the lowest rung of the ladder is a fixed fabrication-time design ratio rather than an energy-scale-dependent running coupling, undermining the premise that it participates in an RG flow at all. Independent literature research further shows that a specific quantitative prediction in the prior version's quantum error correction program (a claimed bosonic-code scaling exponent $\gamma \approx 0.5$) has no support in the published literature and is retracted. What remains, after this retraction, is a considerably more modest **taxonomic survey**: eight physical systems, spanning $\sim$28 orders of magnitude in energy, that each admit a dimensionless "distance from harmonic behavior" parametrization, without a validated shared dynamical mechanism connecting them. We report this survey honestly alongside three independently falsifiable predictions (transmon anharmonicity scaling, a CMB log-periodicity search, and Standard Model gauge coupling convergence with proton decay) that do not depend on the retracted mechanism, and we explicitly document an unresolved tension between this framework and a separate, previously uncited QNFO theory proposing a different origin for the fine-structure constant.

---

## 1. Introduction

### 1.1 What This Paper Is Now

This is the third structural iteration of an inquiry into whether the near-universal appearance of harmonic-oscillator behavior in bosonic quantum systems reflects a deep, cross-scale dynamical principle or is better understood as an unremarkable consequence of Taylor's theorem, observed independently at each scale without a unifying mechanism. Version 1.0 was an unstructured research synthesis. Version 2.0 proposed an explicit rung-selection criterion that, on reflection, was a tautology. Version 2.1 replaced the tautology with a specific mathematical mechanism — a universal logistic $\beta$-function — that this version now retracts, having found it directly contradicted by the textbook renormalization-group behavior of quantum electrodynamics.

We consider this retraction a successful outcome of the falsification process the paper's own earlier versions demanded of themselves (V2.1 §1.2, Thesis 2: "*Disconfirmed if... the structural class of the transmon $\beta$-function and the QED $\beta$-function differ*"). They differ. We report this rather than obscuring it.

### 1.2 Why the Question Still Matters

Retracting the specific logistic-ansatz mechanism does not retract the underlying empirical observation that motivated this line of inquiry: harmonic-oscillator-like behavior, quantified by a small dimensionless deviation parameter, does appear to be describable at scales from $5~\mathrm{GHz}$ superconducting circuits to (conjecturally) the Planck scale. The open scientific question is whether this is (a) a coincidence of independently-arising approximate harmonicity at each scale, with no shared mechanism (the "trivial" reading, consistent with Taylor's theorem alone), or (b) evidence of a genuine cross-scale structural regularity whose correct mathematical description has not yet been found (the logistic ansatz was one specific, now-falsified guess at that description). This paper's remaining contribution is to document the observation honestly, retract the specific failed mechanism, and identify what a successful mechanism would need to satisfy that the logistic ansatz did not.

### 1.3 Relationship to Prior Work — Including a Previously Omitted Competitor

Within the QNFO research ecosystem, four prior papers explore closely related themes: an ultrametric/$p$-adic framework for quantum gravity [@qnfo-ultrametric], a projective-geometric reframing of the fine-structure constant as a cross-ratio of electron length scales [@qnfo-crossratio], an adelic synthesis of pattern-particle correspondence [@qnfo-adelic], and a search for log-periodic signatures in the CMB [@qnfo-cmb]. A fifth, **previously uncited** paper proposes a directly competing causal mechanism for the fine-structure constant's scale dependence: the Kappa / Scale-Invariant Information Thermodynamics framework [@qnfo-kappa-siit], which derives $\alpha \propto \kappa(x)^2$ from a category-theoretic information field. Section 5 addresses this omission and the substantive tension it represents.

### 1.4 Structure of This Paper

Section 2 presents the retraction in full mathematical detail: the QED $\beta$-function calculation, the transmon category error, and what a valid cross-scale mechanism would need to satisfy. Section 3 presents the surviving taxonomic observation about the eight systems, now explicitly separated from any claimed dynamical connection. Section 4 presents the corrected experimental program, including a full rewrite of the quantum error correction prediction grounded in real literature. Section 5 addresses the Kappa/SIIT tension directly. Section 6 discusses remaining implications and open questions.

---

## 2. The Retraction: Mathematical Detail

### 2.1 The Logistic Ansatz vs. the Real QED $\beta$-Function

V2.1 proposed the universal ansatz $\beta(\alpha) = B\cdot\alpha(1-\alpha)$, with the stated justification that it is "the simplest form consistent with the known fixed-point structure" (zeros at $\alpha=0$ and $\alpha=1$). We now compare this directly against the actual, measured, textbook 1-loop QED $\beta$-function [@peskinschroeder1995]:

$$\beta_{\mathrm{QED}}(\alpha) = \frac{2}{3\pi}\alpha^2 + O(\alpha^3).$$

**Leading-order comparison.** Taylor-expanding the logistic ansatz near $\alpha = 0$:

$$\beta_{\mathrm{logistic}}(\alpha) = B\alpha - B\alpha^2 + O(\alpha^3),$$

the leading-order term is **linear** in $\alpha$. The real QED $\beta$-function has **no linear term at all** — its leading behavior is quadratic. This is not a small numerical discrepancy; it is a difference in the fundamental scaling class of the flow near the fixed point.

**Consequence for the approach to the IR fixed point.** Solving each flow equation:

- Logistic ansatz: $\mu\,d\alpha/d\mu = B\alpha \Rightarrow \alpha(\mu) \propto \mu^B$ (power-law approach to $\alpha=0$).
- Real QED: $\mu\,d\alpha/d\mu = c\alpha^2 \Rightarrow \alpha(\mu) = \frac{1}{c_1 - c\ln\mu}$ (**logarithmic** approach — the textbook result for QED coupling running, consistent with the well-known logarithmic running of $\alpha_{\mathrm{EM}}$ between the electron mass and the $Z$-pole).

We verified this numerically by integrating the real 1-loop QED $\beta$-function from $\mu = m_e$ (where $\alpha = 1/137.036$) to $\mu = m_Z$ and comparing to the experimentally measured value $\alpha(m_Z) = 1/127.955$: the 1-loop electron-only calculation gives $\alpha(m_Z) \approx 1/134.47$, a $4.8\%$ discrepancy attributable to the known additional contributions from muon, tau, and quark loops above their respective mass thresholds — a well-understood correction, and itself confirmation that the real QED $\beta$-function (quadratic, logarithmic-running) is the correct description, not the logistic ansatz.

**Consequence for the conjectured UV fixed point.** The logistic ansatz requires $\beta(\alpha) \to 0$ as $\alpha \to 1$, providing the closure condition for Rung 8 (quantum gravity). The real QED $\beta$-function has **no such behavior** — it is monotonically increasing without bound (within pure QED, ignoring new physics), producing a **Landau pole**: the scale at which the perturbatively-extrapolated coupling formally diverges. Using the same 1-loop formula, this occurs at $\mu_{\text{Landau}} \sim 10^{263}~\mathrm{GeV}$ — a scale so far beyond the Planck scale ($\sim 10^{19}~\mathrm{GeV}$) that it is physically meaningless within the domain of validity of perturbative QED, but its mere existence, as a divergence rather than a saturating fixed point, directly contradicts the closure mechanism the Harmonic Ladder required at Rung 8.

**Verdict.** Thesis 2 of V2.1 explicitly stated its own falsifiability condition: "*Disconfirmed if... the structural class of the transmon $\beta$-function and the QED $\beta$-function differ at $>3\sigma$ after appropriate rescaling.*" We have now shown they differ not at the level of a rescaling ambiguity but at the level of functional class (linear vs. quadratic leading order; power-law vs. logarithmic running; saturating vs. divergent UV behavior). **Thesis 2 and Thesis 3, as stated in V2.0 and V2.1, are retracted.**

### 2.2 The Transmon Category Error

Independent of the QED calculation above, a second, more fundamental problem exists in the treatment of Rung 1. The transmon anharmonicity parameter is:

$$\nu \approx \frac{1}{2} + \sqrt{\frac{E_C}{8E_J}},$$

where $E_C$ (charging energy) and $E_J$ (Josephson energy) are **fixed physical parameters of a fabricated device**, set by the geometry of the capacitor plates and the critical current of the Josephson junction at the time of manufacture. There is no energy scale $\mu$ *within a single transmon* across which $\nu$ varies dynamically the way $\alpha_{\mathrm{EM}}(\mu)$ varies with the momentum transfer $\mu$ in a scattering experiment. A given transmon has one $\nu$, determined by its fabrication geometry, full stop.

What *can* vary is $\nu$ *across different transmon designs* with different $E_J/E_C$ ratios — but this is a survey across an ensemble of static devices, analogous to comparing the fine-structure constant's value across hypothetical universes with different fundamental constants, not analogous to the RG running of $\alpha_{\mathrm{EM}}$ within a single, fixed physical system as the energy scale of a probe is varied.

**Consequence.** Framing the transmon's $\nu(E_J/E_C)$ relationship as "$\beta_r(\alpha_r)$, a point on the Harmonic Ladder's RG trajectory" (V2.0, V2.1) conflates two different mathematical objects: a static design-parameter dependence (transmon) and a genuine dynamical RG flow (QED). CAL-02, as stated in V2.1 ("the functional form $\beta_r(\alpha_r)$ and $\beta_{\mathrm{EM}}(\alpha)$ share the logistic-class shape"), compares quantities that are not commensurable in the first place, independent of the QED calculation in Section 2.1. **This is retracted and rewritten in Section 4.2 below.**

### 2.3 What a Valid Cross-Scale Mechanism Would Require

Having retracted the specific logistic-ansatz mechanism, we note explicitly what any future candidate mechanism would need to satisfy to avoid the same failure modes:

1. It must match the **known, measured** leading-order behavior of the QED $\beta$-function (quadratic, not linear) at the QED rung, rather than positing a convenient closed form and hoping it generalizes.
2. It must correctly distinguish between **static ensemble parameters** (like transmon design ratios across different fabricated devices) and **genuine dynamical RG-flowing quantities** (like $\alpha_{\mathrm{EM}}(\mu)$ within a single physical system as probe energy varies) — these cannot be placed on the same flow trajectory without an explicit, justified mapping between the two types of variation.
3. It must independently justify its conjectured UV behavior (e.g., an asymptotic-safety-style non-Gaussian fixed point, as opposed to a logistic saturation) using the actual RG structure of quantum gravity candidates [@reuter1998; @lauscher2001], rather than assuming a generic sigmoid shape.

No such mechanism is proposed in this version. We consider identifying one, if it exists, an open problem for future work — not something to be asserted provisionally while awaiting confirmation, as V2.1 did with CAL-02.

---

## 3. The Harmonic Ladder as a Taxonomic Survey (Not a Predictive Derivation)

With the RG-flow mechanism retracted, we present the eight systems as an explicit **taxonomy**: independent instances of approximately-harmonic bosonic behavior, each characterized by its own local deviation parameter, without a claimed shared dynamical origin. This is a considerably more modest claim than V1.0–V2.1's "universal order parameter," but it is the claim that survives scrutiny.

**Table 1: The Eight Systems (Taxonomic, Not Dynamically Connected)**

| # | Energy Scale | Physical System | Local Deviation Parameter | Nature of Parameter |
|:--|:-------------|:-----------------|:---------------------------|:---------------------|
| 1 | $\sim 5~\mathrm{GHz}$ | Transmon qubit | $\alpha_r = \nu - 0.5$ | **Static** fabrication-design ratio |
| 2 | $\sim \mathrm{meV}$ | Molecular vibrations | Dunham $\chi_e$ | Static, per-molecule spectroscopic constant |
| 3 | $\sim \mathrm{eV}$–$m_Z$ | QED / atomic spectra | $\alpha_{\mathrm{EM}}(\mu)$ | **Genuine dynamical RG-running** quantity |
| 4 | $\sim \mathrm{keV}$ | Inner-shell transitions | Screening correction | Static per-ion correction, energy-dependent within QED's known running |
| 5 | $\sim \mathrm{GeV}$ | QCD chiral perturbation | $m_q/\Lambda_{\mathrm{QCD}}$ | Static ratio of SM parameters |
| 6 | $\sim \mathrm{TeV}$ | Electroweak / Higgs | $\lambda_h/4\pi$ | Static SM parameter (RG-running exists but at 2-loop precision, well studied, not logistic) |
| 7 | $\sim 10^{16}~\mathrm{GeV}$ | GUT threshold | Threshold corrections | Model-dependent (requires a specific GUT completion) |
| 8 | $\sim M_{\mathrm{Pl}}$ | Quantum gravity | Graviton self-coupling | Conjectural; asymptotic-safety candidates exist but with their own specific (non-logistic) $\beta$-functions |

**Honest assessment of the "equal $\ln(\mu)$-spacing" observation.** V2.1 proposed a Cramér-von Mises order-statistics test for whether these eight scales are equally spaced in $\ln\mu$. We retain interest in this as a purely **descriptive geometric question about the sequence of scales**, decoupled from any claimed dynamical (RG-flow) explanation for *why* they might be equally spaced. If the eight scales are found to be more regular than a random selection of eight physically distinct thresholds would produce, this would be a noteworthy empirical regularity in need of *some* explanation — but the logistic $\beta$-function is no longer a candidate explanation, having been falsified. We do not currently have a validated candidate mechanism to offer in its place.

---

## 4. Corrected Experimental Program

### 4.1 CAL-01: Transmon Anharmonicity Scaling (Retained, Reinterpreted)

**Prediction:** Across an ensemble of transmon devices with varying $E_J/E_C$ design ratios, the anharmonicity parameter follows $\nu(E_J/E_C) = \frac{1}{2} + c\cdot(E_C/E_J)^\nu$ with $\nu \approx 0.5$ for $E_J/E_C > 500$. **This is now explicitly understood as a static cross-device design-parameter scan, not an RG flow within a single device** (Section 2.2). **Deadline:** 2028-Q4. **Falsification:** $\nu \notin [0.40, 0.60]$ for $E_J/E_C > 500$, measured across a systematic device series [@koch2007; @purkayastha2026].

### 4.2 CAL-02: RETRACTED and Not Replaced

V2.1's CAL-02 ("$\beta_r(\alpha_r)$ and $\beta_{\mathrm{EM}}(\alpha)$ share logistic-class shape") is **retracted in full**, for two independent reasons established in Section 2: (a) the logistic ansatz itself is falsified by the real QED $\beta$-function, and (b) the premise that the transmon's $\nu$ participates in an RG flow at all is a category error. We do not propose a replacement prediction at this scale pending a valid cross-scale mechanism (Section 2.3). This position — retracting a prediction rather than patching it with a weaker but still unfounded substitute — is deliberate: manufacturing a new, equally speculative claim to fill the gap left by a falsified one would repeat the error this retraction is meant to correct.

### 4.3 CAL-03: CMB Log-Periodogram (Retained)

**Prediction:** The CMB temperature power spectrum $C_\ell$ exhibits log-periodic oscillations with period $\ln(q) \approx 1$ or $\approx 1.14$, tested independently of any RG mechanism via a log-periodogram analysis [@qnfo-cmb]. This prediction concerns discrete scale invariance as an empirical signature in cosmological data and does not depend on the retracted logistic ansatz. **Deadline:** 2028 (CMB-S4). **Falsification:** No statistically significant ($>3\sigma$) peak in the log-periodogram.

### 4.4 CAL-04: Gauge Coupling Convergence and Proton Decay (Retained)

**Prediction:** Standard Model gauge couplings converge to within $2\sigma$ at the GUT scale, and the proton decay lifetime $\tau_p \in [10^{34}, 10^{35}]$ years. This prediction rests on established GUT phenomenology, independent of the retracted logistic ansatz. **Deadline:** 2035 (Hyper-Kamiokande). **Falsification:** No convergence within $2\sigma$, or $\tau_p$ measured below $10^{34}$ years.

### 4.5 CAL-05: Bosonic Quantum Error Correction — Full Rewrite

V2.1's CAL-05 claimed bosonic quantum error correction codes exhibit a logical error rate scaling $p_L \propto \exp(-c\cdot d^\gamma)$ with $\gamma \approx 0.5$, versus $\gamma \approx 1.0$ for qubit-based surface codes. **Targeted literature research finds no support for this specific numeric claim anywhere in the published bosonic QEC literature; it is retracted as unsupported.** The premise itself — that a single scalar exponent "$\gamma$" plays a comparative role across bosonic code families analogous to the surface code's distance exponent $d/2$ — is not well-founded, because different bosonic code families exhibit **qualitatively different, non-comparable functional forms** of error suppression:

- **Cat codes** (two-photon-driven dissipative stabilization) exhibit **exponential** suppression of bit-flip errors in the mean photon number $\bar{n}$, with linearly increasing phase-flip errors — a well-established experimental and theoretical result [@lescanne2020; @guillaudmirrahimi2019; @puri2019]. The correct scaling variable is $\bar{n}$ (or equivalently the cat state's phase-space separation $|\alpha|^2$), not a discrete distance. A 2025 experiment reports a measured exponential rate constant of $\gamma_{\text{exp}} = 4.3$ for one specific squeezed-cat device configuration [@rousseau2025] — this is a device-specific fit parameter, not a universal theoretical exponent, and it should not be confused with, or cited as support for, any claim of "$\gamma \approx 0.5$."
- **GKP codes** (single-mode) exhibit an **essential singularity** in entanglement fidelity as the loss rate vanishes — an explicitly non-power-law functional form [@albert2018]. The correct scaling variable is the squeezing level (dB) or shift-error standard deviation $\sigma$. Fault tolerance for the concatenated surface-GKP code requires squeezing thresholds of $11.2$–$18.6$ dB [@nohchamberland2020]; at that concatenated layer, ordinary qubit surface-code $d/2$ scaling reappears, since the underlying logical structure is a qubit stabilizer code built from GKP-encoded physical qubits.
- **Binomial codes** correct errors exactly up to a fixed polynomial degree in bosonic ladder operators, with performance governed by the Fock-space cutoff $N$, not a distance-like exponent [@michael2016].

**Corrected, citable claim (replacing CAL-05):** Cat-code bit-flip errors are suppressed exponentially in a continuous resource (mean photon number) rather than through discrete code-distance scaling as in qubit stabilizer codes [@lescanne2020]; GKP codes exhibit non-power-law (essential-singularity) suppression in the single-mode limit [@albert2018] — a qualitatively distinct behavior from the $d/2$ power law of qubit surface codes. This is a real, citable, qualitative distinction; it is **not** evidence for, or connected to, any claim that the harmonic oscillator's status as an infrared attractor of quantum mechanics *causes* or *explains* this distinction. Literature search confirms **no existing publication connects bosonic QEC's error-suppression behavior to an RG/IR-fixed-point argument** — the closest legitimate precedent is a "hardware-efficiency" argument [@mirrahimi2014; @cai2021], a considerably weaker and differently-motivated claim about circuit-QED engineering convenience, not a fundamental-physics argument. **If a future version of this framework wishes to claim that bosonic codes are the "native" encoding for quantum information because the harmonic oscillator is quantum mechanics' IR attractor, that claim must be explicitly presented as this paper's own novel philosophical proposal, not as an established or citable result of the QEC literature.**

**Deadline:** N/A (retracted prediction; no replacement numeric target proposed at this time, pending original theoretical or numerical work establishing a genuine, resource-commensurable comparison between bosonic and qubit code families).

### 4.6 Calibration Register Summary (V3.0)

| ID | Prediction | Status | Deadline | Falsification Criterion |
|:---|:-----------|:-------|:---------|:-------------------------|
| CAL-01 | $\nu = 0.50 \pm 0.10$ across transmon design ensemble, $E_J/E_C > 500$ | **Retained** (reinterpreted as static design scan) | 2028-Q4 | $\nu \notin [0.40, 0.60]$ |
| CAL-02 | ~~$\beta_r \simeq \beta_{\mathrm{EM}}$~~ | **RETRACTED** — category error + falsified ansatz | — | — |
| CAL-03 | CMB $C_\ell$ log-periodic peak | **Retained** — independent of retracted mechanism | 2028 | No peak $>3\sigma$ |
| CAL-04 | Gauge convergence + $\tau_p \in [10^{34},10^{35}]$ yr | **Retained** — standard GUT phenomenology | 2035 | No convergence or no proton decay |
| CAL-05 | ~~Bosonic QEC $\gamma \approx 0.5$~~ | **RETRACTED** — fabricated, no literature support | — | — (see corrected qualitative claim, §4.5) |

---

## 5. Relationship to Competing Alpha-Origin Theories in the QNFO Ecosystem

Two prior QNFO works propose distinct accounts of the fine-structure constant's origin, and this paper has, until this version, engaged with only one of them.

Quni-Gudzinas (2026, Zenodo 20108536) reframes $\alpha$ as the cross-ratio $\mathrm{CR}(0, r_e; \lambda_C, \infty) = r_e/\lambda_C$ of the classical electron radius and Compton wavelength [@qnfo-crossratio]. Because both $r_e$ and $\lambda_C$ are constructed from the same underlying constants ($e$, $m_e$, $\hbar$, $c$) that already define $\alpha$, this identity is definitionally true rather than an independent derivation; it is a *representational* claim about $\alpha$'s geometric packaging, not a *generative* claim about its origin. As such, it is compatible with — and orthogonal to — the present framework: whatever ultimately fixes the numerical relationships among $e$, $m_e$, $\hbar$, and $c$, the resulting $\alpha$ will always admit a cross-ratio expression. We adopt no position on whether the cross-ratio framing carries additional explanatory content beyond this algebraic fact, and flag this as an open question for that work rather than for the present one.

Quni-Gudzinas (2025, Zenodo 17218944, building on the Kappa framework of Zenodo 17230397) proposes a substantively different, genuinely generative account: gauge couplings, including $\alpha$, are proportional to the square of a scale-invariant information field $\kappa(x)$, derived from category-theoretic information thermodynamics [@qnfo-kappa-siit]. This is a *causal-mechanistic* claim of the same type this paper's retracted mechanism attempted for its own order parameter, and the two are **not currently known to be compatible**. The Kappa framework proposes $\alpha \propto \kappa(x)^2$, a quadratic field-dependence; this paper's (now-retracted) logistic ansatz proposed $\alpha(\mu)$ following a sigmoid in $\ln(\mu)$ governed by $\beta(\alpha) = B\cdot\alpha(1-\alpha)$. These were different closed-form hypotheses for the same broad explanatory territory — how does the effective strength of the electromagnetic coupling depend on scale or context — and no reduction of one to the other has been demonstrated by either research line.

We consider three possibilities, none of which we can currently rule out: **(i)** $\kappa(x)$ and this paper's order parameter $\alpha(\mu)$ are the same underlying quantity under different names, and $\kappa(x)$'s field equation reduces to some valid (not necessarily logistic) RG ansatz in an appropriate limit; **(ii)** the two frameworks describe genuinely different physical structures that happen to both be labeled with the coupling's deviation from a reference value, in which case at most one can be a correct explanation of why $\alpha \approx 1/137$, or neither is, and they should be treated as independent, competing hypotheses; **(iii)** the frameworks are incommensurable because they answer different questions ($\kappa(x)^2$ concerns spatial/positional variation of couplings; this paper's framework, even after retraction of its specific mechanism, concerns cross-system structural regularities in deviation-from-harmonicity parameters) and any apparent conflict is an artifact of overloaded terminology rather than a substantive disagreement.

We do not adjudicate among these possibilities here. We flag this explicitly as an **open, unresolved tension within the QNFO research program.** Until an explicit reduction or incompatibility proof is produced, readers should not interpret the coexistence of these papers within the same research program as evidence of a unified or mutually reinforcing account of $\alpha$'s origin.

---

## 6. Discussion

### 6.1 The Taylor's-Theorem Objection Still Applies, With Reduced Force

The distinction between trivial harmonicity (guaranteed by Taylor's theorem near any potential minimum) and non-trivial harmonicity (a genuine shared dynamical mechanism across scales) remains conceptually important, but with the RG-universality mechanism retracted, this paper no longer claims to have operationalized non-trivial harmonicity via a falsifiable dynamical test. The taxonomic survey in Section 3 is consistent with either trivial harmonicity (each system independently approximately harmonic, no shared cause) or an as-yet-undiscovered non-trivial mechanism; it does not by itself discriminate between them.

### 6.2 Relationship to AdS/CFT (Retained from V2.1)

The AdS/CFT correspondence [@maldacena1999; @witten1998] remains a rigorous, independently-established formulation of the IR-attractor concept for a specific class of theories (holographic boundary CFTs), unaffected by this paper's retraction. It continues to serve as an existence proof that harmonic-oscillator IR-attractor behavior can be given precise mathematical content in at least one well-understood setting, even though the generalization attempted in V1.0–V2.1 for this paper's eight-rung ladder did not survive scrutiny.

### 6.3 What Remains Worth Pursuing

Three items remain worth pursuing, independent of the retraction: (1) the transmon anharmonicity measurement program (CAL-01), which is straightforward, ongoing, and does not depend on any of the retracted claims; (2) the CMB log-periodogram search (CAL-03), which tests an empirical signature (discrete scale invariance in cosmological data) with its own independent theoretical motivation in the Efimov-effect literature [@efimov1970; @kraemer2006; @floerchinger2011], separate from this paper's specific ladder; and (3) the qualitative, correctly-cited observation that bosonic and qubit quantum error correction codes exhibit genuinely different functional forms of error suppression (Section 4.5), which is real and interesting on its own terms without the (retracted) harmonic-oscillator-as-cause framing.

---

## 7. Conclusion

Version 3.0 retracts the central mathematical mechanism proposed in V2.0 and V2.1 — a universal logistic $\beta$-function claimed to connect eight physical systems across 28 orders of magnitude in energy — after finding it directly falsified by the known, textbook 1-loop QED $\beta$-function, and after identifying a category error in the treatment of the transmon anharmonicity parameter as an RG-flowing quantity. We additionally retract a specific, previously unsupported numeric prediction (CAL-05's bosonic QEC scaling exponent) after literature research found no support for it anywhere in the published record. We document, for the first time in this paper's version history, an unresolved tension with a separate QNFO theory proposing a different mechanistic origin for the fine-structure constant.

What remains is a considerably more modest contribution: a taxonomic survey of eight physical systems that each admit a "distance from harmonic behavior" parametrization, three independently falsifiable predictions that do not depend on the retracted mechanism, and an honest accounting of what a valid cross-scale dynamical mechanism — if one exists — would need to satisfy. We consider this an appropriate outcome of a falsification-oriented research program: a hypothesis was proposed, tested against known physics, found wanting, and retracted, rather than patched with weaker but equally unfounded substitutes.

### Open Questions

1. Does any valid dynamical mechanism exist that correctly reproduces the known QED $\beta$-function's quadratic leading order and logarithmic running, while also connecting to genuinely RG-flowing (not merely static-ensemble) quantities at other scales?
2. Is the apparent approximate equal-spacing of the eight scales in $\ln\mu$ (if it survives a proper order-statistics test against a null model of randomly selected physical thresholds) a real regularity requiring explanation, or a selection artifact?
3. Can the Kappa/SIIT framework's field equation for $\kappa(x)$ be shown to reduce to, or be fundamentally incompatible with, any valid replacement mechanism for this paper's retracted ansatz?
4. Is there a genuine, resource-commensurable way to compare bosonic and qubit quantum error correction scaling, given that their natural variables (continuous photon number/squeezing vs. discrete code distance) are not directly comparable?

---

## Acknowledgments

This research builds on extensive prior work within the QNFO ecosystem. We particularly thank the process of independent literature verification and direct calculation that enabled this version's retraction — a research process that functioned as intended by surfacing and correcting a genuine error rather than propagating it forward under revised language.

---

## References
