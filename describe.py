import sys
import pandas as pd
import numpy as np
import compute_metrics

select_fnc = {
	0: compute_metrics.count,
	1: compute_metrics.mean,
	2: compute_metrics.std,
	3: compute_metrics.mini,
	4: compute_metrics.quarter,
	5: compute_metrics.median,
	6: compute_metrics.three_quarters,
	7: compute_metrics.maxi
}

rows = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]

def get_data():
	try:
		data_path = sys.argv[1]
		return (pd.read_csv(data_path))
	except IndexError:
		print("usage: python describe.py [your_dataset].csv")
		sys.exit(-1)
	except IOError:
		print("could not read data file")
		sys.exit(-1)

def describe(data):
	data_len = len(data[0])
	i = 0
	metrics = np.ndarray(shape=(8, data_len), dtype=float)
	while i != 8:
		j = 0
		while j != data_len:
			metrics[i][j] = select_fnc[i](data[:,j])
			j += 1
		i += 1
	for i in range(len(metrics[:,0]) - 1):
		for j in range(len(metrics[0]) - 1):
			metrics[i][j] = np.format_float_positional(np.float(metrics[i][j]), unique=False, precision=6)
	return metrics

def get_width(column_name, data_column):
	max_size = len(column_name)
	for field in data_column:
		max_size = max(len("%.6f"%field), max_size)
	return max_size

def clean_print(columns, data):
	print("{:<5s}".format(' '), end='')
	for i in range(len(columns)):
		width = get_width(columns[i], data[:,i])
		print("{:>{:d}s}".format(columns[i], width + 2), end='')

	for i in range(len(data[:,0])):
		print("\n{:<5s}".format(rows[i]), end='')
		for j in range(len(data[0])):
			width = get_width(columns[j], data[:,j])
			print("{:>{:d}.6f}".format(data[i][j], width + 2), end='')

if __name__ == "__main__":
	np.set_printoptions(suppress=True)
	data = get_data()
	data = data.select_dtypes('number')
	metrics = describe(data.to_numpy())
	clean_print(data.columns, metrics)