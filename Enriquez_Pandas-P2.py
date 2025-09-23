#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ## Problem 2


#a. First 5 rows with odd-numbered columns
cars.iloc[:5, ::2]

#b. Row with Model of 'Mazda RX4'
cars[cars['Model'] == 'Mazda RX4']


#c. Camaro Z28 Cylinders
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

#d. Selected models
cars.loc[cars['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']),['Model','cyl','gear']]