# Metacetamol

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.MolecularDiagrams/Metacetamol.png)

Figure .  The molecular diagram of Metacetamol.

# CSP studies

| REFCODE | MENSEE |
| --- | --- |
| Formula | C8 H9 N1 O2 |
| Common Name | Metacetamol |
| IUPAC Systematic Name | N-(3-hydroxyphenyl)acetamide |
| Other Names |  |
| CSD Refcodes | MENSEE01, MENSEE04 |
|  |  |
| Search Identifier | A |
| Scientist | Shihao Ying |
| Date | August 2025 |
| Publication | No publication planned. |
| Energy model | 2 |
| Study_ID | 10 |
| Programs | Study_ID=20, CrystalOptimizer (2.4.7.1), DMACRYS (2.3.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Metacetamol\\CrystalOptimizer |
| Potential Description | CrystalOptimizer with GDMA2.2(PBE0/6-31G(d,p)) + FIT with reduced carbon repulsion |
| Energy model | 1 |
| Study_ID | 20 |
| Programs | Flexible CrystalPredictor (2.4.3), DMACRYS (2.3.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\Metacetamol\\CrystalPredictor |
| Potential Description | CrystalPredictor + DMACRYS with GDMA2.2(PBE0/6-31G(d,p)) + FIT with reduced carbon repulsion |

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/Paracetamol_A1.png)

Figure .  Crystal energy landscape of Metacetamol.  Energy model 2, following CrystalOptimizer refinement.

# CSD structures (version 5.46 with Feb 2025 update)

Table .  Crystallographic information for CSD entries for Metacetamol.  Different polymorphs are coloured differently.

| REFCODE | space group | Z’ | a / Å | b / Å | c / Å | α / ° | β / ° | γ / ° | density / g cm<sup>-3</sup> | Form |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MENSEE | Pna21 | 1 | 10.5199 | 17.0195 | 4.2415 | 90 | 90 | 90 | 1.322 | I |
| MENSEE01 | Pna21 | 1 | 10.5129 | 17.0435 | 4.0675 | 90 | 90 | 90 | 1.378 | I |
| MENSEE02 | Pna21 | 1 | 10.522 | 17.062 | 4.058 | 90 | 90 | 90 | 1.378 | I |
| MENSEE03 | Pna21 | 1 | 10.5129 | 17.0435 | 4.0675 | 90 | 90 | 90 | 1.378 | I |
| MENSEE04 | P21 | 4 | 7.6202 | 19.01 | 10.1116 | 90 | 90.388 | 90 | 1.371 | II |
| MENSEE05 | Pna21 | 1 | 10.505 | 16.986 | 4.2444 | 90 | 90 | 90 | 1.326 | I |

Table .  Experimental information for CSD entries for Metacetamol.

| REFCODE | space group | R factor | T / K | Year | Comments |
| --- | --- | --- | --- | --- | --- |
| MENSEE | Pna21 | 3.23 | 293 | 2006 | Slow evaporation from ethanol<sup>1</sup> |
| MENSEE01 | Pna21 | 3.06 | 120 | 2008 | Not mentioned<sup>2</sup> |
| MENSEE02 | Pna21 | 4.95 | 100 | 2013 | Private communication |
| MENSEE03 | Pna21 | 3.06 | 120 | 2008 | Not mentioned<sup>3</sup> |
| MENSEE04 | P21 | 10.94 | 120 | 2015 | Heating to 430 K at 5 K min<sup>-1</sup>, followed by cooling at 0.4 K min<sup>-1</sup>.  Something similar to make a single crystal.<sup>4</sup> |
| MENSEE05 | Pna21 | 3.19 | 296 | 2024 | Private communication, from solution. |

Make this table include whether polymorphs are solution-grown, sublimation grown, templated or otherwise.  Add references.

# Other notes

Mercury’s Crystal Packing Similarity tool (initially 5 molecules and default tolerances) showed that four structures match MENSEE01.  A86 is the best match, but A636, A1911 and A2851 would all match 30 molecules if slightly looser tolerances were used, and would be clustered out if looser criteria were used.

Some structures also match the layer of MENSEE04.  However, the Crystal Packing Similarity tool did not find them all as one of the five molecules was in the next layer.  Therefore, a Crystal Packing Feature search was carried out using 10 molecules of the same layer looking for Medium geometric similarity.  The following structures all match with RMSD<sub>10</sub> < 0.3 Å.  A124, A131, A395, A974, A1013, A7255, A7273.  All match a single layer, but with the adjacent layer being different.

1.	L. K. Hansen, G. L. Perlovich and A. Bauer-Brandl, *Acta Crystallographica Section E*, 2006, **62**, o3627-o3628.

2.	S. L. Huth, T. L. Threlfall and M. B. Hursthouse, *University of Southampton, Crystal Structure Report Archive*, 2008.

3.	S. L. Coles, T. L. Threlfall and M. B. Hursthouse, *University of Southampton, Crystal Structure Report Archive*, 2008.

4.	L. McGregor, D. Rychkov, P. Coster, S. Day, V. Drebushchak, A. Achkasov, G. Nichol, C. Pulham and E. Boldyreva, *Crystengcomm*, 2015, **17**, 6183-6192.
