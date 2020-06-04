# DSLR
A Machine Learning project using Logistic Regression.

# Purpose
This project's main goal is to solve a classification problem and by doing so, learning about data analysis, visualization and Machine Learning techniques. 
There is a training dataset and a testing dataset in the resources folder. 
In them there are Hogwart students who need to be put in one of the 4 houses according their grades in many different subjects.
In order to do that, I first familiarized myself with basic data visualization techniques as well as data analysis in order to select the most interesting features.

# Required packages
-Numpy
-Pandas
-Matplotlib
-Seaborn

# Usage
There are many executable programs in this repository, here is what they do and how to use them:

### logreg_train
Trains the classification model
<pre><code>python3 logreg_train.py -h</code>
usage: logreg_train.py [-h] [-v] [-vi House N_feature1 N_feature2] dataset

Trains our model with the specified dataset

positional arguments:
  dataset: dataset, needs to be a csv

optional arguments:
  -h, --help: show this help message and exit
  -v, --verbose: display in real time actions of training
  -vi House N_feature1 N_feature2: display data of one house in a separate windows

<code>python3 logreg_train.py "./resources/dataset_train.csv" -vi "Ravenclaw" 1 2</code>
</pre>
>This will train the model with the training data
>Generated weights will be saved in weights.csv
>Adding the -vi option will display a graph on the training session in a "one vs all" format for the specified features and house

### logreg_predict
Predicts house belonging for a list of students
<pre><code>python3 logreg_predict.py -h</code>
usage: logreg_predict.py [-h] [-a] [-p] dataset weights

predicts student's house with our model

positional arguments:
  dataset: dataset, needs to be a csv
  weights: weights, needs to be a csv

optional arguments:
  -h, --help: show this help message and exit
  -a, --accuracy: show accuracy for dataset_train
  -p, --piechart: print a piechart for the results

<code>python3 logreg_predict.py "./resources/dataset_test.csv" "./weights.csv" -p</code>
</pre>
>This will predict a house for each student in the test dataset
>Adding the -p option displays a pie chart of the repartition of each student
>You can also use -a if you are making predictions on the training data to know the rate of correct predictions
