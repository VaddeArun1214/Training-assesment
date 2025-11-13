**Python Concepts Summary**

**Python Basic Datatypes**

Python has built-in types like int, float, str, and bool. They store simple values and form the foundation for all operations.

Example:

x = 10   # int

y = 3.14   # float

name = 'Arun'  # str



**List Manipulation**

Lists are mutable ordered collections that can store mixed data types. We can add, remove, or modify elements easily.

Example:

nums = \[1, 2, 3]

nums.append(4)

nums\[1] = 10



**Tuple and Set Operations**

Tuples are immutable lists, while sets store unique unordered items. Sets are great for removing duplicates or doing union/intersection.

Example:

t = (1, 2, 3)

s1, s2 = {1, 2, 3}, {3, 4, 5}

print(s1 | s2)  # Union → {1, 2, 3, 4, 5}



**Dictionary Comprehension**

Dictionaries store key–value pairs. Comprehensions provide a quick way to build them dynamically.

Example:

nums = \[1, 2, 3]

squares = {x: x\*\*2 for x in nums}



**NumPy Array Manipulation**

NumPy arrays are efficient for numerical operations on large datasets. They support element-wise math and reshaping easily.

Example:

import numpy as np

arr = np.arange(1, 6)

print(arr \* 2)  # \[2 4 6 8 10]



**Pandas Series – Creating and Indexing**

A Series is a one-dimensional labeled array. You can create it from lists, arrays, or dictionaries and access values by index.

Example:

import pandas as pd

s = pd.Series(\[10, 20, 30], index=\['a', 'b', 'c'])

print(s\['b'])  # 20





**Pandas DataFrame and Filtering**

DataFrames are 2D labeled tables (like Excel sheets). You can filter rows using conditions or column values.

Example:

df = pd.DataFrame({'Name': \['A', 'B'], 'Age': \[25, 30]})

print(df\[df\['Age'] > 25])





**DataFrame Plotting**

Pandas integrates with Matplotlib to create quick visualizations. You can plot columns directly to analyze trends.

Example:

df\['Age'].plot(kind='bar', title='Age Chart')





**OOP – Class and Inheritance**

Classes define objects with attributes and methods; inheritance lets one class reuse another’s features.

Example:

class Vehicle:

&nbsp;   def move(self): print('Moving')



class Car(Vehicle):

&nbsp;   def wheels(self): print('Has 4 wheels')



Car().move()





**OOP – Encapsulation and Methods**

Encapsulation hides data using private attributes and public methods for control.

Example:

class Bank:

&nbsp;   def \_\_init\_\_(self):

&nbsp;       self.\_\_balance = 1000

&nbsp;   def get\_balance(self):

&nbsp;       return self.\_\_balance

