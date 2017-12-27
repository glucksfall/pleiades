import glob
import shlex
import pandas
import subprocess
import multiprocessing

from pandas import DataFrame

def precompile_kappa():
	cmd = 'mpirun -np 1 PISKaS -i test_model.piskas -t 0 -p 1 -make-sim test_model.bin -o data. -sync-t 1'
	process = subprocess.Popen(shlex.split(cmd), shell = False)
	process.wait()
	cmd = 'rm -f ./profiling.html data.*.out'
	process = subprocess.Popen(shlex.split(cmd), shell = False)
	process.wait()
	return

def run_kasim_precompiled(num):
	cmd = 'mpirun -np 1 PISKaS -load-sim test_model.bin -t 1000 -p 1000 -o test_model.{:03d}. -sync-t 1'.format(num)
	process = subprocess.Popen(shlex.split(cmd), shell = False)
	process.wait()
	return

def read_data(file):
	return pandas.read_csv(file, delimiter = ' ', header = 0, skipfooter = 9, engine = 'python')

def statistics(data):
	rows = range(len(data[0].axes[0]))
	cols = list(data[0].columns.values)
	avrg = pandas.DataFrame(index = rows, columns = cols).fillna(0)
	stdv = pandas.DataFrame(index = rows, columns = cols).fillna(0)

	for i in range(0, len(data)):
		avrg += data[i].divide(len(data))

	DataFrame.to_csv(avrg, path_or_buf = './test_model.avrg.txt', sep = ' ', index = False, float_format = '%.3f')

	for i in range(0, len(data)):
		stdv += (((data[i] - avrg)**2).divide(len(data)-1))

	DataFrame.to_csv(stdv**(0.5), path_or_buf = './test_model.stdv.txt', sep = ' ', index = False, float_format = '%.3f')

	return

if __name__ == '__main__':
	precompile_kappa()
	sims = multiprocessing.Pool(multiprocessing.cpu_count()-1).map(run_kasim_precompiled, range(0, 1000))
	data = multiprocessing.Pool(multiprocessing.cpu_count()-1).map(read_data, glob.glob("./test_model.*.cell.out"))
	avrg = statistics(data)
