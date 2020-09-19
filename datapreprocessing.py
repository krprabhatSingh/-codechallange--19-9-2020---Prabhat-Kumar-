# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import relevant packages
import numpy as np
import pandas as pd 
import matlplotlib.pyplot as plt

# Import the dataset 

healthData = pd.read_csv('Data_for_BMI_Calculator_Height_Weight.csv')

# Seperate the data with features and labels

X = healthData.iloc[:,:-1].values
y = healthData.iloc[:,3].values

# Deal with the Missing values
# We can use class Imputer to deal with missing values

missingValueImputer = Imputer(missing_value = 'NaN', Strategy = 'mean', axis = 0)

missingValueImputer = missingValueImputer.fit(X[:,1:3])

X[:,1:3] = missingValueImputer.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder
X_labelencoder = LabelEncoder()
X[:,0] = X_labelencoder.fit_transform(x[:,0])

# Remove the Mathematical weightage : 

from sklearn.preprocessing import OneHotEncoder

X_ohe = OneHotEncoder(Categorical_features = [0])
X = X_ohe.fit_transform(X).toarray()

# Creating training and testing data splits : 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size = 0.2, 
                                                    random_state = 0)

# generalize the magniture : 

from sklearn.preprocessing import standardSclar
scale = StandardScalar()
X_train = Scale.fit_transform(X_train)
X_test = Scale.fit_transform(X_test)

