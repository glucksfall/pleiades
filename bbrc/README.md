* Please cite the models in this folder using the following:

Pérez-Acle et al. (2017) Stochastic Simulation of Multiscale Complex Systems with PISKaS: a rule-based approach. Submitted manuscript to Biochemical and Biophysical Research Communications.

Santibáñez R, Garrido D, Pérez-Acle T and Martin AJM. Stochastic modeling of gene regulatory networks in Escherichia coli [version 1; not peer reviewed]. F1000Research 2017, 6(ISCB Comm J):1184 (poster) (doi: 10.7490/f1000research.1114462.1). Download poster [here](https://f1000research.com/posters/6-1184).

* To simulate please install [KaSim](https://github.com/Kappa-Dev/KaSim) or [PISKaS](https://github.com/DLab/PISKaS), pandas, and PySB. Intructions to simulate the models using [BNGL](https://github.com/RuleWorld/bionetgen), scipy or MATLAB&reg; would be added soon.

1. To install PySB and pandas in python3:

  `sudo -H pip3 install pysb pandas`

2. Export to kappa:

  `python3 -m pysb.export setting01_rnap01_sigma07.py kappa > setting01_rnap01_sigma07.kappa`

3. To simulate using KaSim v3.5 (not the master branch):

  `path_to_kasim -i setting01_rnap01_sigma07.kappa -t 1000 -p 1000 -o model.out.txt -batch`

4. To simulate using PISKaS v1.3, the model should be modified with the following statements in the top of the file:

  `%compartment: cell 1`
  
  `%use: cell`

  then
  
  `mpirun -np 1 path_to_piskas -i setting01.rnap01.sigma07.kappa -t 1000 -p 1000 -o model.`
