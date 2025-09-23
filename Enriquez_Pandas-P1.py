#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # Experiment 3: Python Data Analysis (Pandas)


# ## Problem 1


import pandas as pd
cars = pd.read_csv('cars.csv') # cars spreadsheet data set loaded to here
cars

cars.head() #This displays the first five of the list

cars.tail() #This displays the last five of the list