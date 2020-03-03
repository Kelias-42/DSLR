import sys
import os
import pandas as pd
import numpy as np

import compute_info

select_fnc = {
	0: compute_info.count,
	1: compute_info.mean,
	2: compute_info.std,
	3: compute_info.mini,
	4: compute_info.quarter,
	5: compute_info.median,
	6: compute_info.three_quarters,
	7: compute_info.maxi
}

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
	#print(metrics)
	return metrics

def clean_print(feature_column, data):
	data.insert(0, feature_column)
	for i in range(len(data)):
		if i == 0:
			print('{:<20s}{:>20s}{:>20s}{:>20s}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))
		else:
			print('{:<20.6f}{:>20.6f}{:>20.6f}{:>20.6f}'.format(data[i][0],data[i][1],data[i][2],data[i][3]))

def main():
	np.set_printoptions(suppress=True)
	data = get_data()
	data = data.select_dtypes('number')
	data_array = data.to_numpy()
	metrics = describe(data_array)	
	clean_print(data.columns, metrics.tolist())

if __name__ == "__main__":
	main()