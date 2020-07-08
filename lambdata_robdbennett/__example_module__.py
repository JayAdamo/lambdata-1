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
    return number + 1

class Animal:
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
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = num_stripes
        def say_great(self):
            return 'Its Greeattt!'

def split_it(dataframe):
   base, test = train_test_split(dataframe, test_size=.15)
   train, val = train_test_split(base, test_size=.2)
   return train, val, test

def pipe_it(train, val, features, target):
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
    df = pd.read_csv(csv)
    return df

def confuse_me(train, val, features, target):
    pipe, X_val, y_val = pipe_it(train, val, features, target)
    return plot_confusion_matrix(pipe, X_val, y_val, values_format='.0f', xticks_rotation='vertical');