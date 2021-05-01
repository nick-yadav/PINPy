# PINPy
PINPy is a collection of Python code used for data processing for the development of a novel specialized database of Potato Type Inhibitor-II family PIs (Pin-II type PIs) plant protease inhibitors. The database, together with the web-based information system, is called PINIR (**Pin**-II type PIs **I**nformation **R**esource) and can be accessed using following web-link.

**Database URL :**[https://pinir.ncl.res.in/](https://pinir.ncl.res.in/)

It consist of following programs:

1. **DomainFinder.py:** This program indentifies which Domains are found in a Sequence and what are their location i.e. it's start and end position.
2. **DomainTypeIdentifier.py:** This program based upon Linker organization in IRD's (Domains) identifies the Domain Type
3. **DSBondFinder.py:** This program finds the probable Di-Sulphide Bonds in the available Domain sequences.
4. **LinkerFinder.py:** This program finds which Linker is found in a Domain and what is its location i.e. it's start and end position.
5. **RclFinder.py:** This this program finds which RCL is found in a Domain and what is its location i.e. it's start and end position.
6. **RclResidueIdentifier.py:** This program identifies the Residues at P1, P2 and P1` position in an RCL.
7. **SequenceAminoComposition.py:** This program finds the Amino Acids composition of Amino Acid Sequences. These Amino Acid sequences can be PI sequences or Domain sequences. It gives each Amino Acid's count and percentage in the sequences.
