#!/usr/bin/env python
"""
lambdata - a collection of Data Science
helper functions
"""
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import category_encoders as ce
from lambdata_robdbennett import __example_module__
from lambdata_robdbennett import classes
from lambdata_robdbennett import test
from lambdata_robdbennett import lambdata_test


TEST = pd.DataFrame(np.ones(10))

