# Guanine

(Last updated 2 December 2024)

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.MolecularDiagrams/Guanine.png)

Figure .  The molecular diagram of the three tautomers of guanine for which searches have been carried out.

# CSP studies

When Louise came to reupload these, there were no .dmaout files for taut19.  Since this stops the upload process working, these files needed to be recreated, and to maintain consistency, this was also done for the other tautomers.  Charge densities were regenerated for each of the five conformations, using the same molecular axis system as previously, at the MP2/6-31G(d,p) level of theory (presumably equivalent to the previous work) and GDMA2.2 used to extract distributed multipoles (the previous work would have used GDMA1).  If the structures were optimized, although the majority remained very close to the original crystal structures, a few changed considerably (of the 109 crystal structures, 6 ended up with an F value over 100 and a further 16 had an F value over 30).  Since the one which changed the most (F = 1916) was the match to experimental form beta and it had transformed to match experimental form alpha, it was felt that it would be better to not optimize the crystal structures, but remove the calculation of splines and run DMACRYS for zero iterations (so as to most closely match the previous work).

| REFCODE | KEMDOW |
| --- | --- |
| Formula | C5 H5 N5 O1 |
| Common Name | Guanine |
| IUPAC Systematic Name | 2-amino-1,7-dihydro-6H-purin-6-one |
| CSD Refcodes | KEMDOW, KEMDOW01 |
|  |  |
| Scientist | Tom Lewis |
| Date | 2005 |
| Publication | No publication planned. |
| Search Identifier | A |
| Energy Model | 1 |
| Study_ID | 1 |
| Programs | Molpak, DMAREL (4.1.1), DMACRYS (2.3.1.1 single point) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\guanine\\taut17 |
| Potential Description | GDMA2.2(MP2/6-31G(d,p) + Fit with reduced carbon repulsion |
| Search Identifier | B |
| Energy Model | 1 |
| Study_ID | 0 |
| Programs | Molpak, DMAREL (4.1.1), DMACRYS (2.3.1.1 single point) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\guanine\\taut19 |
| Potential Description | GDMA2.2(MP2/6-31G(d,p) + Fit with reduced carbon repulsion |
| Search Identifier | C |
| Energy Model | 1 |
| Study_ID | 2 |
| Programs | Molpak, DMAREL (4.1.1), DMACRYS (2.3.1.1 single point) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\guanine\\taut39 |
| Potential Description | GDMA2.2(MP2/6-31G(d,p) + Fit with reduced carbon repulsion |
|  |  |
| Scientist | Louise Price |
| Date | 2024 |
| Publication | No publication planned. |
| Search Identifier | A/B/C |
| Energy Model | 2 |
| Study_ID | 3 |
| Programs | Study_ID=0/1/2, DMACRYS (2.3.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\guanine\\reopt |
| Potential Description | GDMA2.2(MP2/6-31G(d,p) + Fit with reduced carbon repulsion |

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/Nitrofurantoin_A1.png)

Figure .  Crystal energy landscape of (left) taut17 of guanine from previous work and (right) all three tautomers (5 conformations) of guanine, reoptimized and with conformational energy penalties included.

# CSD structures (CSD version 5.45 with Mar, Jun and Sep 2024 updates)

Table .  Crystallographic information for CSD entries for XXX.  Different polymorphs are coloured differently.

| REFCODE | space group | Z’ | a / Å | b / Å | c / Å | α / ° | β / ° | γ / ° | density / g cm<sup>-3</sup> | Form |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KEMDOW | P21/c | 1 | 3.553 | 9.693 | 16.345 | 90 | 95.748 | 90 | 1.792 | alpha |
| KEMDOW01 | P1121/b | 1 | 3.629473 | 9.812765 | 18.42691 | 90 | 90 | 118.0423 | 1.733 | beta |
| KEMDOW02 | P21/c | 1 | 3.631 | 18.440 | 9.815 | 90 | 118.05 | 90 | 1.731 | beta |

Table .  Experimental information for CSD entries for XXX.

| REFCODE | space group | R factor | T / K | Year | Comments |
| --- | --- | --- | --- | --- | --- |
| KEMDOW | P21/c | 5.87 | 120 | 2006 | an attempted solvothermal synthesis, using guanine (150 mg) and solid potassium (40 mg) in dry ethanol (10 ml). The mixture was stirred for 1 h and then heated in an autoclave at 523 K for 7 d.  Synchrotron radiation.<sup>1</sup> |
| KEMDOW01 | P1121/b | 5.96 | 0 | 2015 | Dissolving 0.1 g of guanine powder (Sigma–Aldrich) in 10 mL of 1 N NaOH (pH 14) inside a glass flask. HCl (1 N) was then titrated into the flask until the solution reached pH 11 and became cloudy due to the formation of small guanine crystals. The suspension was then filtered using a PVDF filter (0.22 mm) and dried overnight in a desiccator.  Powder diffraction.<sup>2</sup> |
| KEMDOW02 | P21/c | 24.1 | RT | 2024 | Solved directly from electron diffraction of biogenic guanine crystals from three biological origins: spider integument, scallop eyes, and fish scales.<sup>3</sup> |

The alpha and beta polymorphs contain the same hydrogen bonded sheet.

Guanine monohydrate contains a different tautomer.

A further form, orthorhombic and named gamma, is indicated by electron diffraction.

# Other notes

1.	K. Guille and W. Clegg, *Acta Crystallographica Section C - Crystal Structure Communications*, 2006, **62**, o515-o517.

2.	A. Hirsch, D. Gur, I. Polishchuk, D. Levy, B. Pokroy, A. J. Cruz-Cabeza, L. Addadi, L. Kronik and L. Leiserowitz, *Chemistry of Materials*, 2015, **27**, 8289-8297.

3.	A. Wagner, J. Merkelbach, L. Samperisi, N. Pinsk, B. M. Kariuki, C. E. Hughes, K. D. M. Harris and B. A. Palmer, *Crystal Growth & Design*, 2024, **24**, 899-905.
