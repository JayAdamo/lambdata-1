#!/usr/bin/env python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
import category_encoders as ce


x=2

def increment(number):
    """A toy function that increases a given number by 1"""
    return number + 1

class Animal:
    """A toy Class layout, designed to create an animal.
    Parameters:
    -----------
    : name- The name of the critter.
    : weight- the weight, in pounds, of the critter.
    : diet_type- what the critter eats.
    Outputs:
    -----------
    How the animal runs.
    """
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        if weight > 0:
            self.weight = weight
        else:
            raise Exception
        self.diet_type = diet_type
    def run(self):
        return 'Vroom!'

class Tiger(Animal):
    """A toy class that inherits the attributes of the Animal class.
    Parameters:
    ----------
    : num_stripes- The number of stripes on the tiger.
    Outputs:
    ----------
    What does the tiger say?
    """
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes
    def say_great(self):
        return 'Its Greeattt!'

def split_it(dataframe):

    """A function that takes a dataframe and splits into a train
    , validate, test. Test is 15% of the total, validate is 20%
    of the remainder. 
    This will return the variables of train, val, test."""
    base, test = train_test_split(dataframe, test_size=.15)
    train, val = train_test_split(base, test_size=.2)
    return train, val, test

def pipe_it(train, val, features, target):
    """A function that inputs train, val, features and target. It is
    recommended that you establish features and target as lists before
    running this function. 
    The function will break the train and validate database into the
    X and y categories, apply a Logistic Regression machine learning
    function in a pipeline. The pipeline also applies an ordinal encoder,
    an imputer, and scaler. This isn't appropriate for all machine 
    learning applications.
    The function returns the pipe, X_val, y_val variables, for easy
    scoring or graphing."""
    pipe = make_pipeline(ce.OrdinalEncoder(),
                        SimpleImputer(),
                        StandardScaler(),
                        LogisticRegression(max_iter=200))
    X_train = train[features]
    X_val = val[features]
    y_train = train[target]
    y_val = val[target]
    pipe.fit(X_train, y_train)
    return pipe, X_val, y_val

def make_df(csv):
    """A proof of concept function that turns a csv file into a 
    Pandas database."""
    df = pd.read_csv(csv)
    return df

def confuse_me(train, val, features, target):
    """A function that takes a train, validate database, with listed features
    and target. It runs this through a pipeline, and then produces a
    confusion matrix."""
    pipe, X_val, y_val = pipe_it(train, val, features, target)
    return plot_confusion_matrix(pipe, X_val, y_val, values_format='.0f', xticks_rotation='vertical')

COLORS = ('Blue', 'Orange', 'Green', 'Red', 'Black', 'Cyan', 'Purple')
