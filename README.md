## **PROBLEM 1: LOADING AND DISPLAYING DATA**
```
import pandas as pd
cars = pd.read_csv('cars.csv') 
cars
cars.head()
cars.tail()
```

The first line,

```
import pandas as pd
```

brings the pandas library into the program and gives it the alias `pd`. This is a standard convention that makes it easier to call pandas functions later without typing the full word `pandas`.

Next,

```
cars = pd.read_csv("cars.csv")
```

reads the file `cars.csv` and stores it into a Data frame named `cars`. A Data frame is essentially a table with rows and columns, and it is the core data structure in pandas for handling datasets.

The following line,

```
cars.head()
```

displays the first five rows of the Data frame. This is usually done to check if the data has been loaded properly and to see what the top of the dataset looks like.

Similarly,

```
cars.tail()
```

shows the last five rows of the Data frame. Printing both the top and bottom of the dataset gives a quick overview of how the data is structured from beginning to end. Then save as .py

---

## **PROBLEM 2: SUBSETTING, SLICING, AND INDEXING**

```
cars.iloc[:5, ::2]
cars[cars['Model'] == 'Mazda RX4']
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
cars.loc[cars['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']),['Model','cyl','gear']]
```

The first question of the problem begins with the line

```
cars.iloc[:5, ::2]
```

which uses the `.iloc` indexer to select data by row and column positions. The slice `:5` selects the first five rows, while the slice `::2` picks every other column, starting with the first one. The result displays the first five rows but only the odd-numbered columns.

Next,

```
cars[cars['Model'] == 'Mazda RX4']
```

creates a condition that checks where the `Model` column equals “Mazda RX4.” This condition is applied as a filter to the Data frame, so that only the row corresponding to the Mazda RX4 model is displayed.

Next, this next line, which is:

```
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```

uses `.loc` to locate the row where the `Model` is “Camaro Z28” , then select both the `Model` and `cyl` columns from that row. This indicates the number of cylinders of "Camaro Z28"

For the final part of problem 2, the line

```
cars.loc[cars['Model'].isin(models), ['Model','cyl','gear']]
```

checks whether each value in the `Model` column is one of the names in the list using `.isin(models)`. It then filters the Data frame to include only those rows. Finally, it selects just three columns—`Model`, `cyl`, and `gear`. This displays both the number of cylinders and the gear type for each of the three specified car models.
After all of this, save this problem as a .py file


____________________________________

**REVISION #1**

For problem 1 & 2, after executing all of the syntaxes, save the file problems as .py

**REVISION #2(ADDED COMMENTS)**

## **PROBLEM 1: LOADING AND DISPLAYING DATA**
```
import pandas as pd
cars = pd.read_csv('cars.csv') # cars spreadsheet data set loaded to here
cars
cars.head()
cars.tail()
```

The first line,

```
import pandas as pd
```

brings the pandas library into the program and gives it the alias `pd`. This is a standard convention that makes it easier to call pandas functions later without typing the full word `pandas`.

Next,

```
cars = pd.read_csv("cars.csv") # cars spreadsheet data set loaded to here
```

reads the file `cars.csv` and stores it into a Data frame named `cars`. A Data frame is essentially a table with rows and columns, and it is the core data structure in pandas for handling datasets.

The following line,

```
cars.head()  #This displays the first five of the list
```

displays the first five rows of the Data frame. This is usually done to check if the data has been loaded properly and to see what the top of the dataset looks like.

Similarly,

```
cars.tail() #This displays the last five of the list
```

shows the last five rows of the Data frame. Printing both the top and bottom of the dataset gives a quick overview of how the data is structured from beginning to end. Then save as .py

---

## **PROBLEM 2: SUBSETTING, SLICING, AND INDEXING**

```
cars.iloc[:5, ::2] #a. First 5 rows with odd-numbered columns
cars[cars['Model'] == 'Mazda RX4'] #b. Row with Model of 'Mazda RX4'
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']] #c. Camaro Z28 Cylinders
cars.loc[cars['Model'].isin(['Mazda RX4', 'Ford Pantera L', 'Honda Civic']),['Model','cyl','gear']] #d. Selected models
```

The first question of the problem begins with the line

```
cars.iloc[:5, ::2] #a. First 5 rows with odd-numbered columns
```

which uses the `.iloc` indexer to select data by row and column positions. The slice `:5` selects the first five rows, while the slice `::2` picks every other column, starting with the first one. The result displays the first five rows but only the odd-numbered columns.

Next,

```
cars[cars['Model'] == 'Mazda RX4'] #b. Row with Model of 'Mazda RX4'
```

creates a condition that checks where the `Model` column equals “Mazda RX4.” This condition is applied as a filter to the Data frame, so that only the row corresponding to the Mazda RX4 model is displayed.

Next, this next line, which is:

```
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']] #c. Camaro Z28 Cylinders
```

uses `.loc` to locate the row where the `Model` is “Camaro Z28” , then select both the `Model` and `cyl` columns from that row. This indicates the number of cylinders of "Camaro Z28"

For the final part of problem 2, the line

```
cars.loc[cars['Model'].isin(models), ['Model','cyl','gear']] #d. Selected models
```

checks whether each value in the `Model` column is one of the names in the list using `.isin(models)`. It then filters the Data frame to include only those rows. Finally, it selects just three columns—`Model`, `cyl`, and `gear`. This displays both the number of cylinders and the gear type for each of the three specified car models.
After all of this, save this problem as a .py file

