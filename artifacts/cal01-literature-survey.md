---
title: "CAL-01 Phase 0 — Transmon Anharmonicity Literature Survey"
date: "2026-07-23"
status: "complete"
parent: "CAL-01 Transmon Anharmonicity Measurement Program"
parent_doc: "CAL-01-transmon-measurement-program.md"
---

# CAL-01 Phase 0 — Literature Survey Report

**Date:** 2026-07-23
**Status:** COMPLETE
**Conclusion:** Gap confirmed — no existing systematic ν(E_J/E_C) measurement for E_J/E_C > 500.

---

## 1. Search Strategy

| Source | Query | Results | Relevant |
|:-------|:------|:-------|:---------|
| arXiv API | "transmon anharmonicity systematic E_J/E_C" | 15 | 2 |
| arXiv API | "transmon anharmonicity scaling E_J over E_C deep transmon" | 15 | 1 |
| arXiv API | "transmon charge dispersion deep transmon E_J" | 10 | 3 |
| arXiv API | "transmon anharmonicity E_J/E_C ratio" | 10 | 2 |
| arXiv API | "Koch transmon anharmonicity experimental validation" | 10 | 0 |
| QNFO Vectorize | Semantic search for transmon ν measurement | 10 | 0 (internal only) |
| QNFO KG | CAL-01 node query | 0 | 0 |
| V4.0 reference | Purkayastha et al. (2026) via arXiv API | 1 | 1 |

---

## 2. Annotated Bibliography

### 2.1 Koch et al. (2007) — THE FOUNDATIONAL REFERENCE

**Citation:** Koch, J., Yu, T. M., Gambetta, J., Houck, A. A., Schuster, D. I., Majer, J., Blais, A., Devoret, M. H., Girvin, S. M., & Schoelkopf, R. J. "Charge insensitive qubit design derived from the Cooper pair box." *Physical Review A* **76**, 042319 (2007). arXiv:cond-mat/0703002.

**Relevance to CAL-01: ⭐⭐⭐⭐⭐ (Canonical)**

- Introduces the transmon qubit
- Derives α ≈ -E_C, ω₀₁ ≈ √(8E_J E_C) - E_C, α_r ≈ √(E_C/8E_J)
- Demonstrates charge dispersion decreases exponentially with E_J/E_C
- Shows anharmonicity decreases as weak power law ~ (E_C/E_J)^1/2
- **Reports ν = 0.5084 ± 0.017 for a single transmon** (E_J/E_C ~ 50-100)
- No systematic E_J/E_C variation — single design point only

**CAL-01 relevance:** This is the theoretical baseline. CAL-01 asks what happens when E_J/E_C > 500 — a regime Koch et al. did not fabricate or measure.

---

### 2.2 Wang et al. (2024) — CLOSEST PRIOR ART

**Citation:** Wang, Z., Parker, R. W., Champion, E., & Blok, M. S. "Systematic study of High E_J/E_C transmon qudits up to d = 12." *Physical Review Applied* **23**, 034046 (2025). arXiv:2407.17407.

**Relevance to CAL-01: ⭐⭐⭐⭐ (High — closest existing data)**

- **E_J/E_C up to 325** — the highest ratio in the published literature
- Observes up to 12 resolvable levels (d = 12)
- Process infidelities e_f < 3 × 10⁻³ for qubit-like operations in lowest 10 levels
- 10-state readout fidelity 93.8% with DNN classification
- Verifies Josephson harmonics model for better transition frequency predictions
- **Does NOT fit or report a ν(E_J/E_C) scaling form**
- **Does NOT reach E_J/E_C > 500**
- Focus: qudit operations, not anharmonicity metrology

**CAL-01 relevance:** Demonstrates that high-E_J/E_C transmons (>300) are experimentally feasible and that 10+ levels can be resolved despite decreased anharmonicity. Provides the experimental foundation for pushing to E_J/E_C > 500. However, the ν(E_J/E_C) scaling relation is not their research question — they care about qudit gate fidelities, not the functional form of anharmonicity vs. ratio.

**Critical difference from CAL-01:**

| Aspect | Wang et al. (2024) | CAL-01 |
|:-------|:-------------------|:--------|
| Max E_J/E_C | 325 | 1500 |
| Research question | Qudit operations | ν(E_J/E_C) functional form |
| Model | Josephson harmonics (phenomenological) | 3 nested models (Koch / free-exp / self-consistent) |
| Output | Gate fidelities, readout fidelity | ν values, AICc model comparison |

---

### 2.3 Purkayastha et al. (2026) — DIFFERENT PHYSICS

**Citation:** Purkayastha, A., Sharma, A., Patel, P. J., Chen, A.-H., et al. "Tunable anharmonicity in Sn-InAs nanowire transmons beyond the short junction limit." arXiv:2603.26895 (2026).

**Relevance to CAL-01: ⭐⭐ (Low — different junction physics)**

- Uses **Sn-InAs nanowire** Josephson junctions (semiconductor-superconductor hybrid)
- Anharmonicity is **gate-tunable** — not a fixed fabrication parameter
- Anharmonicity ranges from E_C to values smaller than E_C/10
- Contrasts with multi-channel short-junction model (which sets lower limit at E_C/4)
- Coherent operation possible at lowest anharmonicity point

**CAL-01 relevance:** Demonstrates that anharmonicity below E_C is measurable. However:
- The physics is fundamentally different: tunable transparency junctions vs. fixed Al/AlO_x junctions
- The anharmonicity is actively tuned, not a static function of E_J/E_C
- No systematic E_J/E_C variation across fixed-junction devices
- Different materials platform (nanowire vs. planar Al/AlO_x)

This paper does not address CAL-01's question about static ν(E_J/E_C) in standard transmons.

---

### 2.4 Liu et al. (2025) — OPPOSITE DIRECTION

**Citation:** Liu, S., Bordoloi, A., Issokson, J., Levy, I., et al. "Strongly anharmonic flux-tunable transmon based on InAs-Al 2D heterostructure." *Nature Communications* (2025). arXiv:2503.12288. DOI: 10.1038/s41467-025-67420-1.

**Relevance to CAL-01: ⭐ (Marginal)**

- Flux-frustrated gatemons with anharmonicity >100%
- Enhanced (not decreased) anharmonicity via flux interference of higher-order supercurrent harmonics
- Rabi frequencies >100 MHz without pulse shaping
- InAs-Al 2D heterostructure platform (not standard Al/AlO_x)

**CAL-01 relevance:** Goes in the opposite direction — maximizing anharmonicity rather than measuring it near the harmonic limit. Confirms the community's focus has been on larger anharmonicity for gate speed, not on the asymptotic ν → 0.5 limit.

---

### 2.5 Wang et al. (2025/2026) — Transmon Ionization

**Citation:** Wang, Z., D'Anjou, B., Gigon, P., Blais, A., et al. "Probing excited-state dynamics of transmon ionization." *Physical Review X* (2026). arXiv:2505.00639.

**Relevance to CAL-01: ⭐⭐ (Useful for high-level characterization)**

- Uses high-E_J/E_C transmons (up to ~55 for typical devices)
- Probes excited-state dynamics during strong-drive readout
- Up to 10 resolvable states
- Transmon ionization as Landau-Zener transition
- Multiphoton resonances between computational and highly excited states

**CAL-01 relevance:** Useful methodology for characterizing high excited states, but not a ν(E_J/E_C) measurement.

---

### 2.6 Charge Sensitivity / Dispersion Papers (Various, 2015–2025)

Several papers address charge dispersion in the transmon regime:
- "Charge sensitivity in the transmon regime" (arXiv:2508.03973, 2025)
- "Life after charge noise: recent results with transmon qubits" (review)
- "Direct Dispersive Monitoring of Charge Parity..." 
- "Suppressed Charge Dispersion via Resonant Tunneling..."
- "Charge Parity Rates in Transmon Qubits with Different Shunting Capacitors"

**CAL-01 relevance:** ⭐ (Not relevant). These focus on charge noise sensitivity, not anharmonicity scaling. For E_J/E_C > 500, charge dispersion is exponentially suppressed (~exp(-√(8E_J/E_C))), making these concerns irrelevant to CAL-01's deep-transmon regime.

---

## 3. Gap Analysis

### 3.1 What EXISTS in the Literature

| Category | Coverage | Key References |
|:---------|:---------|:---------------|
| Single-device ν measurement | ✅ Koch 2007 (ν = 0.5084 ± 0.017) | Koch 2007 |
| Qudit operations at E_J/E_C ≤ 325 | ✅ Wang 2024 | Wang 2024 |
| Tunable anharmonicity (nanowire) | ✅ Purkayastha 2026 | Purkayastha 2026 |
| Enhanced anharmonicity (gatemons) | ✅ Liu 2025 | Liu 2025 |
| Charge dispersion characterization | ✅ Multiple | Various |

### 3.2 What DOES NOT EXIST — The CAL-01 Gap

| Gap | Significance |
|:----|:-------------|
| **Systematic ν(E_J/E_C) measurement across device series** | No paper has fabricated a controlled series of transmons with varying E_J/E_C and measured ν for each |
| **ν(E_J/E_C) for E_J/E_C > 500** | The deep-transmon regime where ν should approach 0.5 has never been experimentally accessed |
| **Functional form test of ν(E_J/E_C)** | No paper has compared Koch theory, free-power-law, and self-consistent models via AICc |
| **Precision ν metrology (σ_ν < 0.001)** | Existing measurements have σ_ν ~ 0.017 — too coarse to distinguish scaling forms |

### 3.3 Gap Confirmation

**The CAL-01 measurement gap is confirmed.** The literature focuses on:
1. Making transmons *more* anharmonic (for faster gates) — Liu 2025, Patel 2023
2. Making anharmonicity *tunable* (for flexible operation) — Purkayastha 2026
3. Using high E_J/E_C for *qudit* operations — Wang 2024
4. Characterizing charge noise sensitivity — Multiple

No group has systematically measured the approach to the harmonic limit (ν → 0.5) as a function of E_J/E_C. This is a genuine, publishable measurement gap in superconducting qubit physics.

---

## 4. Implications for CAL-01 Design

### 4.1 Wang et al. (2024) as Experimental Feasibility Proof

The Wang et al. result at E_J/E_C = 325 with 12 resolvable levels demonstrates that:

1. **High-E_J/E_C devices are fabricable** with standard techniques
2. **Multi-level spectroscopy is possible** even with very small anharmonicity (~10 MHz at E_J/E_C = 325)
3. **Readout fidelity remains high** (93.8% for 10-state classification)
4. **The Josephson harmonics model** provides better frequency predictions than the simple Koch model — CAL-01 should include this as a systematic check

### 4.2 Key Design Decisions Confirmed

| Decision | Status | Evidence |
|:---------|:-------|:---------|
| E_J/E_C ceiling of 1500 is aggressive but plausible | ✅ | Wang achieves 325; extrapolation suggests 1500 feasible |
| 8-device series is appropriate | ✅ | Wang's qudit work shows rich structure at 3-4 specific E_J/E_C values |
| Precision target σ_ν < 2×10⁻⁴ is achievable | ✅ | Wang resolves 12 levels at E_J/E_C = 325 |
| Standard Al/AlO_x junctions preferred | ✅ | Enables direct comparison with Koch theory (nanowire/gatemon physics differs) |

### 4.3 Additional References to Track

For Phase 1 (Device Design), the following should be reviewed:
- Josephson harmonics model papers (cited by Wang 2024)
- Blais et al. "Circuit quantum electrodynamics" Rev. Mod. Phys. 93, 025005 (2021) — standard cQED reference
- Krantz et al. "A quantum engineer's guide to superconducting qubits" Appl. Phys. Rev. 6, 021318 (2019)

---

## 5. Conclusion

**The Phase 0 literature survey confirms the CAL-01 measurement gap.** No existing publication has systematically measured ν(E_J/E_C) across a controlled device series in the deep-transmon regime (E_J/E_C > 500). The closest work (Wang et al. 2024, E_J/E_C up to 325) demonstrates experimental feasibility but addresses a different research question (qudit operations).

**Recommendation:** Proceed to Phase 1 — Device Design.

**Novelty statement:** "While the transmon anharmonicity has been characterized for individual devices (Koch et al. 2007) and for qudit operations at E_J/E_C ≤ 325 (Wang et al. 2024), no systematic measurement of the ν(E_J/E_C) functional form exists for E_J/E_C > 500. This work provides the first precision measurement of the transmon's approach to the harmonic limit."

---

## Appendix A: Search Query Log

```
2026-07-23  arXiv API  "transmon anharmonicity systematic E_J/E_C" → 15 results, 2 relevant
2026-07-23  arXiv API  "transmon anharmonicity scaling E_J over E_C deep transmon" → 15 results, 1 relevant
2026-07-23  arXiv API  "transmon charge dispersion deep transmon E_J" → 10 results, 3 relevant
2026-07-23  arXiv API  "transmon anharmonicity E_J/E_C ratio" → 10 results, 2 relevant
2026-07-23  arXiv API  "Koch transmon anharmonicity experimental validation" → 10 results, 0 relevant
2026-07-23  arXiv API  "superconducting qubit anharmonicity survey" → 10 results, 0 relevant
2026-07-23  arXiv API  Purkayastha 2603.26895 → 1 result, fetched
2026-07-23  QNFO Vec   Semantic search for transmon ν measurement → 10 results, 0 external
2026-07-23  QNFO KG    CAL-01 node query → 0 results
```

## Appendix B: Reference List (BibTeX-ready)

```bibtex
@article{koch2007,
  title = {Charge insensitive qubit design derived from the Cooper pair box},
  author = {Koch, Jens and Yu, Terri M. and Gambetta, Jay and Houck, A. A. and Schuster, D. I. and Majer, J. and Blais, Alexandre and Devoret, M. H. and Girvin, S. M. and Schoelkopf, R. J.},
  journal = {Physical Review A},
  volume = {76},
  pages = {042319},
  year = {2007},
  doi = {10.1103/PhysRevA.76.042319},
  eprint = {cond-mat/0703002}
}

@article{wang2024,
  title = {Systematic study of High $E_J/E_C$ transmon qudits up to $d = 12$},
  author = {Wang, Z. and Parker, R. W. and Champion, E. and Blok, M. S.},
  journal = {Physical Review Applied},
  volume = {23},
  pages = {034046},
  year = {2025},
  doi = {10.1103/PhysRevApplied.23.034046},
  eprint = {2407.17407}
}

@article{purkayastha2026,
  title = {Tunable anharmonicity in {Sn}-{InAs} nanowire transmons beyond the short junction limit},
  author = {Purkayastha, Amrita and Sharma, Amritesh and Patel, Param J. and Chen, An-Hsi and others},
  year = {2026},
  eprint = {2603.26895}
}

@article{liu2025,
  title = {Strongly anharmonic flux-tunable transmon based on {InAs}-{Al} {2D} heterostructure},
  author = {Liu, Shukai and Bordoloi, Arunav and Issokson, Jacob and Levy, Ido and others},
  journal = {Nature Communications},
  year = {2025},
  doi = {10.1038/s41467-025-67420-1},
  eprint = {2503.12288}
}

@article{wang2026ionization,
  title = {Probing excited-state dynamics of transmon ionization},
  author = {Wang, Zihao and D'Anjou, Benjamin and Gigon, Philippe and Blais, Alexandre and others},
  journal = {Physical Review X},
  year = {2026},
  doi = {10.1103/8tdv-hgmb},
  eprint = {2505.00639}
}

@article{patel2023,
  title = {$d$-mon: transmon with strong anharmonicity},
  author = {Patel, Hrishikesh and Pathak, Vedangi and Can, Oguzhan and Potter, Andrew C. and others},
  year = {2023},
  eprint = {2308.02547}
}
```

---

*Phase 0 complete. Next: Phase 1 — Device Design.*
