# PROJECT-PLAN.md — Harmonic Paradigm

**Project Slug:** `harmonische-paradigma`
**Created:** 2026-07-22
**Status:** Phase 0 (Project Initialization)
**Research Domain:** Quantum Field Theory / Renormalization Group / Harmonic Oscillator

---

## §1 Charter

### 1.1 Mission
To formalize, publish, and deploy the **Harmonic Paradigm**: a unified theoretical framework demonstrating that the harmonic oscillator is the universal infrared (IR) attractor of quantum theory, that the renormalization group (RG) is the scale-space syntax translating IR physics to the ultraviolet (UV), and that a single dimensionless order parameter **α** — the distance-from-harmonicity — unifies transmon anharmonicity, the QED fine-structure constant, GUT threshold corrections, and quantum gravity couplings across an 8-rung **Harmonic Ladder**.

### 1.2 Core Claim Lock (HARD — logically valid, falsifiable formulation)

**Claim 1 (IR Attractor):** For any quantum system perturbed from harmonicity, the low-energy effective theory flows to the harmonic oscillator as the unique IR fixed point, with the convergence rate quantified by the dimensionless parameter α = (Eₙ − nℏω)/ℏω.

**Falsifiability:** This claim would be disconfirmed if any bosonic quantum system with a stable ground state and a continuous spectrum near zero energy exhibits low-energy dynamics NOT approximable as a harmonic oscillator with residual anharmonicity parametrized by α.

**Claim 2 (RG as Scale-Space Syntax):** The renormalization group β-function is not merely a calculational technique but the structural grammar that expresses how α(rung) changes across energy scales. The β-function's zeros mark scale-invariant rungs where the harmonic paradigm is exact; its slope predicts the flow between rungs.

**Falsifiability:** This claim would be disconfirmed if (a) the QED fine-structure constant running cannot be expressed as α(rung=3) derived from an RG flow seeded at rung=2 (transmon anharmonicity), or (b) any experimentally measured β-function zero cannot be mapped to a harmonic-ladder rung.

**Claim 3 (α as Universal Order Parameter):** The single dimensionless parameter α = (E_measured − E_harmonic)/E_harmonic serves as the unifying order parameter across ALL 8 rungs of the Harmonic Ladder, with each rung corresponding to a distinct energy scale where α takes a specific, calculable value.

**Falsifiability:** Disconfirmed if any rung requires a second independent dimensionless parameter beyond α to fully characterize its deviation from exact harmonicity, or if two rungs at the same energy scale require different α values.

### 1.3 The 8-Rung Harmonic Ladder

| Rung | Energy Scale | Physical System | α Expression | Status |
|------|-------------|-----------------|--------------|--------|
| 1 | ~5 GHz | Transmon qubit | ν − 0.5 (anharmonicity) | **Measured:** ν = 0.5084 ± 0.017 |
| 2 | ~meV | Molecular vibrations | Dunham expansion coefficients | Known |
| 3 | ~eV | Atomic spectra / QED | α_fs ≈ 1/137 | Known |
| 4 | ~keV | Inner-shell transitions | Screening corrections | Known |
| 5 | ~GeV | QCD chiral perturbation | Quark-mass corrections | Partially known |
| 6 | ~TeV | Electroweak / Higgs | λ_h, yukawa corrections | Partially known |
| 7 | ~10¹⁶ GeV | GUT threshold | Threshold corrections | Predicted |
| 8 | ~M_Pl | Quantum gravity | Graviton self-interactions | Speculative |

---

## §2 Phases with Work Breakdown Structure (WBS)

### Phase 0: Project Initialization — COMPLETE
- **WBS 0.1:** Repository scaffold ✓
- **WBS 0.2:** PROJECT-PLAN.md with charter, WBS, milestones, deliverables, risks ✓
- **WBS 0.3:** Core claim locked in falsifiable terms ✓
- **WBS 0.4:** .gitignore from template ✓
- **WBS 0.5:** README.md ✓
- **WBS 0.6:** Git init, GitHub repo creation, Phase 0 closeout ✓
- **Deliverable:** Tag `v0.1-phase0`

### Phase 1: Due Diligence — COMPLETE
- **WBS 1.1:** KG cross-reference (2,154 nodes, 15 QNFO papers) ✓
- **WBS 1.2:** External literature search (Semantic Scholar, arXiv, web) ✓
- **WBS 1.3:** Gap analysis and novelty confirmation ✓
- **Deliverable:** `artifacts/due-diligence.md`

### Phase 2: Literature Search & Triage — COMPLETE
- **WBS 2.1:** Multi-source search (5 sources) ✓
- **WBS 2.2:** Deduplication and classification ✓
- **WBS 2.3:** Core paper deep reads ✓
- **Deliverable:** `artifacts/lit-review.md`

### Phase 3: Citation Management — COMPLETE
- **WBS 3.1:** Citation extraction from paper ✓
- **WBS 3.2:** BibTeX verification ✓
- **WBS 3.3:** Audit report ✓
- **Deliverable:** `references.bib`, `artifacts/citation-audit.md`

### Phase 4: Deep Research (9-Stage Bayesian Cascade) — COMPLETE
- **WBS 4.1:** Domain assessment ✓
- **WBS 4.2:** Paradigm-shift candidate identification (5 candidates) ✓
- **WBS 4.3:** Assumption audit ✓
- **WBS 4.4:** Red-team adversarial challenge (6 challenges) ✓
- **WBS 4.5:** Bayesian sensitivity analysis ✓
- **WBS 4.6:** Calibration register (5 entries) ✓
- **WBS 4.7:** Portfolio allocation ✓
- **WBS 4.8:** Strategic memo ✓
- **WBS 4.9:** Adversarial review ✓
- **Deliverable:** `artifacts/strategic-memo.md`

### Phase 5: Formal Publication — PENDING
- **WBS 5.1:** Publication Language Gate scan → clean paper.md
- **WBS 5.2:** Self-evaluation rubric → all ≥ 3, avg ≥ 4.0
- **WBS 5.3:** Unicode-LateX preprocessing → `paper.build.md`
- **WBS 5.4:** Pandoc+XeLaTeX PDF build → `paper.pdf`
- **WBS 5.5:** PDF rendering verification (`check-pdf.py`)
- **WBS 5.6:** Credential scan on paper.md
- **WBS 5.7:** Provenance bundle creation
- **WBS 5.8:** Zenodo upload + metadata + publish
- **WBS 5.9:** DOI verification (independent re-query)
- **Deliverable:** `harmonische-paradigma-research-synthesis.pdf`, Zenodo DOI, `PROVENANCE-BUNDLE.zip`

### Phase 6: D1 Deployment — PENDING
- **WBS 6.1:** Cloudflare account/discovery
- **WBS 6.2:** D1 living-paper check-then-write
- **WBS 6.3:** Papers-server Worker verification
- **Deliverable:** D1 living-paper row, HTTP 200 from papers.qnfo.org

### Phase 7: Dissemination — PENDING
- **WBS 7.1:** Papers-server URL HTTP 200 verification
- **WBS 7.2:** SEO audit (robots.txt, sitemap, meta tags, Schema.org)
- **WBS 7.3:** Buffer social media posting (Twitter, LinkedIn, Bluesky)
- **Deliverable:** Verified social posts in Buffer queue

### Phase 8: Core Distribution — PENDING
- **WBS 8.1:** GitHub push + tag + release with DOI link
- **WBS 8.2:** R2 archive sync (paper.md, paper.pdf, provenance bundle)
- **WBS 8.3:** Knowledge Graph seed (Paper node + BELONGS_TO edges)
- **WBS 8.4:** Internet Archive snapshot
- **WBS 8.5:** DNSLink (optional)
- **Deliverable:** All 4 core layers verified (GitHub, Zenodo, R2, D1/KG)

---

## §3 Milestones with Gate Criteria

| Milestone | Phase | Tag | Gate Criteria |
|-----------|-------|-----|---------------|
| M0: Project Init | 0 | `v0.1-phase0` | Scaffold exists, PLANs written, git pushed |
| M1: Novelty Validated | 1-2 | `v0.3-phase2-lit` | KG + external search confirm zero prior full-ladder synthesis |
| M2: Deep Analysis | 3-4 | `v0.5-phase4-deep` | Bayesian cascade complete, calibration register locked |
| M3: Published | 5 | `v1.0` | Zenodo DOI resolves, PDF verified |
| M4: Deployed | 6 | `v1.1-deploy` | D1 entry exists, papers.qnfo.org HTTP 200 |
| M5: Distributed | 7-8 | `v1.3-distribute` | All 4 core layers + social dissemination complete |

---

## §4 Deliverable Registry

| ID | Deliverable | Phase | Format | Local Path | Archival Target(s) | Status |
|----|------------|-------|--------|-----------|-------------------|--------|
| D-0.1 | PROJECT-PLAN.md | 0 | Markdown | `PROJECT-PLAN.md` | GitHub | in-progress |
| D-0.2 | README.md | 0 | Markdown | `README.md` | GitHub | in-progress |
| D-0.3 | .gitignore | 0 | Text | `.gitignore` | GitHub | complete |
| D-5.1 | Research Synthesis (md) | 5 | Markdown | `harmonische-paradigma-research-synthesis.md` | GitHub, Zenodo, R2 | draft |
| D-5.2 | Research Synthesis (PDF) | 5 | PDF | `harmonische-paradigma-research-synthesis.pdf` | GitHub, Zenodo, R2 | verified* |
| D-5.3 | Provenance Bundle | 5 | ZIP | `PROVENANCE-BUNDLE.zip` | Zenodo | pending |
| D-6.1 | D1 living-paper record | 6 | SQL row | `living-paper.papers` | Cloudflare D1 | pending |
| D-6.2 | R2 archive copy | 6 | Files | `releases/2026/07/harmonische-paradigma/` | Cloudflare R2 | pending |
| D-7.1 | Social media posts | 7 | Buffer posts | — | Buffer (Twitter/LinkedIn/Bluesky) | pending |
| D-8.1 | KG Paper node | 8 | Graph node | — | QNFO Knowledge Graph | pending |
| D-8.2 | Internet Archive snapshot | 8 | URL | — | archive.org | pending |
| D-8.3 | Zenodo DOI | 5 | DOI | — | Zenodo | pending |

*PDF was built in prior session and verified with check-pdf.py — rebuild needed after paper.md cleanup.

---

## §5 Risk Register

| ID | Risk | Phase(s) Affected | Likelihood | Impact | Mitigation | Status |
|----|------|-------------------|------------|--------|-----------|--------|
| R-01 | Paper contains internal/project language leaking to public output | 5 | Low | High | Publication Language Gate scan before publication | open |
| R-02 | Zenodo API returns 500/timeout during upload | 5 | Medium | Low | Exponential backoff retry (1s/4s/16s), draft recovery | open |
| R-03 | PDF rebuild fails due to Unicode glyph issues | 5 | Medium | High | `unicode-latex-preprocess.py` before Pandoc; `check-pdf.py` verification | open |
| R-04 | D1 insert fails due to FTS5 shadow-table conflict | 6 | Medium | Medium | CHECK-THEN-WRITE pattern (no ON CONFLICT upsert) | open |
| R-05 | Buffer posting blocked by account queue limit | 7 | Low | Low | Verify queue capacity before post; disclose limit if hit | open |
| R-06 | Paper lacks sufficient formal rigor for peer review | 5-8 | Medium | Medium | Physics Writing Standards 18-point checklist | open |
| R-07 | Novelty claim challenged by undiscovered external paper | 1-2 | Low | High | Comprehensive multi-source literature search already performed | mitigated |
| R-08 | Core claim unfalsifiable in its strongest form | 0, 4 | Low | High | Core Claim Lock reformulation with specific falsifiability conditions | mitigated |

---

## §6 Success Criteria

1. **Novelty:** The full 8-rung Harmonic Ladder with α as unifying order parameter is confirmed genuinely novel (no prior publication synthesizes all rungs).
2. **Falsifiability:** Every core claim states specific disconfirming conditions per Physics Writing Standards.
3. **Zenodo DOI:** Paper published with persistent DOI, all metadata correct, DOI resolves independently.
4. **D1 Living-Paper:** Paper discoverable via papers.qnfo.org with correct slug and metadata.
5. **Core Distribution:** All 4 layers (GitHub, Zenodo, R2, D1/KG) verified independently.
6. **Social Dissemination:** Buffer posts queued on all 3 channels (Twitter, LinkedIn, Bluesky).

---

## §7 Version History

| Version | Date | Phase | Description |
|---------|------|-------|-------------|
| v0.1-phase0 | 2026-07-22 | 0 | Project initialization, scaffold, core claim lock |
| v4.0-closeout | 2026-07-22 | 5 | V4.0 published (DOI 10.5281/zenodo.21505993), RG program closed |
| cal01-v1.0 | 2026-07-23 | 9 | CAL-01 measurement program document created, Phase 0 initiated |

---

## §8 CAL-01 — Transmon Anharmonicity Measurement Sub-Program

**Parent:** Harmonic Paradigm V4.0 (DOI 10.5281/zenodo.21505993)
**Document:** `CAL-01-transmon-measurement-program.md`
**Deadline:** 2028-Q4
**Status:** ACTIVE — Phase 0 complete, Phase 1 (Device Design) pending
**Independent of:** Retracted RG-universality mechanism. ν is a static fabrication ratio.

### 8.1 Charter

CAL-01 is a **pure metrology program**: measure the transmon anharmonicity parameter
ν(E_J/E_C) across a systematic device series with E_J/E_C > 500 to test:

$$\nu(E_J/E_C) = \frac{1}{2} + c \cdot \left(\frac{E_C}{E_J}\right)^\nu, \quad \nu \approx 0.5$$

**Falsification criterion:** ν ∉ [0.40, 0.60] for E_J/E_C > 500.

The deep-transmon regime (E_J/E_C > 500) has never been systematically measured.
This is standard transmon physics (Koch et al. 2007) — a harmonic-oscillator
ground-truth measurement, not a test of any cross-scale hypothesis.

### 8.2 Phases

#### Phase 0: Literature Survey — ✅ COMPLETE (2026-07-23)
- **WBS 0.1:** Search arXiv for transmon anharmonicity systematic surveys
- **WBS 0.2:** Search PRL/PRA/PRB/APL for ν(E_J/E_C) measurements
- **WBS 0.3:** Search Nature/Nature Physics for deep-transmon characterization
- **WBS 0.4:** Extract Purkayastha et al. (2026) parameters
- **WBS 0.5:** Compile annotated bibliography
- **WBS 0.6:** Gap confirmation: verify no existing E_J/E_C > 500 data
- **Deliverable:** `artifacts/cal01-literature-survey.md`

#### Phase 1: Device Design — [PENDING]
- **WBS 1.1:** Finalize 8-device series parameters (E_J/E_C = 50–1500)
- **WBS 1.2:** Design junction geometries for target E_J
- **WBS 1.3:** Design capacitor geometries for target E_C
- **WBS 1.4:** Electromagnetic simulation (Sonnet/HFSS)
- **WBS 1.5:** Fabrication mask layout
- **Deliverable:** `artifacts/cal01-device-design.md`, GDSII mask files

#### Phase 2: Fabrication — [PENDING]
- **WBS 2.1:** Partner identification (foundry or academic cleanroom)
- **WBS 2.2:** First fabrication run (20 devices)
- **WBS 2.3:** Room-temperature screening (I_c, C_Σ at 300K)
- **WBS 2.4:** Yield analysis; iterate if needed
- **Deliverable:** Fabricated devices, screening report

#### Phase 3: Baseline Measurements (E_J/E_C = 50–200) — [PENDING]
- **WBS 3.1:** Dilution refrigerator cooldown
- **WBS 3.2:** Two-tone spectroscopy for ω₀₁, ω₁₂
- **WBS 3.3:** Ramsey interferometry for precision ω₀₁
- **WBS 3.4:** ν extraction for low-ratio devices
- **Deliverable:** `artifacts/cal01-baseline-measurements.md`, dataset

#### Phase 4: Deep-Transmon Measurements (E_J/E_C > 500) — [PENDING]
- **WBS 4.1:** High-resolution spectroscopy for small anharmonicity
- **WBS 4.2:** Systematic error control (AC Stark, thermal, TLS)
- **WBS 4.3:** ν extraction for high-ratio devices
- **WBS 4.4:** Cross-validation with independent E_J/E_C determination
- **Deliverable:** `artifacts/cal01-deep-transmon-measurements.md`, full dataset

#### Phase 5: Data Analysis — [PENDING]
- **WBS 5.1:** 3-model fit (Koch null / free-exponent / self-consistent)
- **WBS 5.2:** AICc model comparison
- **WBS 5.3:** MCMC parameter inference
- **WBS 5.4:** Systematic error propagation
- **WBS 5.5:** Falsification assessment
- **Deliverable:** `artifacts/cal01-analysis.md`, analysis code, figures

#### Phase 6: Publication — [PENDING]
- **WBS 6.1:** Draft manuscript (PRL/PRB format)
- **WBS 6.2:** Internal review
- **WBS 6.3:** arXiv preprint
- **WBS 6.4:** Journal submission
- **Deliverable:** arXiv preprint, journal submission

#### Phase 7: Dissemination — [PENDING]
- **WBS 7.1:** Zenodo deposit with full dataset
- **WBS 7.2:** D1 living-paper record
- **WBS 7.3:** Social media announcement
- **Deliverable:** Zenodo DOI, D1 record

### 8.3 Milestones

| Milestone | Phase | Target Date | Gate Criteria |
|-----------|-------|-------------|---------------|
| M-CAL-0 | 0 | 2026-Q4 | Literature survey complete, gap confirmed |
| M-CAL-1 | 1 | 2027-Q1 | Device design finalized, masks ready |
| M-CAL-2 | 2 | 2027-Q2 | Devices fabricated and screened |
| M-CAL-3 | 3 | 2027-Q3 | ν measured for E_J/E_C = 50–200 |
| M-CAL-4 | 4 | 2028-Q2 | ν measured for E_J/E_C = 500–1500 |
| M-CAL-5 | 5 | 2028-Q3 | Analysis complete, falsification assessed |
| M-CAL-6 | 6 | 2028-Q4 | Paper submitted/published |

### 8.4 Deliverables

| ID | Deliverable | Phase | Format | Path |
|----|------------|-------|--------|------|
| D-CAL-0 | Literature survey | 0 | Markdown | `artifacts/cal01-literature-survey.md` |
| D-CAL-1 | Device design document | 1 | Markdown + GDSII | `artifacts/cal01-device-design.md` |
| D-CAL-2 | Fabrication report | 2 | Markdown | `artifacts/cal01-fabrication-report.md` |
| D-CAL-3 | Baseline measurements | 3 | Markdown + CSV | `artifacts/cal01-baseline-data.csv` |
| D-CAL-4 | Deep-transmon measurements | 4 | Markdown + CSV | `artifacts/cal01-deep-transmon-data.csv` |
| D-CAL-5 | Analysis report | 5 | Markdown + Python | `artifacts/cal01-analysis.md` |
| D-CAL-6 | Publication manuscript | 6 | PDF | `paper-cal01.pdf` |
| D-CAL-7 | Zenodo dataset | 7 | DOI + ZIP | Zenodo |

### 8.5 Risk Register

| ID | Risk | Phase | Likelihood | Impact | Mitigation |
|----|------|-------|------------|--------|-----------|
| R-CAL-01 | No existing systematic ν(E_J/E_C) studies found (gap confirmed — good) | 0 | High | Positive | Confirms novelty; proceed to Phase 1 |
| R-CAL-02 | Purkayastha et al. (2026) already covers E_J/E_C > 500 | 0 | Low | High | Adjust scope to fill remaining gaps |
| R-CAL-03 | Anharmonicity too small to resolve at E_J/E_C > 1000 | 4 | Medium | Medium | Lower ceiling to E_J/E_C = 750 if needed |
| R-CAL-04 | Fabrication yield too low for deep-transmon designs | 2 | Medium | High | Multiple fabrication runs; partner with experienced foundry |
| R-CAL-05 | Competing group publishes first | 6 | Low | Medium | Preprint early; Phase 3 results publishable alone |
| R-CAL-06 | ν outside [0.40, 0.60] — prediction falsified | 5 | Low | High | Publish regardless; falsification is a valid scientific result |
