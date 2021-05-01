import pinpy.domain.domain_finder as dof
import pinpy.sequence.amino_composition as ac
import pinpy.domain.domain_type as dt
import pinpy.linker.linker_finder as lf 
import pinpy.rcl.rcl_finder as rf 
import pinpy.rcl.rcl_residues as rs 
import pinpy.dsbond.dsbond_finder as dbf

# ac.calculate_amino_composition(
#     "PINIR_AminoSequences.xlsx", "PINIR_SequenceAminoComposition.csv")

# dof.find_domains_in_seq(
#     "PINIR_Domains.xlsx", "PINIR_Pin2Sequences.xlsx", "PINIR_SequencesDomains.csv")

# dt.identify_domain_type(
#     "PINIR_domainDetails.xlsx", "PINIR_domainDetails_domainType.csv")

# lf.find_linker_in_domain(
#     "PINIR_Domains.xlsx", "PINIR_Linkers.xlsx", "PINIR_DomainsLinker.csv")

# rf.find_rcl_in_domain(
#     "PINIR_Domains.xlsx", "PINIR_RCL.xlsx", "PINIR_DomainsRCL.csv")

# rs.identify_residues(
#     "PINIR_RCL.xlsx", "PINIR_RCL_residues.csv")

# dbf.find_disulphide_bonds(
#     "domainSequences.csv", "PINIR_domainDSBonds.csv")