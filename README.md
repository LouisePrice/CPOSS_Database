<html>

<link rel="stylesheet" href="0.MolecularDiagrams/cpossstyle.css" type="text/css" />
<link rel="shortcut icon" href="0.MolecularDiagrams/favicon.ico" />

<style>
table.searchATable { border-top-width : 1px;
    border-right-width : 1px;
    border-bottom-width : 1px;
    border-left-width : 1px;
    border: 1px;
    border-color: #010173;
    border-style : solid solid solid solid;
    width:100%;
    border-collapse: collapse; 
    border-spacing: 1px 1px;
    table-layout: fixed; }
</style>

# CPOSS_Database
This is the legacy repository for all CPOSS CSP landscapes.

## Instructions for use

These instructions were written for a specific purpose.  The user wanted the .cif files for two of the experimental forms of Succinic Acid.  This is how you would find them.

Go to https://github.com/LouisePrice/CPOSS_Database  Go to the SuccinicAcid folder.  Open and read the Word Document to see which search you want (I would recommend Search A, Energy Model 2, since it is what we published).  Go to SuccinicAcidA folder.  Download the 2.SuccinicAcidA_CrystOpt.zip file.  Open the spreadsheet within that.  The CSP data worksheet is the most useful, and there is a lookup table at the bottom for the experimental structures.  This will tell you that A23778, A4348 and A5136 are all the beta form, but the alpha form was not found in the search.  However, the experimental crystal structures were optimized with E1 being beta, E2 being alpha and E3 being gamma.  The same .zip file has all the crystal structures in as .res files.  You can easily convert them to .cif in Mercury.

I'm just going to try and write something with html to see if it works.

<table border="1"><tr><td bgcolor="red">This is supposed to be a red table cell</td></tr></table>

## Molecule Information

There will be a table, outlined in black, describing the general information about the molecule.

<table class="molTable"><tr><td>REFCODE</td><td>The refcode of the molecule will appear here</td><td>There will usually be a link to download the Word Document</td></tr></table>

## Search Information

Then there will be tables about the searches that were carried out.  Each search has a search identifier (A, B, C, etc.) and can have multiple energy models (1, 2, 3, etc.).  Different searches have different colour outlines, and different energy models are separated by horizontal rules.

<table class="searchATable"><tr><td>Search Identifier</td><td>A</td><td>There will usually be a <span class="blue">link</span> to the overall spreadsheet and the chemiscope file.</td></tr></table>

</html>
