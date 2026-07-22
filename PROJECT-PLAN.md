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
