# -*- coding: utf-8 -*-

import glob
import seaborn
import multiprocessing
import matplotlib.pyplot as plt

from pandas import *

def read_data(file):
	return pandas.read_csv(file, delimiter = ' ', header = 0)

if __name__ == '__main__':
	# 1st data set
	with open('sigma.exp01.rnap01.sigma07/test_model.avrg.txt', 'r') as file:
		avrg = read_data(file)
	seaborn.set_style("white")
	seaborn.set_context("poster")
	ax1 = seaborn.regplot(x = avrg.iloc[:,1], y = avrg.loc[:,"'RNAP_cplx'"].divide(1), scatter = True, fit_reg = False, ci = 95, scatter_kws={"s": 20}, line_kws={"alpha": 0.3})

	# 2nd data set
	with open('sigma.exp02.rnap07.sigma07/test_model.avrg.txt', 'r') as file:
		avrg = read_data(file)
	seaborn.set_style("white")
	seaborn.set_context("poster")
	seaborn.regplot(x = avrg.iloc[:,1], y = avrg.loc[:,"'RNAP_cplx'"].divide(7), ci = 95, scatter = True, fit_reg = False, scatter_kws={"s": 20}, line_kws={"alpha": 0.3}, ax = ax1)

	# 3rd data setd
	with open('sigma.exp03.rnap28.sigma28/test_model.avrg.txt', 'r') as file:
		avrg = read_data(file)
	seaborn.set_style("white")
	seaborn.set_context("poster")
	seaborn.regplot(x = avrg.iloc[:,1], y = avrg.loc[:,"'RNAP_cplx'"].divide(28), scatter = True, fit_reg = False, ci = 95, scatter_kws={"s": 20}, line_kws={"alpha": 0.3}, ax = ax1)

	# final plot options
	plt.xlabel('Time', fontsize = 20)
	plt.ylabel('Free RNAP-SF complexes', fontsize = 20)
	plt.ylim([0, 0.25])
	plt.xlim([0, 1000])
	seaborn.despine()
	ax1.figure.savefig('sigmas.eps', format = 'eps', bbox_inches = 'tight')
