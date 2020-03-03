import numpy as np

def count(data):
	count = 0
	for i in data:
		if not np.isnan(i):
			count += 1
	return float(count)

def mean(data):
	curr_count = count(data)
	if curr_count == 0:
		return float("NaN")
	total = 0
	for i in data:
		if not np.isnan(i):
			total += i
	return float(total / curr_count)

def std(data):
	return float(2)

def mini(data):
	return float(min(data))

def maxi(data):
	return float(max(data))

def quarter(data):
	return float(5)

def median(data):
	return float(6)

def three_quarters(data):
	return float(7)