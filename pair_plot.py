import matplotlib.pyplot as plt
import seaborn as sb
import describe

houses={
	"Ravenclaw": 1,
	"Slytherin": 2,
	"Gryffindor": 3,
	"Hufflepuff": 4
}

houses_rev = {value: key for key, value in houses.items()}

if __name__ == "__main__":
	data = describe.get_data()
	data["Hogwarts House"].replace(houses, inplace=True)
	data = data.select_dtypes('number')
	data["Hogwarts House"].replace(houses_rev, inplace=True)
	data.drop('Index', axis=1, inplace=True)
	sb.pairplot(data, hue='Hogwarts House', markers='.')
	plt.show()