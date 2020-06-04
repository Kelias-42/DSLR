# DSLR
A Machine Learning project using Logistic Regression.

# Purpose
This project's main goal is to solve a classification problem and by doing so, learning about data analysis, data visualization and Machine Learning techniques. 
I was given a training dataset and a testing dataset which are in the resources folder. 
In them there are Hogwart students who need to be put in one of 4 houses according to their grades in many different subjects.
In order to do that, I first familiarized myself with basic data visualization techniques as well as data analysis in order to select the most interesting features. I then made a training program generating weights which will be used by the prediction program to assign students to their house.

# Required packages
* Numpy
* Pandas
* Matplotlib
* Seaborn

# Usage
There are many executable programs in this repository, here is what they do and how to use them:

### logreg_train
Trains the classification model
```
$> python logreg_train.py -h
usage: logreg_train.py [-h] [-v] [-vi House N_feature1 N_feature2] dataset

Trains the model with the specified dataset

positional arguments:
  dataset: dataset, needs to be a csv

optional arguments:
  -h, --help: show this help message and exit
  -v, --verbose: display in real time actions of training
  -vi House N_feature1 N_feature2: display data of one house in a separate windows

$> python logreg_train.py "./resources/dataset_train.csv" -vi "Ravenclaw" 1 2
```
>This will train the model by computing weights

>Generated weights will be saved in weights.csv

>Adding the -vi option will display a graph on the training session in a "one vs all" format for the specified features and house

### logreg_predict
Predicts house belonging for a list of students
```
$> python logreg_predict.py -h
usage: logreg_predict.py [-h] [-a] [-p] dataset weights

predicts student's house with our model

positional arguments:
  dataset: dataset, needs to be a csv
  weights: weights, needs to be a csv

optional arguments:
  -h, --help: show this help message and exit
  -a, --accuracy: show accuracy for dataset_train
  -p, --piechart: print a piechart for the results
$> python logreg_predict.py "./resources/dataset_test.csv" "./weights.csv" -p
```

>This will predict a house for each student in the test dataset

>Adding the -p option displays a pie chart of the repartition of each student

>You can also use -a if you are making predictions on the training data to know the rate of correct predictions

### describe
Gives different metrics regarding the dataset given as an argument
```
$> python describe.py "./resources/dataset_train.csv"
```
>This will display a description of the training dataset similar to pandas.describe()

### pair_plot
Displays a pair_plot of the data using seaborn. Very useful to determine which attributes to keep for the training.
```
$> python pair_plot.py ./resources/dataset_train.csv
```
>This will open a new window containing the pair plot, it may take a while to load considering there's a lot of computation to be done

### histogram
Displays a histogram answering the question:

Which Hogwarts course has a homogeneous score distribution beween all four houses?
```
$> python histogram.py "./resources/dataset_train.csv"
```
>This will open a new window containing the histogram

### Scatter Plot
Displays a scatter plot answering the question:

What are the two features that are similar?
```shell
$> python scatter_plot.py "./resources/dataset_train.csv"
```
>This will open a new window containing the scatter plot

# Credit
This project was made by Julien Dumay (https://github.com/ChokMania) and myself, Aleksi Gautier (https://github.com/Kelias-42)
