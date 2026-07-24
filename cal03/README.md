# CAL-03 — CMB Log-Periodogram: Efimov/DSI Search

**Parent DOI**: [10.5281/zenodo.21499051](https://doi.org/10.5281/zenodo.21499051) (Harmonic Paradigm)
**Status**: Archived 2026-07-23
**Deadline**: 2028-Q4 (CMB-S4 definitive test)

## Summary

Search for log-periodic oscillations in the Planck 2018 CMB TT power spectrum with periods ln(q) ≈ 1 (Efimov, q ≈ e) and ln(q) ≈ ln(π) ≈ 1.14. Physically motivated by the Efimov effect and discrete scale invariance (DSI), independent of the retracted Harmonic Paradigm logistic β-function mechanism.

**Result**: H₀ NOT REJECTED. No statistically significant log-periodic oscillations detected. Global MC p-value = 0.38 (full unbinned spectrum, 200 ΛCDM+noise mocks). B₉₅ < 0.004 amplitude constraint.

## Contents

| File | Description |
|:-----|:------------|
| `CAL-03-cmb-log-periodogram.md` | Full analysis report (includes binned + full-spectrum results) |
| `cal03_log_periodogram.py` | Binned-spectrum analysis pipeline (83 bins) |
| `cal03_log_periodogram_full.py` | Full-spectrum analysis pipeline (2471 pts, definitive) |
| `results.json` | Binned-spectrum numerical results |
| `results_full.json` | Full-spectrum numerical results (definitive) |
| `data/` | Planck 2018 data files (binned, full, best-fit theory) |
| `figures/` | 8 figures (4 binned + 4 full-spectrum) |

## Data Provenance

All input data from ESA Planck Legacy Archive, Release 3.01 (2018):

- **Full unbinned TT**: `https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-full_R3.01.txt` (170,547 bytes local copy included)
- **Binned TT**: `https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmology/COM_PowerSpect_CMB-TT-binned_R3.01.txt`
- **Best-fit ΛCDM**: `https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmology/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt`

## Reproducibility

```bash
# Install dependencies
pip install numpy scipy matplotlib

# Run full-spectrum analysis (definitive)
python cal03_log_periodogram_full.py
```

All data files are self-contained — no network access required.

## References

1. Efimov, V. (1970). *Phys. Lett. B* 33, 563.
2. Kraemer, T. et al. (2006). *Nature* 440, 315.
3. Floerchinger, S. et al. (2011). *Few-Body Syst.* 51, 153.
4. Planck Collaboration (2020). *A&A* 641, A1.
