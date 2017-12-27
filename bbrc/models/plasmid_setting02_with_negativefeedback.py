""" Rodrigo Santibanez @ Dlab-FCV (rsantibanez@dlab.cl); Version History
2016-10-13	Updated mechanism of RNase H: it cleaves and degrades 3'end of RNA Primer
			End of version v03 of the model
			
2016-10-07	Expression of RNA Primer with a linker to DNA Primer in the ori site: 
			Numbering links wit negative number (surprinsibgly) works
			Falloff works if the blocking agent is added to the rule:
			e.g. dna_primer(prot = None, rna = ANY, type = 'ori')
			Added RNase H activity and prototype of DNA PolIII activity
			
2016-10-05	Link "x" occurs only one time in the mixture = add the companion agent linked to it
			MATLAB Script now read a .py file and create rules based on DNA and RNA definition
			End of version v02 of the model
			
2016-10-05	Rules do the job, but them are not a biological mechanism
			
2016-10-04	Stills problems with falloff of RNAP when it encounter a RNA/DNA primer duplex
			
2016-10-03	Expression of RNA Primer coupled to link to the replication origin in the plasmid:
			doesn't works
			Rewrited agents: DNA and RNA agents have a dna, a prot, and a rna sites that binds
			to a dna, to a prot, and to a rna agent, respectively.
			Rewrited rules: linked RNA agents, as is specified by Kappa BioBrick Framework 
			(previuosly, rules created unlinked agents)
			Rewrited obs: Obs are linked DNA and RNA agents
			
2016-09-30	Fully functional Kappa BioBrick Rules
			Extended script now create Observables along with Initial DNA and RNA agents
		
2016-09-29	MATLAB Script reads a .kappa file looking for DNA and RNA agents and write 
			"%init:" agents that are linked and the corresponding "%var:"
			Rewrited agents: Now DNA and RNA agents have a binding site where rnap (or any 
			protein) binds to them
		
2016-09-28	Complete rules for RNA-I expression within Kappa BioBrick Framework 
			(doesn't replaces previous version v00)
			End of version v01 of the model
			
2016-09-27	Complete rules for RNA-I expression without link permutation 
			(doesn't follows Kappa BioBrick Framework)
			End of version v00 of the model
			
2016-09-23	Project Started
			References:
			Polisky 1988 Cell
			del Solar & Espinoza 2000 Molecular Microbiology
			Million-Weaver & Camps 2014 Plasmid
"""

from pysb import *
Model()

# DNA
Monomer('dna_i', ['dna', 'prot', 'rna', 'type', 'up', 'dw'], {'type': ['p1', 'ss5end', 'l1', 'l2', 'l3', 't1']})
Initial(dna_i(dna = None, prot = None, rna = None, type = 'p1', up = None, dw = None), Parameter('t0_dna_i_p1', 1))
Initial(dna_i(dna = None, prot = None, rna = None, type = 'ss5end', up = None, dw = None), Parameter('t0_dna_i_ss5end', 1))
Initial(dna_i(dna = None, prot = None, rna = None, type = 'l1', up = None, dw = None), Parameter('t0_dna_i_l1', 1))
Initial(dna_i(dna = None, prot = None, rna = None, type = 'l2', up = None, dw = None), Parameter('t0_dna_i_l2', 1))
Initial(dna_i(dna = None, prot = None, rna = None, type = 'l3', up = None, dw = None), Parameter('t0_dna_i_l3', 1))
Initial(dna_i(dna = None, prot = None, rna = None, type = 't1', up = None, dw = None), Parameter('t0_dna_i_t1', 1))
Observable('obs_dna_i_p1', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 'p1', up = WILD, dw = WILD))
Observable('obs_dna_i_ss5end', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 'ss5end', up = WILD, dw = WILD))
Observable('obs_dna_i_l1', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l1', up = WILD, dw = WILD))
Observable('obs_dna_i_l2', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l2', up = WILD, dw = WILD))
Observable('obs_dna_i_l3', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l3', up = WILD, dw = WILD))
Observable('obs_dna_i_t1', dna_i(dna = WILD, prot = WILD, rna = WILD, type = 't1', up = WILD, dw = WILD))

Monomer('dna_primer', ['dna', 'prot', 'rna', 'type', 'up', 'dw'], {'type': ['p1', 'l1', 'l2', 'a', 'ab', 'bg', 'pl5', 'l5', 'l6', 'l7', 'l8', 'ori', 'ss3end', 't1']})
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'p1', up = None, dw = None), Parameter('t0_dna_primer_p1', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l1', up = None, dw = None), Parameter('t0_dna_primer_l1', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l2', up = None, dw = None), Parameter('t0_dna_primer_l2', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'a', up = None, dw = None), Parameter('t0_dna_primer_alpha', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'ab', up = None, dw = None), Parameter('t0_dna_primer_alpha_beta', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'bg', up = None, dw = None), Parameter('t0_dna_primer_beta_gamma', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'pl5', up = None, dw = None), Parameter('t0_dna_primer_prel5', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l5', up = None, dw = None), Parameter('t0_dna_primer_l5', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l6', up = None, dw = None), Parameter('t0_dna_primer_l6', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l7', up = None, dw = None), Parameter('t0_dna_primer_l7', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'l8', up = None, dw = None), Parameter('t0_dna_primer_l8', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'ori', up = None, dw = None), Parameter('t0_dna_primer_O', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 'ss3end', up = None, dw = None), Parameter('t0_dna_primer_ss3end', 1))
Initial(dna_primer(dna = None, prot = None, rna = None, type = 't1', up = None, dw = None), Parameter('t0_dna_primer_t1', 1))
Observable('obs_dna_primer_p1', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'p1', up = WILD, dw = WILD))
Observable('obs_dna_primer_l1', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l1', up = WILD, dw = WILD))
Observable('obs_dna_primer_l2', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l2', up = WILD, dw = WILD))
Observable('obs_dna_primer_a', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'a', up = WILD, dw = WILD))
Observable('obs_dna_primer_ab', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ab', up = WILD, dw = WILD))
Observable('obs_dna_primer_bg', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'bg', up = WILD, dw = WILD))
Observable('obs_dna_primer_pl5', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'pl5', up = WILD, dw = WILD))
Observable('obs_dna_primer_l5', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l5', up = WILD, dw = WILD))
Observable('obs_dna_primer_l6', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l6', up = WILD, dw = WILD))
Observable('obs_dna_primer_7', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l7', up = WILD, dw = WILD))
Observable('obs_dna_primer_l8', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l8', up = WILD, dw = WILD))
Observable('obs_dna_primer_ori', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ori', up = WILD, dw = WILD))
Observable('obs_dna_primer_ss3end', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ss3end', up = WILD, dw = WILD))
Observable('obs_dna_primer_t1', dna_primer(dna = WILD, prot = WILD, rna = WILD, type = 't1', up = WILD, dw = WILD))

# RNA
Monomer('rna_i', ['dna', 'prot', 'rna', 'type', 'up', 'dw'], {'type': ['ss5end', 'l1', 'l2', 'l3']})
Initial(rna_i(dna = None, prot = None, rna = None, type = 'ss5end', up = None, dw = None), Parameter('t0_rna_i_ss5end', 0))
Initial(rna_i(dna = None, prot = None, rna = None, type = 'l1', up = None, dw = None), Parameter('t0_rna_i_l1', 0))
Initial(rna_i(dna = None, prot = None, rna = None, type = 'l2', up = None, dw = None), Parameter('t0_rna_i_l2', 0))
Initial(rna_i(dna = None, prot = None, rna = None, type = 'l3', up = None, dw = None), Parameter('t0_rna_i_l3', 0))
Observable('obs_rna_i_ss5end', rna_i(dna = WILD, prot = WILD, rna = WILD, type = 'ss5end', up = WILD, dw = WILD))
Observable('obs_rna_i_l1', rna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l1', up = WILD, dw = WILD))
Observable('obs_rna_i_l2', rna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l2', up = WILD, dw = WILD))
Observable('obs_rna_i_l3', rna_i(dna = WILD, prot = WILD, rna = WILD, type = 'l3', up = WILD, dw = WILD))

Monomer('rna_primer', ['dna', 'prot', 'rna', 'type', 'up', 'dw'], {'type': ['l1', 'l2', 'a', 'ab', 'bg', 'pl5', 'l5', 'l6', 'l7', 'l8', 'ori', 'ss3end']})
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l1', up = None, dw = None), Parameter('t0_rna_primer_l1', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l2', up = None, dw = None), Parameter('t0_rna_primer_l2', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'a', up = None, dw = None), Parameter('t0_rna_primer_a', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'ab', up = None, dw = None), Parameter('t0_rna_primer_ab', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'bg', up = None, dw = None), Parameter('t0_rna_primer_bg', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'pl5', up = None, dw = None), Parameter('t0_rna_primer_pl5', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l5', up = None, dw = None), Parameter('t0_rna_primer_l5', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l6', up = None, dw = None), Parameter('t0_rna_primer_l6', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l7', up = None, dw = None), Parameter('t0_rna_primer_l7', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'l8', up = None, dw = None), Parameter('t0_rna_primer_l8', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'ori', up = None, dw = None), Parameter('t0_rna_primer_ori', 0))
Initial(rna_primer(dna = None, prot = None, rna = None, type = 'ss3end', up = None, dw = None), Parameter('t0_rna_primer_ss3end', 0))
Observable('obs_rna_primer_l1', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l1', up = WILD, dw = WILD))
Observable('obs_rna_primer_l2', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l2', up = WILD, dw = WILD))
Observable('obs_rna_primer_a', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'a', up = WILD, dw = WILD))
Observable('obs_rna_primer_ab', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ab', up = WILD, dw = WILD))
Observable('obs_rna_primer_bg', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'bg', up = WILD, dw = WILD))
Observable('obs_rna_primer_pl5', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'pl5', up = WILD, dw = WILD))
Observable('obs_rna_primer_l5', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l5', up = WILD, dw = WILD))
Observable('obs_rna_primer_l6', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l6', up = WILD, dw = WILD))
Observable('obs_rna_primer_l7', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l7', up = WILD, dw = WILD))
Observable('obs_rna_primer_l8', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'l8', up = WILD, dw = WILD))
Observable('obs_rna_primer_ori', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ori', up = WILD, dw = WILD))
Observable('obs_rna_primer_ss3end', rna_primer(dna = WILD, prot = WILD, rna = WILD, type = 'ss3end', up = WILD, dw = WILD))

# Protein and Protein-complex agents
Monomer('cplx_pol3', ['dna', 'rna'])
Initial(cplx_pol3(dna = None, rna = None), Parameter('t0_cplx_pol3', 1))

Monomer('cplx_rnap', ['dna', 'prot', 'rna'])
Initial(cplx_rnap(dna = None, prot = None, rna = None), Parameter('t0_cplx_rnap', 2))

Monomer('prot_rnha', ['dna', 'rna'])
Initial(prot_rnha(dna = None, rna = None), Parameter('t0_prot_rnha', 1))

# DNA Transcription
Rule('docking_rnap_dna_i_p1',
	cplx_rnap(dna = None) + dna_i(prot = None, type = 'p1') != 
	cplx_rnap(dna = 1) + dna_i(prot = 1, type = 'p1'),
	Parameter('fwd_docking_rnap_dna_i_p1', 1),
	Parameter('rvs_docking_rnap_dna_i_p1', 1))

Rule('sliding_rnap_dna_i_ss5end',
	cplx_rnap(dna = 1, rna = None) + dna_i(prot = 1, type = 'p1') + dna_i(prot = None, type = 'ss5end') >>
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = None, type = 'p1') + dna_i(prot = 1, type = 'ss5end') + rna_i(prot = 3, type = 'ss5end'),
	Parameter('fwd_sliding_rnap_dna_i_ss5end', 1))

Rule('sliding_rnap_dna_i_l1',
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = 1, type = 'ss5end') + dna_i(prot = None, type = 'l1') + rna_i(prot = 3, type = 'ss5end', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = None, type = 'ss5end') + dna_i(prot = 1, type = 'l1') + rna_i(prot = None, type = 'ss5end', dw = 4) + rna_i(prot = 3, type = 'l1', up = 4),
	Parameter('fwd_sliding_rnap_dna_i_l1', 1))

Rule('sliding_rnap_dna_i_l2',
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = 1, type = 'l1') + dna_i(prot = None, type = 'l2') + rna_i(prot = 3, type = 'l1', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = None, type = 'l1') + dna_i(prot = 1, type = 'l2') + rna_i(prot = None, type = 'l1', dw = 4) + rna_i(prot = 3, type = 'l2', up = 4),
	Parameter('fwd_sliding_rnap_dna_i_l2', 1))

Rule('sliding_rnap_dna_i_l3',
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = 1, type = 'l2') + dna_i(prot = None, type = 'l3') + rna_i(prot = 3, type = 'l2', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = None, type = 'l2') + dna_i(prot = 1, type = 'l3') + rna_i(prot = None, type = 'l2', dw = 4) + rna_i(prot = 3, type = 'l3', up = 4),
	Parameter('fwd_sliding_rnap_dna_i_l3', 1))

Rule('sliding_rnap_dna_i_t1',
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = 1, type = 'l3') + dna_i(prot = None, type = 't1') + rna_i(prot = 3, type = 'l3') >>
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = None, type = 'l3') + dna_i(prot = 1, type = 't1') + rna_i(prot = 3, type = 'l3'),
	Parameter('fwd_sliding_rnap_dna_i_t1', 1))

Rule('falloff_rnap_dna_i_t1',
	cplx_rnap(dna = 1, rna = 3) + dna_i(prot = 1, type = 't1') + rna_i(prot = 3, type = 'l3') >>
	cplx_rnap(dna = None, rna = None) + dna_i(prot = None, type = 't1') + rna_i(prot = None, type = 'l3'),
	Parameter('fwd_falloff_rnap_dna_i_t1', 1))

Rule('docking_rnap_dna_primer_p1',
	cplx_rnap(dna = None) + dna_primer(prot = None, type = 'p1') != 
	cplx_rnap(dna = 1) + dna_primer(prot = 1, type = 'p1'),
	Parameter('fwd_docking_rnap_dna_primer_p1', 1),
	Parameter('rvs_docking_rnap_dna_primer_p1', 1))

Rule('sliding_rnap_dna_primer_l1',
	cplx_rnap(dna = 1, rna = None) + dna_primer(prot = 1, type = 'p1') + dna_primer(prot = None, type = 'l1') >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'p1') + dna_primer(prot = 1, type = 'l1') + rna_primer(prot = 3, type = 'l1'),
	Parameter('fwd_sliding_rnap_dna_primer_l1', 1))

Rule('sliding_rnap_dna_primer_l2',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l1') + dna_primer(prot = None, type = 'l2') + rna_primer(prot = 3, type = 'l1', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l1') + dna_primer(prot = 1, type = 'l2') + rna_primer(prot = None, type = 'l1', dw = 4) + rna_primer(prot = 3, type = 'l2', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_l2', 1))

Rule('sliding_rnap_dna_primer_alpha',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l2') + dna_primer(prot = None, type = 'a') + rna_primer(prot = 3, type = 'l2', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l2') + dna_primer(prot = 1, type = 'a') + rna_primer(prot = None, type = 'l2', dw = 4) + rna_primer(prot = 3, type = 'a', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_alpha', 1))

Rule('sliding_rnap_dna_primer_alpha_beta',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'a') + dna_primer(prot = None, type = 'ab') + rna_primer(prot = 3, type = 'a', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'a') + dna_primer(prot = 1, type = 'ab') + rna_primer(prot = None, type = 'a', dw = 4) + rna_primer(prot = 3, type = 'ab', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_alpha_beta', 1))

Rule('sliding_rnap_dna_primer_beta_gamma',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'ab') + dna_primer(prot = None, type = 'bg') + rna_primer(prot = 3, type = 'ab', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'ab') + dna_primer(prot = 1, type = 'bg') + rna_primer(prot = None, type = 'ab', dw = 4) + rna_primer(prot = 3, type = 'bg', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_beta_gamma', 1))

Rule('sliding_rnap_dna_primer_prel5',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'bg') + dna_primer(prot = None, type = 'pl5') + rna_primer(prot = 3, type = 'bg', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'bg') + dna_primer(prot = 1, type = 'pl5') + rna_primer(prot = None, type = 'bg', dw = 4) + rna_primer(prot = 3, type = 'pl5', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_prel5', 1))

Rule('sliding_rnap_dna_primer_l5',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'pl5') + dna_primer(prot = None, type = 'l5') + rna_primer(prot = 3, type = 'pl5', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'pl5') + dna_primer(prot = 1, type = 'l5') + rna_primer(prot = None, type = 'pl5', dw = 4) + rna_primer(prot = 3, type = 'l5', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_l5', 1))

Rule('sliding_rnap_dna_primer_l6',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l5') + dna_primer(prot = None, type = 'l6') + rna_primer(prot = 3, type = 'l5', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l5') + dna_primer(prot = 1, type = 'l6') + rna_primer(prot = None, type = 'l5', dw = 4) + rna_primer(prot = 3, type = 'l6', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_l6', 1))

Rule('sliding_rnap_dna_primer_l7',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l6') + dna_primer(prot = None, type = 'l7') + rna_primer(prot = 3, type = 'l6', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l6') + dna_primer(prot = 1, type = 'l7') + rna_primer(prot = None, type = 'l6', dw = 4) + rna_primer(prot = 3, type = 'l7', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_l7', 1))

Rule('sliding_rnap_dna_primer_l8',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l7') + dna_primer(prot = None, type = 'l8') + rna_primer(prot = 3, type = 'l7', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l7') + dna_primer(prot = 1, type = 'l8') + rna_primer(prot = None, type = 'l7', dw = 4) + rna_primer(prot = 3, type = 'l8', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_l8', 1))

Rule('sliding_rnap_dna_primer_ori',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l8') + dna_primer(prot = None, rna = None, type = 'ori') + rna_primer(prot = 3, type = 'l8', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'l8') + dna_primer(prot = 1, rna = 5, type = 'ori') + rna_primer(prot = None, type = 'l8', dw = 4) + rna_primer(dna = 5, prot = 3, type = 'ori', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_ori', 1))

Rule('sliding_rnap_dna_primer_ss3end',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'ori') + dna_primer(prot = None, type = 'ss3end') + rna_primer(prot = 3, type = 'ori', dw = None) >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'ori') + dna_primer(prot = 1, type = 'ss3end') + rna_primer(prot = None, type = 'ori', dw = 4) + rna_primer(prot = 3, type = 'ss3end', up = 4),
	Parameter('fwd_sliding_rnap_dna_primer_ss3end', 1))

Rule('sliding_rnap_dna_primer_t1',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'ss3end') + dna_primer(prot = None, type = 't1') + rna_primer(prot = 3, type = 'ss3end') >>
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = None, type = 'ss3end') + dna_primer(prot = 1, type = 't1') + rna_primer(prot = 3, type = 'ss3end'),
	Parameter('fwd_sliding_rnap_dna_primer_t1', 1))

Rule('falloff_rnap_dna_primer_t1',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 't1') + rna_primer(prot = 3, type = 'ss3end') >>
	cplx_rnap(dna = None, rna = None) + dna_primer(prot = None, type = 't1') + rna_primer(prot = None, type = 'ss3end'),
	Parameter('fwd_falloff_rnap_dna_primer_t1', 1))

# Falloff of RNAP from DNA Primer if the site ori of DNA Primer is blocked
Rule('falloff_rnap_dna_primer_l8',
	cplx_rnap(dna = 1, rna = 3) + dna_primer(prot = 1, type = 'l8') + dna_primer(prot = ANY, rna = ANY, type = 'ori') + rna_primer(prot = 3, type = 'l8') >>
	cplx_rnap(dna = None, rna = None) + dna_primer(prot = None, type = 'l8') + dna_primer(prot = ANY, rna = ANY, type = 'ori') + rna_primer(prot = None, type = 'l8'),
	Parameter('fwd_falloff_rnap_dna_primer_l8', 1))

# RNA I - RNA Primer duplex
Rule('rna_rna_duplex',
	dna_primer(prot = None, rna = 1, type = 'ori') + rna_primer(dna = 1, prot = None, rna = None, type = 'ori') + rna_i(prot = None, rna = None, type = 'l3') >>
	dna_primer(prot = None, rna = None, type = 'ori') + rna_primer(dna = None, prot = None, rna = 2, type = 'ori') + rna_i(prot = None, rna = 2, type = 'l3'),
	Parameter('fwd_rna_rna_duplex', 1))

# DNA replication
Rule('docking_rnha_rna_primer_ori',
	prot_rnha(dna = None, rna = None) + dna_primer(prot = None, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = None, type = 'ori') !=
	prot_rnha(dna = 1, rna = 3) + dna_primer(prot = 1, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = 3, type = 'ori'),
	Parameter('fwd_docking_rnha_rna_primer_ori', 1),
	Parameter('rvs_docking_rnha_rna_primer_ori', 1))

Rule('rna_primer_cleavage',
	prot_rnha(dna = 1, rna = 3) + dna_primer(prot = 1, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = 3, type = 'ori', dw = 5) + rna_primer(prot = None, type = 'ss3end', up = 5) >> 
	prot_rnha(dna = None, rna = 3) + dna_primer(prot = None, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = None, type = 'ori', dw = None) + rna_primer(prot = 3, type = 'ss3end', up = None),
	Parameter('fwd_rna_primer_cleavage', 1))

Rule('deg_rna_primer_ss3end',
	prot_rnha(rna  = 3) + rna_primer(prot = 3, type = 'ss3end', up = None) >>
	prot_rnha(rna = None),
	Parameter('fwd_deg_rna_primer_ss3end', 1))

Rule('docking_pol3_dna_primer',
	cplx_pol3(dna = None, rna = None) + dna_primer(prot = None, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = None, type = 'ori', dw = None) !=
	cplx_pol3(dna = 1, rna = 3) + dna_primer(prot = 1, rna = 4, type = 'ori') + rna_primer(dna = 4, prot = 3, type = 'ori', dw = None),
	Parameter('fwd_docking_pol3_dna_primer_ori', 1),
	Parameter('rvs_docking_pol3_dna_primer_ori', 1))

gene_i = dna_i(type = 'p1') % dna_i(type = 'ss5end') % dna_i(type = 'l1') % dna_i(type = 'l2') % dna_i(type = 'l3') % dna_i(type = 't1')

gene_primer = dna_primer(type = 'p1') % dna_primer(type = 'l1') % dna_primer(type = 'l2') % dna_primer(type = 'a') % dna_primer(type = 'ab') % dna_primer(type = 'bg') % dna_primer(type = 'pl5') % dna_primer(type = 'l5') % dna_primer(type = 'l6') % dna_primer(type = 'l7') % dna_primer(type = 'l8') % dna_primer(type = 'ori') % dna_primer(type = 'ss3end') % dna_primer(type = 't1')

Rule('dna_replication',
	cplx_pol3(dna = 1, rna = 3) + dna_primer(prot = 1, rna = 2, type = 'ori') + rna_primer(dna = 2, prot = 3, type = 'ori', dw = None) >>
	cplx_pol3(dna = None, rna = None) + dna_primer(prot = None, rna = None, type = 'ori') + gene_i + gene_primer,
	Parameter('fwd_dna_replication', 1))
