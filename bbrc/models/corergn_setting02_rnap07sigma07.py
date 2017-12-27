from pysb import ANY, WILD, Model, Monomer, Parameter, Expression, Initial, Observable, Rule
from pysb.macros import *

Model()

###################################################################################################
# DNA
Monomer('DNA_rpoA', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoA(type = 'P1'), Parameter('t0_DNA_rpoA_P1', 1))
Initial(DNA_rpoA(type = 'RBS'), Parameter('t0_DNA_rpoA_RBS', 1))
Initial(DNA_rpoA(type = 'CDS'), Parameter('t0_DNA_rpoA_CDS', 1))
Initial(DNA_rpoA(type = 'T1'), Parameter('t0_DNA_rpoA_T1', 1))

Monomer('DNA_rpoB', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoB(type = 'P1'), Parameter('t0_DNA_rpoB_P1', 1))
Initial(DNA_rpoB(type = 'RBS'), Parameter('t0_DNA_rpoB_RBS', 1))
Initial(DNA_rpoB(type = 'CDS'), Parameter('t0_DNA_rpoB_CDS', 1))

Monomer('DNA_rpoC', ['type'], {'type': ['RBS', 'CDS', 'T1']})
Initial(DNA_rpoC(type = 'RBS'), Parameter('t0_DNA_rpoC_RBS', 1))
Initial(DNA_rpoC(type = 'CDS'), Parameter('t0_DNA_rpoC_CDS', 1))
Initial(DNA_rpoC(type = 'T1'), Parameter('t0_DNA_rpoC_T1', 1))

Monomer('DNA_rpoD', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoD(type = 'P1'), Parameter('t0_DNA_rpoD_P1', 1))
Initial(DNA_rpoD(type = 'RBS'), Parameter('t0_DNA_rpoD_RBS', 1))
Initial(DNA_rpoD(type = 'CDS'), Parameter('t0_DNA_rpoD_CDS', 1))
Initial(DNA_rpoD(type = 'T1'), Parameter('t0_DNA_rpoD_T1', 1))

Monomer('DNA_rpoE', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoE(type = 'P1'), Parameter('t0_DNA_rpoE_P1', 1))
Initial(DNA_rpoE(type = 'RBS'), Parameter('t0_DNA_rpoE_RBS', 1))
Initial(DNA_rpoE(type = 'CDS'), Parameter('t0_DNA_rpoE_CDS', 1))
Initial(DNA_rpoE(type = 'T1'), Parameter('t0_DNA_rpoE_T1', 1))

Monomer('DNA_rpoH', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoH(type = 'P1'), Parameter('t0_DNA_rpoH_P1', 1))
Initial(DNA_rpoH(type = 'RBS'), Parameter('t0_DNA_rpoH_RBS', 1))
Initial(DNA_rpoH(type = 'CDS'), Parameter('t0_DNA_rpoH_CDS', 1))
Initial(DNA_rpoH(type = 'T1'), Parameter('t0_DNA_rpoH_T1', 1))

Monomer('DNA_fliA', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_fliA(type = 'P1'), Parameter('t0_DNA_fliA_P1', 1))
Initial(DNA_fliA(type = 'RBS'), Parameter('t0_DNA_fliA_RBS', 1))
Initial(DNA_fliA(type = 'CDS'), Parameter('t0_DNA_fliA_CDS', 1))
Initial(DNA_fliA(type = 'T1'), Parameter('t0_DNA_fliA_T1', 1))

Monomer('DNA_rpoN', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoN(type = 'P1'), Parameter('t0_DNA_rpoN_P1', 1))
Initial(DNA_rpoN(type = 'RBS'), Parameter('t0_DNA_rpoN_RBS', 1))
Initial(DNA_rpoN(type = 'CDS'), Parameter('t0_DNA_rpoN_CDS', 1))
Initial(DNA_rpoN(type = 'T1'), Parameter('t0_DNA_rpoN_T1', 1))

Monomer('DNA_rpoS', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_rpoS(type = 'P1'), Parameter('t0_DNA_rpoS_P1', 1))
Initial(DNA_rpoS(type = 'RBS'), Parameter('t0_DNA_rpoS_RBS', 1))
Initial(DNA_rpoS(type = 'CDS'), Parameter('t0_DNA_rpoS_CDS', 1))
Initial(DNA_rpoS(type = 'T1'), Parameter('t0_DNA_rpoS_T1', 1))

Monomer('DNA_fecI', ['type'], {'type': ['P1', 'RBS', 'CDS', 'T1']})
Initial(DNA_fecI(type = 'P1'), Parameter('t0_DNA_fecI_P1', 1))
Initial(DNA_fecI(type = 'RBS'), Parameter('t0_DNA_fecI_RBS', 1))
Initial(DNA_fecI(type = 'CDS'), Parameter('t0_DNA_fecI_CDS', 1))
Initial(DNA_fecI(type = 'T1'), Parameter('t0_DNA_fecI_T1', 1))

###################################################################################################
# RNA
Monomer('RNA_rpoA', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoA(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoA_RBS', 186))      # Recuerda dividir todo por 10
Initial(RNA_rpoA(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoA_CDS', 186))
Observable('rpoA_RNA', RNA_rpoA(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoB', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoB(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoB_RBS', 60))
Initial(RNA_rpoB(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoB_CDS', 60))
Observable('rpoB_RNA', RNA_rpoB(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoC', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoC(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoC_RBS', 72))
Initial(RNA_rpoC(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoC_CDS', 72))
Observable('rpoC_RNA', RNA_rpoC(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoD', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoD(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoD_RBS', 68))
Initial(RNA_rpoD(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoD_CDS', 68))
Observable('rpoD_RNA', RNA_rpoD(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoE', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoE(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoE_RBS', 64))
Initial(RNA_rpoE(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoE_CDS', 64))
Observable('rpoE_RNA', RNA_rpoE(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoH', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoH(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoH_RBS', 55))
Initial(RNA_rpoH(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoH_CDS', 55))
Observable('rpoH_RNA', RNA_rpoH(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_fliA', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_fliA(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_fliA_RBS', 69))
Initial(RNA_fliA(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_fliA_CDS', 69))
Observable('fliA_RNA', RNA_fliA(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoN', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoN(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoN_RBS', 45))
Initial(RNA_rpoN(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoN_CDS', 45))
Observable('rpoN_RNA', RNA_rpoN(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_rpoS', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_rpoS(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_rpoS_RBS', 46))
Initial(RNA_rpoS(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_rpoS_CDS', 46))
Observable('rpoS_RNA', RNA_rpoS(type = 'CDS', up = WILD, dw = WILD))

Monomer('RNA_fecI', ['type', 'up', 'dw'], {'type': ['RBS', 'CDS']})
Initial(RNA_fecI(type = 'RBS', up = None, dw = None), Parameter('t0_RNA_fecI_RBS', 15))
Initial(RNA_fecI(type = 'CDS', up = None, dw = None), Parameter('t0_RNA_fecI_CDS', 15))
Observable('fecI_RNA', RNA_fecI(type = ('CDS', WILD), up = WILD, dw = WILD))

###################################################################################################
#Proteins
Monomer('Prot_rpoA', ['PBD_01', 'PBD_02'])
Initial(Prot_rpoA(PBD_01 = None, PBD_02 = None), Parameter('t0_Prot_rpoA', 14))
Observable('rpoA_Prot', Prot_rpoA(PBD_01 = WILD, PBD_02 = WILD))

Monomer('Prot_rpoB', ['PBD_01', 'PBD_02'])
Initial(Prot_rpoB(PBD_01 = None, PBD_02 = None), Parameter('t0_Prot_rpoB', 7))
Observable('rpoB_Prot', Prot_rpoB(PBD_01 = WILD, PBD_02 = WILD))

Monomer('Prot_rpoC', ['PBD_01', 'PBD_02'])
Initial(Prot_rpoC(PBD_01 = None, PBD_02 = None), Parameter('t0_Prot_rpoC', 7))
Observable('rpoC_Prot', Prot_rpoC(PBD_01 = WILD, PBD_02 = WILD))

Monomer('Prot_rpoD', ['PBD_01'])
Initial(Prot_rpoD(PBD_01 = None), Parameter('t0_Prot_rpoD', 1))
Observable('rpoD_Prot', Prot_rpoD(PBD_01 = None))

Monomer('Prot_rpoE', ['PBD_01'])
Initial(Prot_rpoE(PBD_01 = None), Parameter('t0_Prot_rpoE', 1))
Observable('rpoE_Prot', Prot_rpoE(PBD_01 = None))

Monomer('Prot_rpoH', ['PBD_01'])
Initial(Prot_rpoH(PBD_01 = None), Parameter('t0_Prot_rpoH', 1))
Observable('rpoH_Prot', Prot_rpoH(PBD_01 = None))

Monomer('Prot_fliA', ['PBD_01'])
Initial(Prot_fliA(PBD_01 = None), Parameter('t0_Prot_fliA', 1))
Observable('fliA_Prot', Prot_fliA(PBD_01 = None))

Monomer('Prot_rpoN', ['PBD_01'])
Initial(Prot_rpoN(PBD_01 = None), Parameter('t0_Prot_rpoN', 1))
Observable('rpoN_Prot', Prot_rpoN(PBD_01 = None))

Monomer('Prot_rpoS', ['PBD_01'])
Initial(Prot_rpoS(PBD_01 = None), Parameter('t0_Prot_rpoS', 1))
Observable('rpoS_Prot', Prot_rpoS(PBD_01 = None))

Monomer('Prot_fecI', ['PBD_01'])
Initial(Prot_fecI(PBD_01 = None), Parameter('t0_Prot_fecI', 1))
Observable('fecI_Prot', Prot_fecI(PBD_01 = None))

###################################################################################################
#Protein Complexes
Monomer('RNAP', ['DBD_01', 'PBD_01', 'RBD_01'])
Initial(RNAP(DBD_01 = None, PBD_01 = None, RBD_01 = None), Parameter('t0_RNAP', 0))
Observable('RNAP_cplx', RNAP(DBD_01 = None, PBD_01 = ANY, RBD_01 = None))

Monomer('R30S', ['PBD_01', 'RBD_01'])
Initial(R30S(PBD_01 = None, RBD_01 = None), Parameter('t0_R30S', 1))
Observable('R30S_cplx', R30S(PBD_01 = WILD, RBD_01 = WILD))

Monomer('R50S', ['PBD_01', 'PBD_02'])
Initial(R50S(PBD_01 = None, PBD_02 = None), Parameter('t0_R50S', 1))
Observable('R50S_cplx', R50S(PBD_01 = WILD, PBD_02 = WILD))

###################################################################################################
#Protein Aliases (free proteins and protein-only complexes)
free_rpoa = Prot_rpoA(PBD_01 = None, PBD_02 = None)
free_rpob = Prot_rpoB(PBD_01 = None, PBD_02 = None)
free_rpoc = Prot_rpoC(PBD_01 = None, PBD_02 = None)

free_rpod = Prot_rpoD(PBD_01 = None)
free_rpoe = Prot_rpoE(PBD_01 = None)
free_rpoh = Prot_rpoH(PBD_01 = None)
free_flia = Prot_fliA(PBD_01 = None)
free_rpon = Prot_rpoN(PBD_01 = None)
free_rpos = Prot_rpoS(PBD_01 = None)
free_feci = Prot_fecI(PBD_01 = None)

cplx_rnap = RNAP(DBD_01 = None, PBD_01 = None, RBD_01 = None)
cplx_R30S = R30S(PBD_01 = None, RBD_01 = None)
cplx_R50S = R50S(PBD_01 = None, PBD_02 = None)

###################################################################################################
#RNA Pol Assembly (Ishihama81, Sequential Assembly: Two RpoA; Then RpoB; Then RpoC; Then a Sigma Factor)
cplx_rpoa_rpoa           = Prot_rpoA(PBD_01 = 1, PBD_02 = None) % Prot_rpoA(PBD_01 = None, PBD_02 = 1)
cplx_rpoa_rpoa_rpob      = Prot_rpoA(PBD_01 = 1, PBD_02 = 2) % Prot_rpoA(PBD_01 = None, PBD_02 = 1) % Prot_rpoB(PBD_01 = 2, PBD_02 = None)
cplx_rpoa_rpoa_rpob_rpoc = Prot_rpoA(PBD_01 = 1, PBD_02 = 2) % Prot_rpoA(PBD_01 = 3, PBD_02 = 1) % Prot_rpoB(PBD_01 = 2, PBD_02 = 4) % Prot_rpoC(PBD_01 = 3, PBD_02 = 4)

cplx_rnap70 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2)
cplx_rnap24 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_rpoE(PBD_01 = 2)
cplx_rnap32 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_rpoH(PBD_01 = 2)
cplx_rnap28 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_fliA(PBD_01 = 2)
cplx_rnap54 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_rpoN(PBD_01 = 2)
cplx_rnap38 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2)
cplx_rnap19 = RNAP(DBD_01 = None, PBD_01 = 2, RBD_01 = None) % Prot_fecI(PBD_01 = 2)

Rule('rpoa_rpoa', free_rpoa + free_rpoa != cplx_rpoa_rpoa,
     Parameter('rpoa_rpoa_fwd', 1),
     Parameter('rpoa_rpoa_rvs', 1))

Rule('rpoa_rpoa_rpob', free_rpob + cplx_rpoa_rpoa != cplx_rpoa_rpoa_rpob,
     Parameter('rpoa_rpoa_rpob_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc', free_rpoc + cplx_rpoa_rpoa_rpob != cplx_rpoa_rpoa_rpob_rpoc + cplx_rnap,
     Parameter('rpoa_rpoa_rpob_rpoc_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_rpod', cplx_rnap + free_rpod != cplx_rnap70,
     Parameter('rpoa_rpoa_rpob_rpoc_rpod_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rpod_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_rpoe', cplx_rnap + free_rpoe != cplx_rnap24,
     Parameter('rpoa_rpoa_rpob_rpoc_rpoe_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rpoe_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_rpoh', cplx_rnap + free_rpoh != cplx_rnap32,
     Parameter('rpoa_rpoa_rpob_rpoc_rpoh_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rpoh_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_flia', cplx_rnap + free_flia != cplx_rnap28,
     Parameter('rpoa_rpoa_rpob_rpoc_flia_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_flia_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_rpon', cplx_rnap + free_rpon != cplx_rnap54,
     Parameter('rpoa_rpoa_rpob_rpoc_rpon_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rpon_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_rpos', cplx_rnap + free_rpos != cplx_rnap38,
     Parameter('rpoa_rpoa_rpob_rpoc_rpos_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_rpos_rvs', 1))

Rule('rpoa_rpoa_rpob_rpoc_feci', cplx_rnap + free_feci != cplx_rnap19,
     Parameter('rpoa_rpoa_rpob_rpoc_feci_fwd', 1),
     Parameter('rpoa_rpoa_rpob_rpoc_feci_rvs', 1))

###################################################################################################
#DNA Transcription
#kappa rules for rpoA transcription
Rule('docking_rnap70_p1rpoa',
     cplx_rnap70 + DNA_rpoA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoA(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpoa_fwd', 1),
     Parameter('docking_rnap70_p1rpoa_rvs', 1))

Rule('sliding_rnap70_rbsrpoa',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoA(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('RBS', 1)) % RNA_rpoA(type = 'RBS', up = None, dw = 3) + DNA_rpoA(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpoa_fwd', 1))

Rule('docking_rnap32_p1rpoa',
     cplx_rnap32 + DNA_rpoA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoH(PBD_01 = 2) % DNA_rpoA(type = ('P1', 1)),
     Parameter('docking_rnap32_p1rpoa_fwd', 1),
     Parameter('docking_rnap32_p1rpoa_rvs', 1))

Rule('sliding_rnap32_rbsrpoa',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoA(type = ('P1', 1)) % Prot_rpoH(PBD_01 = 2) + DNA_rpoA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('RBS', 1)) % RNA_rpoA(type = 'RBS', up = None, dw = 3) + DNA_rpoA(type = 'P1') + free_rpoh,
     Parameter('sliding_rnap32_rbsrpoa_fwd', 1))

Rule('docking_rnap54_p1rpoa',
     cplx_rnap54 + DNA_rpoA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoN(PBD_01 = 2) % DNA_rpoA(type = ('P1', 1)),
     Parameter('docking_rnap54_p1rpoa_fwd', 1),
     Parameter('docking_rnap54_p1rpoa_rvs', 1))

Rule('sliding_rnap54_rbsrpoa',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoA(type = ('P1', 1)) % Prot_rpoN(PBD_01 = 2) + DNA_rpoA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('RBS', 1)) % RNA_rpoA(type = 'RBS', up = None, dw = 3) + DNA_rpoA(type = 'P1') + free_rpon,
     Parameter('sliding_rnap54_rbsrpoa_fwd', 1))

Rule('docking_rnap38_p1rpoa',
     cplx_rnap38 + DNA_rpoA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoA(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpoa_fwd', 1),
     Parameter('docking_rnap38_p1rpoa_rvs', 1))

Rule('sliding_rnap38_rbsrpoa',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoA(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('RBS', 1)) % RNA_rpoA(type = 'RBS', up = None, dw = 3) + DNA_rpoA(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpoa_fwd', 1))

Rule('sliding_rnap_cdsrpoa',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('RBS', 1)) % RNA_rpoA(type = 'RBS', up = None, dw = 3) + DNA_rpoA(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('CDS', 1)) % RNA_rpoA(type = 'RBS', up = 4, dw = 3) % RNA_rpoA(type = 'CDS', up = None, dw = 4) + DNA_rpoA(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpoa_fwd', 1))

Rule('sliding_rnap_terrpoa',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('CDS', 1)) % RNA_rpoA(type = 'RBS', up = 4, dw = 3) % RNA_rpoA(type = 'CDS', up = None, dw = 4) + DNA_rpoA(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('T1', 1)) % RNA_rpoA(type = 'RBS', up = 4, dw = 3) % RNA_rpoA(type = 'CDS', up = None, dw = 4) + DNA_rpoA(type = 'CDS'),
     Parameter('sliding_rnap_terrpoa_fwd', 1))

Rule('falloff_rnap_terrpoa',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoA(type = ('T1', 1)) % RNA_rpoA(type = 'RBS', up = 4, dw = 3) % RNA_rpoA(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoA(type = 'T1') + RNA_rpoA(type = 'RBS', up = 4, dw = None) % RNA_rpoA(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpoa_fwd', 1))

#kappa rules for rpoB and rpoC transcription
Rule('docking_rnap70_p1rpob',
     cplx_rnap70 + DNA_rpoB(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoB(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpob_fwd', 1),
     Parameter('docking_rnap70_p1rpob_rvs', 1))

Rule('sliding_rnap70_rbsrpob',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoB(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoB(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoB(type = ('RBS', 1)) % RNA_rpoB(type = 'RBS', up = None, dw = 3) + DNA_rpoB(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpob_fwd', 1))

Rule('docking_rnap38_p1rpob',
     cplx_rnap38 + DNA_rpoB(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoB(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpob_fwd', 1),
     Parameter('docking_rnap38_p1rpob_rvs', 1))

Rule('sliding_rnap38_rbsrpob',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoB(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoB(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoB(type = ('RBS', 1)) % RNA_rpoB(type = 'RBS', up = None, dw = 3) + DNA_rpoB(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpob_fwd', 1))

Rule('sliding_rnap_cdsrpob',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoB(type = ('RBS', 1)) % RNA_rpoB(type = 'RBS', up = None, dw = 3) + DNA_rpoB(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoB(type = ('CDS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = None, dw = 4) + DNA_rpoB(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpob_fwd', 1))

Rule('sliding_rnap_rbsrpoc',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoB(type = ('CDS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = None, dw = 4) + DNA_rpoC(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('RBS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = None, dw = 5) + DNA_rpoB(type = 'CDS'),
     Parameter('sliding_rnap70_rbsrpoc_fwd', 1))

Rule('sliding_rnap_cdsrpoc',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('RBS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = None, dw = 5) + DNA_rpoC(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('CDS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6) + DNA_rpoC(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpoc_fwd', 1))

Rule('sliding_rnap_terrpoc',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('CDS', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6) + DNA_rpoC(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('T1', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6) + DNA_rpoC(type = 'CDS'),
     Parameter('sliding_rnap_terrpoc_fwd', 1))

Rule('falloff_rnap_terrpoc',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoC(type = ('T1', 1)) % RNA_rpoB(type = 'RBS', up = 4, dw = 3) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6) >>
     cplx_rnap + DNA_rpoC(type = 'T1') + RNA_rpoB(type = 'RBS', up = 4, dw = None) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6),
     Parameter('falloff_rnap_terrpoc_fwd', 1))

#kappa rules for rpoD transcription
Rule('docking_rnap70_p1rpod',
     cplx_rnap70 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpod_fwd', 1),
     Parameter('docking_rnap70_p1rpod_rvs', 1))

Rule('sliding_rnap70_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpod_fwd', 1))

Rule('docking_rnap24_p1rpod',
     cplx_rnap24 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoE(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap24_p1rpod_fwd', 1),
     Parameter('docking_rnap24_p1rpod_rvs', 1))

Rule('sliding_rnap24_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_rpoE(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_rpoe,
     Parameter('sliding_rnap24_rbsrpod_fwd', 1))

Rule('docking_rnap32_p1rpod',
     cplx_rnap32 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoH(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap32_p1rpod_fwd', 1),
     Parameter('docking_rnap32_p1rpod_rvs', 1))

Rule('sliding_rnap32_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_rpoH(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_rpoh,
     Parameter('sliding_rnap32_rbsrpod_fwd', 1))

Rule('docking_rnap28_p1rpod',
     cplx_rnap28 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_fliA(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap28_p1rpod_fwd', 1),
     Parameter('docking_rnap28_p1rpod_rvs', 1))

Rule('sliding_rnap28_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_fliA(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_flia,
     Parameter('sliding_rnap28_rbsrpod_fwd', 1))

Rule('docking_rnap54_p1rpod',
     cplx_rnap54 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoN(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap54_p1rpod_fwd', 1),
     Parameter('docking_rnap54_p1rpod_rvs', 1))

Rule('sliding_rnap54_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_rpoN(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_rpon,
     Parameter('sliding_rnap54_rbsrpod_fwd', 1))

Rule('docking_rnap38_p1rpod',
     cplx_rnap38 + DNA_rpoD(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoD(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpod_fwd', 1),
     Parameter('docking_rnap38_p1rpod_rvs', 1))

Rule('sliding_rnap38_rbsrpod',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoD(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoD(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpod_fwd', 1))

Rule('sliding_rnap_cdsrpod',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('RBS', 1)) % RNA_rpoD(type = 'RBS', up = None, dw = 3) + DNA_rpoD(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('CDS', 1)) % RNA_rpoD(type = 'RBS', up = 4, dw = 3) % RNA_rpoD(type = 'CDS', up = None, dw = 4) + DNA_rpoD(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpod_fwd', 1))

Rule('sliding_rnap_terrpod',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('CDS', 1)) % RNA_rpoD(type = 'RBS', up = 4, dw = 3) % RNA_rpoD(type = 'CDS', up = None, dw = 4) + DNA_rpoD(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('T1', 1)) % RNA_rpoD(type = 'RBS', up = 4, dw = 3) % RNA_rpoD(type = 'CDS', up = None, dw = 4) + DNA_rpoD(type = 'CDS'),
     Parameter('sliding_rnap_terrpod_fwd', 1))

Rule('falloff_rnap_terrpod',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoD(type = ('T1', 1)) % RNA_rpoD(type = 'RBS', up = 4, dw = 3) % RNA_rpoD(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoD(type = 'T1') + RNA_rpoD(type = 'RBS', up = 4, dw = None) % RNA_rpoD(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpod_fwd', 1))

#kappa rules for rpoE transcription
Rule('docking_rnap70_p1rpoe',
     cplx_rnap70 + DNA_rpoE(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoE(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpoe_fwd', 1),
     Parameter('docking_rnap70_p1rpoe_rvs', 1))

Rule('sliding_rnap70_rbsrpoe',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoE(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoE(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('RBS', 1)) % RNA_rpoE(type = 'RBS', up = None, dw = 3) + DNA_rpoE(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpoe_fwd', 1))

Rule('docking_rnap24_p1rpoe',
     cplx_rnap24 + DNA_rpoE(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoE(PBD_01 = 2) % DNA_rpoE(type = ('P1', 1)),
     Parameter('docking_rnap24_p1rpoe_fwd', 1),
     Parameter('docking_rnap24_p1rpoe_rvs', 1))

Rule('sliding_rnap24_rbsrpoe',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoE(type = ('P1', 1)) % Prot_rpoE(PBD_01 = 2) + DNA_rpoE(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('RBS', 1)) % RNA_rpoE(type = 'RBS', up = None, dw = 3) + DNA_rpoE(type = 'P1') + free_rpoe,
     Parameter('sliding_rnap24_rbsrpoe_fwd', 1))

Rule('docking_rnap38_p1rpoe',
     cplx_rnap38 + DNA_rpoE(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoE(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpoe_fwd', 1),
     Parameter('docking_rnap38_p1rpoe_rvs', 1))

Rule('sliding_rnap38_rbsrpoe',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoE(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoE(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('RBS', 1)) % RNA_rpoE(type = 'RBS', up = None, dw = 3) + DNA_rpoE(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpoe_fwd', 1))

Rule('sliding_rnap_cdsrpoe',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('RBS', 1)) % RNA_rpoE(type = 'RBS', up = None, dw = 3) + DNA_rpoE(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('CDS', 1)) % RNA_rpoE(type = 'RBS', up = 4, dw = 3) % RNA_rpoE(type = 'CDS', up = None, dw = 4) + DNA_rpoE(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpoe_fwd', 1))

Rule('sliding_rnap_terrpoe',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('CDS', 1)) % RNA_rpoE(type = 'RBS', up = 4, dw = 3) % RNA_rpoE(type = 'CDS', up = None, dw = 4) + DNA_rpoE(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('T1', 1)) % RNA_rpoE(type = 'RBS', up = 4, dw = 3) % RNA_rpoE(type = 'CDS', up = None, dw = 4) + DNA_rpoE(type = 'CDS'),
     Parameter('sliding_rnap_terrpoe_fwd', 1))

Rule('falloff_rnap_terrpoe',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoE(type = ('T1', 1)) % RNA_rpoE(type = 'RBS', up = 4, dw = 3) % RNA_rpoE(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoE(type = 'T1') + RNA_rpoE(type = 'RBS', up = 4, dw = None) % RNA_rpoE(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpoe_fwd', 1))

#kappa rules for rpoH transcription
Rule('docking_rnap70_p1rpoh',
     cplx_rnap70 + DNA_rpoH(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoH(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpoh_fwd', 1),
     Parameter('docking_rnap70_p1rpoh_rvs', 1))

Rule('sliding_rnap70_rbsrpoh',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoH(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoH(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('RBS', 1)) % RNA_rpoH(type = 'RBS', up = None, dw = 3) + DNA_rpoH(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpoh_fwd', 1))

Rule('docking_rnap24_p1rpoh',
     cplx_rnap24 + DNA_rpoH(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoE(PBD_01 = 2) % DNA_rpoH(type = ('P1', 1)),
     Parameter('docking_rnap24_p1rpoh_fwd', 1),
     Parameter('docking_rnap24_p1rpoh_rvs', 1))

Rule('sliding_rnap24_rbsrpoh',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoH(type = ('P1', 1)) % Prot_rpoE(PBD_01 = 2) + DNA_rpoH(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('RBS', 1)) % RNA_rpoH(type = 'RBS', up = None, dw = 3) + DNA_rpoH(type = 'P1') + free_rpoe,
     Parameter('sliding_rnap24_rbsrpoh_fwd', 1))

Rule('docking_rnap54_p1rpoh',
     cplx_rnap54 + DNA_rpoH(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoN(PBD_01 = 2) % DNA_rpoH(type = ('P1', 1)),
     Parameter('docking_rnap54_p1rpoh_fwd', 1),
     Parameter('docking_rnap54_p1rpoh_rvs', 1))

Rule('sliding_rnap54_rbsrpoh',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoH(type = ('P1', 1)) % Prot_rpoN(PBD_01 = 2) + DNA_rpoH(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('RBS', 1)) % RNA_rpoH(type = 'RBS', up = None, dw = 3) + DNA_rpoH(type = 'P1') + free_rpon,
     Parameter('sliding_rnap54_rbsrpoh_fwd', 1))

Rule('docking_rnap38_p1rpoh',
     cplx_rnap38 + DNA_rpoH(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoH(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpoh_fwd', 1),
     Parameter('docking_rnap38_p1rpoh_rvs', 1))

Rule('sliding_rnap38_rbsrpoh',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoH(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoH(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('RBS', 1)) % RNA_rpoH(type = 'RBS', up = None, dw = 3) + DNA_rpoH(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpoh_fwd', 1))

Rule('sliding_rnap_cdsrpoh',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('RBS', 1)) % RNA_rpoH(type = 'RBS', up = None, dw = 3) + DNA_rpoH(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('CDS', 1)) % RNA_rpoH(type = 'RBS', up = 4, dw = 3) % RNA_rpoH(type = 'CDS', up = None, dw = 4) + DNA_rpoH(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpoh_fwd', 1))

Rule('sliding_rnap_terrpoh',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('CDS', 1)) % RNA_rpoH(type = 'RBS', up = 4, dw = 3) % RNA_rpoH(type = 'CDS', up = None, dw = 4) + DNA_rpoH(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('T1', 1)) % RNA_rpoH(type = 'RBS', up = 4, dw = 3) % RNA_rpoH(type = 'CDS', up = None, dw = 4) + DNA_rpoH(type = 'CDS'),
     Parameter('sliding_rnap_terrpoh_fwd', 1))

Rule('falloff_rnap_terrpoh',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoH(type = ('T1', 1)) % RNA_rpoH(type = 'RBS', up = 4, dw = 3) % RNA_rpoH(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoH(type = 'T1') + RNA_rpoH(type = 'RBS', up = 4, dw = None) % RNA_rpoH(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpoh_fwd', 1))

#kappa rules for rpoN transcription
Rule('docking_rnap70_p1rpon',
     cplx_rnap70 + DNA_rpoN(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoN(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpon_fwd', 1),
     Parameter('docking_rnap70_p1rpon_rvs', 1))

Rule('sliding_rnap70_rbsrpon',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoN(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoN(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('RBS', 1)) % RNA_rpoN(type = 'RBS', up = None, dw = 3) + DNA_rpoN(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpon_fwd', 1))

Rule('docking_rnap24_p1rpon',
     cplx_rnap24 + DNA_rpoN(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoE(PBD_01 = 2) % DNA_rpoN(type = ('P1', 1)),
     Parameter('docking_rnap24_p1rpon_fwd', 1),
     Parameter('docking_rnap24_p1rpon_rvs', 1))

Rule('sliding_rnap24_rbsrpon',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoN(type = ('P1', 1)) % Prot_rpoE(PBD_01 = 2) + DNA_rpoN(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('RBS', 1)) % RNA_rpoN(type = 'RBS', up = None, dw = 3) + DNA_rpoN(type = 'P1') + free_rpoe,
     Parameter('sliding_rnap24_rbsrpon_fwd', 1))

Rule('docking_rnap28_p1rpon',
     cplx_rnap28 + DNA_rpoN(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_fliA(PBD_01 = 2) % DNA_rpoN(type = ('P1', 1)),
     Parameter('docking_rnap28_p1rpon_fwd', 1),
     Parameter('docking_rnap28_p1rpon_rvs', 1))

Rule('sliding_rnap28_rbsrpon',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoN(type = ('P1', 1)) % Prot_fliA(PBD_01 = 2) + DNA_rpoN(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('RBS', 1)) % RNA_rpoN(type = 'RBS', up = None, dw = 3) + DNA_rpoN(type = 'P1') + free_flia,
     Parameter('sliding_rnap28_rbsrpon_fwd', 1))

Rule('docking_rnap38_p1rpon',
     cplx_rnap38 + DNA_rpoN(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_rpoN(type = ('P1', 1)),
     Parameter('docking_rnap38_p1rpon_fwd', 1),
     Parameter('docking_rnap38_p1rpon_rvs', 1))

Rule('sliding_rnap38_rbsrpon',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoN(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_rpoN(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('RBS', 1)) % RNA_rpoN(type = 'RBS', up = None, dw = 3) + DNA_rpoN(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsrpon_fwd', 1))

Rule('sliding_rnap_cdsrpon',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('RBS', 1)) % RNA_rpoN(type = 'RBS', up = None, dw = 3) + DNA_rpoN(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('CDS', 1)) % RNA_rpoN(type = 'RBS', up = 4, dw = 3) % RNA_rpoN(type = 'CDS', up = None, dw = 4) + DNA_rpoN(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpon_fwd', 1))

Rule('sliding_rnap_terrpon',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('CDS', 1)) % RNA_rpoN(type = 'RBS', up = 4, dw = 3) % RNA_rpoN(type = 'CDS', up = None, dw = 4) + DNA_rpoN(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('T1', 1)) % RNA_rpoN(type = 'RBS', up = 4, dw = 3) % RNA_rpoN(type = 'CDS', up = None, dw = 4) + DNA_rpoN(type = 'CDS'),
     Parameter('sliding_rnap_terrpon_fwd', 1))

Rule('falloff_rnap_terrpon',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoN(type = ('T1', 1)) % RNA_rpoN(type = 'RBS', up = 4, dw = 3) % RNA_rpoN(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoN(type = 'T1') + RNA_rpoN(type = 'RBS', up = 4, dw = None) % RNA_rpoN(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpon_fwd', 1))

#kappa rules for rpoS transcription
Rule('docking_rnap70_p1rpos',
     cplx_rnap70 + DNA_rpoS(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_rpoS(type = ('P1', 1)),
     Parameter('docking_rnap70_p1rpos_fwd', 1),
     Parameter('docking_rnap70_p1rpos_rvs', 1))

Rule('sliding_rnap70_rbsrpos',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_rpoS(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_rpoS(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('RBS', 1)) % RNA_rpoS(type = 'RBS', up = None, dw = 3) + DNA_rpoS(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsrpos_fwd', 1))

Rule('sliding_rnap_cdsrpos',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('RBS', 1)) % RNA_rpoS(type = 'RBS', up = None, dw = 3) + DNA_rpoS(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('CDS', 1)) % RNA_rpoS(type = 'RBS', up = 4, dw = 3) % RNA_rpoS(type = 'CDS', up = None, dw = 4) + DNA_rpoS(type = 'RBS'),
     Parameter('sliding_rnap_cdsrpos_fwd', 1))

Rule('sliding_rnap_terrpos',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('CDS', 1)) % RNA_rpoS(type = 'RBS', up = 4, dw = 3) % RNA_rpoS(type = 'CDS', up = None, dw = 4) + DNA_rpoS(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('T1', 1)) % RNA_rpoS(type = 'RBS', up = 4, dw = 3) % RNA_rpoS(type = 'CDS', up = None, dw = 4) + DNA_rpoS(type = 'CDS'),
     Parameter('sliding_rnap_terrpos_fwd', 1))

Rule('falloff_rnap_terrpos',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_rpoS(type = ('T1', 1)) % RNA_rpoS(type = 'RBS', up = 4, dw = 3) % RNA_rpoS(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_rpoS(type = 'T1') + RNA_rpoS(type = 'RBS', up = 4, dw = None) % RNA_rpoS(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terrpos_fwd', 1))

#kappa rules for fecI transcription
Rule('docking_rnap70_p1feci',
     cplx_rnap70 + DNA_fecI(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_fecI(type = ('P1', 1)),
     Parameter('docking_rnap70_p1feci_fwd', 1),
     Parameter('docking_rnap70_p1feci_rvs', 1))

Rule('sliding_rnap70_rbsfeci',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_fecI(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_fecI(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('RBS', 1)) % RNA_fecI(type = 'RBS', up = None, dw = 3) + DNA_fecI(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsfeci_fwd', 1))

Rule('docking_rnap38_p1feci',
     cplx_rnap38 + DNA_fecI(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoS(PBD_01 = 2) % DNA_fecI(type = ('P1', 1)),
     Parameter('docking_rnap38_p1feci_fwd', 1),
     Parameter('docking_rnap38_p1feci_rvs', 1))

Rule('sliding_rnap38_rbsfeci',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_fecI(type = ('P1', 1)) % Prot_rpoS(PBD_01 = 2) + DNA_fecI(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('RBS', 1)) % RNA_fecI(type = 'RBS', up = None, dw = 3) + DNA_fecI(type = 'P1') + free_rpos,
     Parameter('sliding_rnap38_rbsfeci_fwd', 1))

Rule('sliding_rnap_cdsfeci',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('RBS', 1)) % RNA_fecI(type = 'RBS', up = None, dw = 3) + DNA_fecI(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('CDS', 1)) % RNA_fecI(type = 'RBS', up = 4, dw = 3) % RNA_fecI(type = 'CDS', up = None, dw = 4) + DNA_fecI(type = 'RBS'),
     Parameter('sliding_rnap_cdsfeci_fwd', 1))

Rule('sliding_rnap_terfeci',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('CDS', 1)) % RNA_fecI(type = 'RBS', up = 4, dw = 3) % RNA_fecI(type = 'CDS', up = None, dw = 4) + DNA_fecI(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('T1', 1)) % RNA_fecI(type = 'RBS', up = 4, dw = 3) % RNA_fecI(type = 'CDS', up = None, dw = 4) + DNA_fecI(type = 'CDS'),
     Parameter('sliding_rnap_terfeci_fwd', 1))

Rule('falloff_rnap_terfeci',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fecI(type = ('T1', 1)) % RNA_fecI(type = 'RBS', up = 4, dw = 3) % RNA_fecI(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_fecI(type = 'T1') + RNA_fecI(type = 'RBS', up = 4, dw = None) % RNA_fecI(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terfeci_fwd', 1))

#kappa rules for fliA transcription
Rule('docking_rnap70_p1flia',
     cplx_rnap70 + DNA_fliA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_rpoD(PBD_01 = 2) % DNA_fliA(type = ('P1', 1)),
     Parameter('docking_rnap70_p1flia_fwd', 1),
     Parameter('docking_rnap70_p1flia_rvs', 1))

Rule('sliding_rnap70_rbsflia',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_fliA(type = ('P1', 1)) % Prot_rpoD(PBD_01 = 2) + DNA_fliA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('RBS', 1)) % RNA_fliA(type = 'RBS', up = None, dw = 3) + DNA_fliA(type = 'P1') + free_rpod,
     Parameter('sliding_rnap70_rbsflia_fwd', 1))

Rule('docking_rnap28_p1flia',
     cplx_rnap28 + DNA_fliA(type = 'P1') !=
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % Prot_fliA(PBD_01 = 2) % DNA_fliA(type = ('P1', 1)),
     Parameter('docking_rnap28_p1flia_fwd', 1),
     Parameter('docking_rnap28_p1flia_rvs', 1))

Rule('sliding_rnap28_rbsflia',
     RNAP(DBD_01 = 1, PBD_01 = 2, RBD_01 = None) % DNA_fliA(type = ('P1', 1)) % Prot_fliA(PBD_01 = 2) + DNA_fliA(type = 'RBS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('RBS', 1)) % RNA_fliA(type = 'RBS', up = None, dw = 3) + DNA_fliA(type = 'P1') + free_flia,
     Parameter('sliding_rnap28_rbsflia_fwd', 1))

Rule('sliding_rnap_cdsflia',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('RBS', 1)) % RNA_fliA(type = 'RBS', up = None, dw = 3) + DNA_fliA(type = 'CDS') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('CDS', 1)) % RNA_fliA(type = 'RBS', up = 4, dw = 3) % RNA_fliA(type = 'CDS', up = None, dw = 4) + DNA_fliA(type = 'RBS'),
     Parameter('sliding_rnap_cdsflia_fwd', 1))

Rule('sliding_rnap_terflia',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('CDS', 1)) % RNA_fliA(type = 'RBS', up = 4, dw = 3) % RNA_fliA(type = 'CDS', up = None, dw = 4) + DNA_fliA(type = 'T1') >>
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('T1', 1)) % RNA_fliA(type = 'RBS', up = 4, dw = 3) % RNA_fliA(type = 'CDS', up = None, dw = 4) + DNA_fliA(type = 'CDS'),
     Parameter('sliding_rnap_terflia_fwd', 1))

Rule('falloff_rnap_terflia',
     RNAP(DBD_01 = 1, PBD_01 = None, RBD_01 = 3) % DNA_fliA(type = ('T1', 1)) % RNA_fliA(type = 'RBS', up = 4, dw = 3) % RNA_fliA(type = 'CDS', up = None, dw = 4) >>
     cplx_rnap + DNA_fliA(type = 'T1') + RNA_fliA(type = 'RBS', up = 4, dw = None) % RNA_fliA(type = 'CDS', up = None, dw = 4),
     Parameter('falloff_rnap_terflia_fwd', 1))

synthesize_degrade_table([[RNA_rpoA(type = 'RBS', up = 4, dw = None) % RNA_rpoA(type = 'CDS', up = None, dw = 4), None, 0.0571],
                          [RNA_rpoB(type = 'RBS', up = 4, dw = None) % RNA_rpoB(type = 'CDS', up = 5, dw = 4) % RNA_rpoC(type = 'RBS', up = 6, dw = 5) % RNA_rpoC(type = 'CDS', up = None, dw = 6), None, 0.0286],
                          [RNA_rpoD(type = 'RBS', up = 4, dw = None) % RNA_rpoD(type = 'CDS', up = None, dw = 4), None, 0.0857],
                          [RNA_rpoE(type = 'RBS', up = 4, dw = None) % RNA_rpoE(type = 'CDS', up = None, dw = 4), None, 0.0429],
                          [RNA_rpoH(type = 'RBS', up = 4, dw = None) % RNA_rpoH(type = 'CDS', up = None, dw = 4), None, 0.0571],
                          [RNA_rpoN(type = 'RBS', up = 4, dw = None) % RNA_rpoN(type = 'CDS', up = None, dw = 4), None, 0.0571],
                          [RNA_rpoS(type = 'RBS', up = 4, dw = None) % RNA_rpoS(type = 'CDS', up = None, dw = 4), None, 0.0143],
                          [RNA_fecI(type = 'RBS', up = 4, dw = None) % RNA_fecI(type = 'CDS', up = None, dw = 4), None, 0.0286],
                          [RNA_fliA(type = 'RBS', up = 4, dw = None) % RNA_fliA(type = 'CDS', up = None, dw = 4), None, 0.0286]])
