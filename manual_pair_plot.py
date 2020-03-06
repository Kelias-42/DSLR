import matplotlib.pyplot as plt
import numpy as np
import describe

houses={
	"Ravenclaw": 1,
	"Slytherin": 2,
	"Gryffindor": 3,
	"Hufflepuff": 4
}

def pair_plot(data):
	#plt.figure(figsize=(20,15))
	size = len(data[0]) - 2
	for i in range(size):
		for j in range(size):
			plt.subplot(size, size, ((i * size) + j + 1))
			for house in range (1, 5):
				x = []
				y = []
				for row in data:
					if row[1] == house and not np.isnan(row[i + 2]) and not np.isnan(row[j + 2]):
						x.append(row[i + 2])
						y.append(row[j + 2])
				plt.scatter(x, y, alpha=0.7, s=9)
	

def main():
	data = describe.get_data()
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	#columns = data.columns
	data = data.to_numpy()
	#for i in range(2, len(data[0])):
	#	for j in range(2, len(data[0])):	
	#		scatter_plot(data, i, j)
	pair_plot(data)
	
if __name__ == "__main__":
	main()