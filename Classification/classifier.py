# Import necessary libraries
import numpy as np
import pandas as pd
import sklearn as sk
import seaborn as sns
from sklearn import tree
import matplotlib.pyplot as plt
from helper import plot_boundary
from prettytable import PrettyTable
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 20)
plt.rcParams["figure.figsize"] = (12,8)


# Read the data file "election_train.csv" as a Pandas dataframe
elect_train = pd.read_csv("election_train.csv")

# Read the data file "election_test.csv" as a Pandas dataframe
elect_test = pd.read_csv("election_test.csv")

# Take a quick look at the train data
elect_train.head()


### edTest(test_data) ###
# Set the columns minority and bachelor as train data predictors
X_train = ___

# Set the columns minority and bachelor as test data predictors
X_test = ___

# Set the column "won" as the train response variable
y_train = ___

# Set the column "won" as the test response variable
y_test = ___


### edTest(test_models) ###

# Initialize a Decision Tree classifier with a depth of 2
dt1 = ___

# Fit the classifier on the train data
___

# Initialize a Decision Tree classifier with a depth of 10
dt2 = ___

# Fit the classifier on the train data
___


# Call the function plot_boundary from the helper file to get 
# the decision boundaries of both the classifiers
plot_boundary(elect_train, dt1, dt2)


# Set of predictor columns
pred_cols = ['minority', 'density','hispanic','obesity','female','income','bachelor','inactivity']

# Use the columns above as the features to 
# get the predictor set from the train data
X_train = ___

# Use the columns above as the features to 
# get the predictor set from the test data
X_test = ___

# Initialize a Decision Tree classifier with a depth of 2
dt1 = ___

# Initialize a Decision Tree classifier with a depth of 10
dt2 = ___

# Initialize a Decision Tree classifier with a depth of 15
dt3 = ___

# Fit all the classifier on the train data
___
___
___


### edTest(test_accuracy) ###

# Compute the train and test accuracy for the first decision tree classifier of depth 2
dt1_train_acc = ___
dt1_test_acc = ___

# Compute the train and test accuracy for the second decision tree classifier of depth 10
dt2_train_acc = ___
dt2_test_acc = ___

# Compute the train and test accuracy for the third decision tree classifier of depth 15
dt3_train_acc = ___
dt3_test_acc = ___


# Helper code to plot the scores of each classifier as a table
pt = PrettyTable()
pt.field_names = ['Max Depth', 'Number of Features', 'Train Accuracy', 'Test Accuracy']
pt.add_row([2, len(pred_cols), round(dt1_train_acc, 4), round(dt1_test_acc,4)])
pt.add_row([10, len(pred_cols), round(dt2_train_acc,4), round(dt2_test_acc,4)])
pt.add_row([15, len(pred_cols), round(dt3_train_acc,4), round(dt3_test_acc,4)])
print(pt)
