# 2-Chlorobenzamide

(Last updated December 2025)

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.MolecularDiagrams/2chlorobenzamide.png)

Figure .  The molecular diagram of 2-chlorobenzamide.

# CSP studies

| REFCODE | CLBZAM |
| --- | --- |
| Formula | C7 H6 N1 O1 Cl1 |
| Common Name | 2-Chlorobenzamide |
| IUPAC Systematic Name | 2-Chlorobenzamide |
| Other Names | 2-Chlorobenzamide |
| CSD Refcodes | CLBZAM12, CLBZAM11, CLBZAM13 |
|  |  |
| Search Identifier | A |
| Scientist | Louise Price |
| Date | 2011 |
| Publication | Cockcroft JK; Buanz ABM; Ntantou A; Price LS; Tocher DA; Vickers M; Lancaster RW, Crystal Growth & Design 2016, 16(11), 6144-6147 |
| Energy model | 1 |
| Study_ID | 10 |
| Programs | Flexible CrystalPredictor (1.x), CrystalOptimizer (x), DMACRYS (2.0.4) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\2-chlorobenzamide_CPCO |
| Potential Description | CrystalOptimizer, GDMA2.2 (MP2/6-31G(d,p)) multipoles, MP2/6-31G(d,p) intra, FIT |
| Intramolecular Description | MP2/6-31G(d,p) |
|  |  |
| Search Identifier | B |
| Scientist | Anastasia Ntantou |
| Date | pre-2010 |
| Publication | Masters thesis only |
| Energy model | 1 |
| Study_ID | 0 |
| Programs | MOLPAK, DMAREL (4.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\2-chlorobenzamide |
| Potential Description | DMA + FIT + CL (DAY & PRICE 2003) |
| Intramolecular Description | MP2/6-31G(d,p) |
|  |  |
| Search Identifier | C |
| Scientist | Bob Lancaster |
| Date | pre-2010 |
| Publication | No publication planned |
| Energy model | 1 |
| Study_ID | 2 |
| Programs | MOLPAK, DMACRYS (1.1.1) |
| Location on S Drive | \\CHEMISTRY_CPOSS\\0-EarlySearches\\home\\louise_price.eminerals\\2-chlorobenzamide_BOB |
| Potential Description | DMA + FIT |
| Intramolecular Description | MP2/6-31G(d,p) |

![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/2chlorobenzamide_A1.png)![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/2chlorobenzamide_B1.png)![Embedded image](https://raw.githubusercontent.com/LouisePrice/CPOSS_Database/main/0.Landscapes/2chlorobenzamide_C1.png)

Figure .  Crystal energy landscape of 2-chlorobenzamide from previous work.  Top: from Study_ID=10.  Bottom left: from Study_ID=0.  Bottom right: from Study_ID=2.

# CSD structures (CSD version 6.01)

Table .  Crystallographic information for CSD entries for 2-chlorobenzamide.  Different polymorphs are coloured differently.

| REFCODE | space group | Z’ | a / Å | b / Å | c / Å | α / ° | β / ° | γ / ° | density / g cm<sup>-3</sup> | Form |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CLBZAM10 | P21/n | 1.0 | 14.127 | 10.683 | 5.051 | 90.0 | 90.2 | 90.0 | 1.3556 | alpha form |
| CLBZAM11 | P212121 | 1.0 | 14.0300 | 10.599 | 5.064 | 90.0 | 90.0 | 90.0 | 1.3723 | beta form |
| CLBZAM12 | P21/n | 1.0 | 5.05934 | 10.3235 | 14.2631 | 90.0 | 92.187 | 90.0 | 1.3881 | alpha form |
| CLBZAM13 | P212121 | 1.0 | 5.06073 | 10.3791 | 13.9351 | 90.0 | 90.0 | 90.0 | 1.4118 | beta form |

CLBZAM11 and CLBZAM13 are notionally the same form.  However Louise can’t overlay them in Mercury and they have different structure matches.  The are possibly enantiomers (needs more investigation, which I don’t have time for!).

Two other polymorphs of 2-chlorobenzamide are reported, CLBZAM02 gamma and CLBZMA03 delta.  Neither have space groups or full structures.

Table .  Experimental information for CSD entries for XXX.

| REFCODE | space group | R factor | T / K | Year | Comments |
| --- | --- | --- | --- | --- | --- |
| CLBZAM10 | P21/n | 9.700 | None | 1974 | 10.1107/S0567740874007801 |
| CLBZAM11 | P212121 | 6.5 | None | 1974 | 10.1107/S0567740874007801 |
| CLBZAM12 | P21/n | 3.0 | 150 K | 2016 | 10.1021/acs.cgd.6b00973 |
| CLBZAM13 | P212121 | 2.2 | 150 K | 2016 | 10.1021/acs.cgd.6b00973 |

Make this table include whether polymorphs are solution-grown, sublimation grown, templated or otherwise.  Add references.

# Other notes

There was no .pot file for CLBZAM Study_ID = 10.  The pote.dat files were compared for Bob’s search and Louise’s search, and differed only in the H_F2 ClF1 cross term.

| Bob’s search |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BUCK | H_F2 | H_F2 | 52.12899 | 0.214592 | 0.222819 | 0 | 70 |  |  |
| BUCK | ClF1 | ClF1 | 9583.58 | 0.2849 | 80.22445 | 0 | 70 |  |  |
| BUCK | ClF1 | H_F2 | 446.9519 | 0.214592 | 2.373693 | 0 | 70 |  |  |
| Louise’s search |  |  |  |  |  |  |  |  |  |
| BUCK | H_F2 | H_F2 | 52.12899 | 0.214592 | 0.222819 | 0 | 70 |  |  |
| BUCK | ClF1 | ClF1 | 9583.58 | 0.2849 | 80.22445 | 0 | 70 |  |  |
| BUCK | ClF1 | H_F2 | 706.8114 | 0.244798 | 4.227947 | 0 | 70 |  |  |
| Anastasia’s search |  |  |  |  |  |  |  |  |  |
| BUCK | HP | CODA | HP | CODA | 52.12899 | 0.214592 | 0.222819 | 0 | 70 |
| BUCK | CL | CODA | CL | CODA | 5905.001 | 0.299159 | 86.7168 | 0 | 70 |
| BUCK | CL | CODA | HP | CODA | 554.8123 | 0.256857 | 4.395825 | 0 | 70 |
| Cross potential from crosspot |  |  |  |  |  |  |  |  |  |
| BUCK | H_F2 | ClF1 | 706.8114 | 0.244798 | 4.227947 | 0 | 70 |  |  |
| Anastasia’s cross potential from crosspot |  |  |  |  |  |  |  |  |  |
| BUCK | H_F2 | ClF1 | 554.8168 | 0.249915 | 4.395697 | 0 | 70 |  |  |

The chlorine potential was different in the case of Anastasia’s search.  The cross term was consistent (within rounding errors in Excel).  The cross potential used by Bob’s search was wrong.
