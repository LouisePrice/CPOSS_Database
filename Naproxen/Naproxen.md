# Naproxen

(Last updated 27 May 2024)

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.MolecularDiagrams/Naproxen.png)

Figure .  The molecular diagram of Naproxen.

In the CSD structures, the OMe group is in the plane of the ring.  The Me and COOH are above and below the plane of the ring (the H is in the plane of the ring).

# CSP studies

The angle in the experimental conformation was close to 70, and so the first search consisted of two rigid molecule MOLPAK searches with the fully optimized and constrained optimized conformations.  This was originally an “EarlySearch.”  An approximation to the experimental structure was found in both.

Later, this was then extended to include 8 distinct conformations, although only files in three of the new conformations were stored.  Since the structures were on a consistent energy surface, they were both called study_id=0, although the files were stored in different locations.  These have now been stored in the same naproxen_molpak folder, and conformation opt renamed CONFa.  The previous structures with the constrained optimized conformation and the other conformations which only gave high energy structures have been removed.

A limited CrystalPredictor search was also carried out, with only CONFa and only in spacegroup Pbca.  This was not stored on the S: drive, but Emiliana’s files are still on cposs.  However, the structure labels don’t match!  CP37 on the spreadsheet was called 27-1 in the search!  CP14 was 18-1.  The paper reported only 4 structures, two of which were the same (symmetry reduced and not).  These were labelled 1, 70 and 433 and match the structure labels on cposs.  There were also searches in other spacegroups, but these were not uploaded, not included in any spreadsheet and not reported in the paper.  Therefore, the CP_Pbca search on cposs has been reuploaded and replaces the unexplained data on the database.

These two searches were combined, and CrystalOptimizer run on selected structures.

Spreadsheets and data on the database relating to the Williams potential and the exp conformation have been deleted.

In 2024, a new search was carried out, with the molecule kept flexible in the eight different regions previously identified.

| REFCODE | COYRUD |
| --- | --- |
| Formula | C14 H14 O3 |
| Common Name | Naproxen |
| IUPAC Systematic Name | S-2-(6-methoxynaphthalen-2-yl)propanoic acid |
| Other Names |  |
| CSD Refcodes | COYRUD14, PAPTUX |
|  |  |
| Search Identifier | A |
| Scientist | Louise Price |
| Date | June 2024 |
| Publication | Database Comparison paper |
| Energy model | 2 |
| Study_ID | 11 |
| Programs | Study_ID=20, CrystalOptimizer (2.4.7.1), DMACRYS (2.3.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Naproxen\\CrystOpt |
| Potential Description | CrystalOptimizer PBE1PBE/6-31G(d,p) intramolecular + GDMA2.2(PBE1PBE/6-31G(d,p)) DMA + FIT |
| Intramolecular Description | PBE0/6-31G(d,p) |
| Energy model | 1 |
| Study_ID | 20 |
| Programs | CrystalPredictor (2.4.3), DMACRYS (2.3.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Naproxen\\CrystPred |
| Potential Description | CrystalPredictor2.4.3.2(torsion groups) + DMACRYS with GDMA2.2(PBE0/6-31G(d,p)) + FIT |
| Intramolecular Description | PBE0/6-31G(d,p) |
|  |  |
| Search Identifier | B |
| Scientist | Emiliana D'Oria |
| Date | 2009-2010 |
| Publication | Braun DE; Ardid-Candel M; D'Oria E; Karamertzanis PG; Arlin JB; Florence AJ; Jones AG; Price SL. Cryst Growth Des 2011, 11(12), 5659-5669 (Paper reports PCM refinement of structures in this set.) |
| Energy model | 3 |
| Study_ID | 10 |
| Programs | Study_ID=0 and Study_ID=2, CrystalOptimizer (2.0), DMACRYS (2.0.2) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Naproxen\\naproxen_crystopt |
| Potential Description | CrystalOptimizer RHF/6-31G(d,p) Intra, GDMA(MP2/6-31G(d,p)) DMA + FIT |
| Intramolecular Description | RHF 6-31G(d,p) |
| Energy model | 2 |
| Study_ID | 0 |
| Programs | MOLPAK, DMAREL (4.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Naproxen\\naproxen_molpak |
| Potential Description | DMA + FIT |
| Intramolecular Description | MP2/6-31G(d,p) |
| Energy model | 1 |
| Study_ID | 21 |
| Programs | Rigid CrystalPredictor (run at IC by Panos), DMACRYS (2.0.2a) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Naproxen\\naproxen_crystpred |
| Potential Description | DMA + FIT |
| Intramolecular Description | MP2/6-31G(d,p) |

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/Naproxen_A2.png)![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/Naproxen_B3.png)

Figure .  Crystal energy landscapes of Naproxen from previous work.  Left: Original search, combined CrystalOptimizer (Study_ID=10).  Right: Updated search, CrystalOptimizer (Study_ID=11).

# CSD structures (CSD version 5.45 with Nov 2023 update)

Table .  Crystallographic information for CSD entries for Naproxen.  Different polymorphs are coloured differently.

| REFCODE | space group | Z’ | a / Å | b / Å | c / Å | α / ° | β / ° | γ / ° | density / g cm<sup>-3</sup> | Form |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COYRUD | P21 | 1 | 13.315 | 5.7765 | 7.8732 | 90 | 93.88 | 90 | 1.266 | Enantiopure |
| COYRUD01 | P21 | 1 | 7.855 | 5.783 | 13.349 | 90 | 93.9 | 90 | 1.264 | Enantiopure |
| COYRUD11 | P21 | 1 | 13.375 | 5.793 | 7.914 | 90 | 93.91 | 90 | 1.25 | Enantiopure |
| COYRUD12 | P21 | 1 | 7.7354 | 5.7181 | 13.3641 | 90 | 93.737 | 90 | 1.296 | Enantiopure |
| COYRUD13 | P21 | 1 | 7.8759 | 5.7834 | 13.323 | 90 | 93.877 | 90 | 1.263 | Enantiopure |
| COYRUD14 | P21 | 1 | 7.7162 | 5.7022 | 13.371 | 90 | 93.73 | 90 | 1.303 | Enantiopure |
| PAPTUX | Pbca | 1 | 25.8301 | 15.4939 | 5.9465 | 90 | 90 | 90 | 1.285 | Racemic |
| PAPTUX01 | Pbca | 1 | 5.953 | 25.93 | 15.2 | 90 | 90 | 90 | 1.304 | Racemic |

Table .  Experimental information for CSD entries for Naproxen.

| REFCODE | space group | R factor | T / K | Year | Comments |
| --- | --- | --- | --- | --- | --- |
| COYRUD | P21 | 5.3 | 295 | 1985 | Slow evaporation of a saturated solution in benzene at room temperature<sup>2</sup> |
| COYRUD01 | P21 | 9.9 | 295 | 1984 | No coordinates; recrystallized from ethanol solution (paper not online) |
| COYRUD11 | P21 | 4.2 | 295 | 1987 | Refinement of COYRUD01 data? (paper not online) |
| COYRUD12 | P21 | 3.43 | 102 | 2011 | Slow evaporation of a benzene solution<sup>3</sup> |
| COYRUD13 | P21 | 3.03 | 298 | 2015 | Evaporation from ethanol/water mixture<sup>4</sup> |
| COYRUD14 | P21 | 2.81 | 100 | 2018 | Melt crystallization between two squeezed CaF<sub>2</sub> plates (but not for the XRD?)<sup>5</sup> |
| PAPTUX | Pbca | 4.5 | 298 | 2011 | Powder diffraction; recrystallized from ethanol<sup>1</sup> |
| PAPTUX01 | Pbca | 12.61 | 100 | 2016 | Private communication |

Make this table include whether polymorphs are solution-grown, sublimation grown, templated or otherwise.  Add references.

# Other notes

(1) Braun, D. E.; Ardid-Candel, M.; D'Oria, E.; Karamertzanis, P. G.; Arlin, J. B.; Florence, A. J.; Jones, A. G.; Price, S. L. Racemic Naproxen: A Multidisciplinary Structural and Thermodynamic Comparison with the Enantiopure Form. *Crystal Growth & Design ***2011**, *11* (12), 5659-5669.

(2) Ravikumar, K.; Rajan, S. S.; Pattabhi, V.; Gabe, E. J. Structure of naproxen, C14H14O3. *Acta Crystallographica Section C ***1985**, *41* (2), 280-282. DOI: doi:10.1107/S0108270185003626.

(3) King, M. D.; Buchanan, W. D.; Korter, T. M. Application of London-type dispersion corrections to the solid-state density functional theory simulation of the terahertz spectra of crystalline pharmaceuticals. *Physical Chemistry Chemical Physics ***2011**, *13* (10), 4250-4259, Article. DOI: 10.1039/c0cp01595d.

(4) Tang, G.-M.; Wang, J.-H.; Zhao, C.; Wang, Y.-T.; Cui, Y.-Z.; Cheng, F.-Y.; Ng, S. W. Multi odd–even effects on cell parameters, melting points, and optical properties of chiral crystal solids based on S-naproxen. *CrystEngComm ***2015**, *17* (38), 7258-7261, 10.1039/C5CE01345C. DOI: 10.1039/C5CE01345C.

(5) Hachuła, B. The nature of hydrogen-bonding interactions in nonsteroidal anti-inflammatory drugs revealed by polarized IR spectroscopy. *Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy ***2018**, *188*, 189-196. DOI: [https://doi.org/10.1016/j.saa.2017.07.005](https://doi.org/10.1016/j.saa.2017.07.005).
