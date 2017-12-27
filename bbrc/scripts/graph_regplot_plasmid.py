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
	with open('plasmid.exp01.large.simulation/test_model.avrg.txt', 'r') as file:
		avrg = read_data(file)
	seaborn.set_style("white")
	seaborn.set_context("poster")
	ax1 = seaborn.regplot(x = avrg.iloc[:,1].divide(100), y = avrg.loc[:,"'obs_dna_i_p1'"], scatter = True, fit_reg = False, ci = 95, scatter_kws={"s": 20}, line_kws={"alpha": 0.3})

	# 2nd data set
	with open('plasmid.exp02.large.simulation/test_model.avrg.txt', 'r') as file:
		avrg = read_data(file)
	seaborn.set_style("white")
	seaborn.set_context("poster")
	seaborn.regplot(x = avrg.iloc[:,1].divide(100), y = avrg.loc[:,"'obs_dna_i_p1'"], ci = 95, scatter = True, fit_reg = False, scatter_kws={"s": 20}, line_kws={"alpha": 0.3}, ax = ax1)

	# final plot options
	plt.xlabel('Time', fontsize = 20)
	plt.ylabel('Plasmid Copy Number', fontsize = 20)
	plt.ylim([0, 500])
	plt.xlim([0, 1000])
	seaborn.despine()
	ax1.figure.savefig('plasmid_copies.eps', format = 'eps', bbox_inches = 'tight')
