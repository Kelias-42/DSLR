import matplotlib.pyplot as plt
import numpy as np
import describe

houses={
		"Ravenclaw": 1,
		"Slytherin": 2,
		"Gryffindor": 3,
		"Hufflepuff": 4
		}

def plot_hist(data):
	for i in range(1, 4):
		sorted_data = []	
		for row in data:
			if row[1] == i and not np.isnan(row[12]):
				sorted_data.append(row[12])
		plt.hist(sorted_data, alpha=0.5)

def main():
	np.set_printoptions(suppress=True)
	data = describe.get_data()
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	data = data.to_numpy()
	plot_hist(data)

if __name__ == "__main__":
	main()