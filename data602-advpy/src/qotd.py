
# 1. Create a list called animals that contain the following: cat, dog, manta ray, horse, crouching tiger
animals = ['cat', 'dog', 'manta ray', 'horse', 'crouching tiger']
print(animals)

# 2. Repeat question 1 and loop through and print each item in the animal list by iterating through an index number and using range(). 
# Set a variable len_animals to the length of the animal list.
len_animals = len(animals)
for i in range(len_animals):
    print(animals[i])

# 3. Programmatically reorganize the countdown list below in descending order and return the value of the 5th element in the sorted countdown list.
countdown = [9, 8, 7, 5, 4, 2, 1, 6, 10, 3, 0, -5]
countdown.sort(reverse=True)
print(f"countdown after the sort {countdown}")
the_fifth_element = countdown[4]
print(f"the fifth element = {the_fifth_element}")

#4. Write a program to add item 7000 after 6000 in the following Python List
# Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)


# 5. Write a program to remove all occurrences of item 20 in the following list.
list2 = [5, 20, 30, 15, 20, 30, 20]
print([item for item in list2 if item != 20])

# 6. Using the following dictionary .. (Use python to solve for the answer.)
dict = {"Course": "DATA 606", "Program": "MSDS", "School": "CUNYSPS"}
dict
# 6a. What is the name of the course?
# there is no name attribute

# 6b. Change the course to DATA602
dict['Course'] = "DATA602"
dict

# 6c. Add new information to the dictionary - "Professor" with "Schettini"
dict['Professor'] = "Schettini"
dict

# 6d. Using the len function, find how many keys there are in the dictionary. 
print(len(dict.keys()))


# 7.  Write a Python program to change Brad’s salary to 7500 in the following dictionary.
sample_dict = {
    'emp1': {'name': 'Amanda', 'salary': 8200},
    'emp2': {'name': 'John', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 700}
}
sample_dict['emp3']['salary'] = 7500
sample_dict


	
#1. Write a function to calculate the area and perimeter of a rectangle.
def calc_area(base: float, height: float):
    return {"perimeter": 2 * base * height, "area": base * height}
print(calc_area(base= 4, height=6))

#2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.
def odd_or_even(number): 
    return "false" if number % 2 else "true"  # even % 2 = zero, which is falsy
print(f"{odd_or_even(3)}")
print(f"{odd_or_even(16)}")

#3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
import re
def case_counter(mystr) -> dict:
    ## remove spaces and characters
    pattern = "[^a-zA-Z0-9]"
    replacement = "" # this replaces the matched text with an empty string
    chars_only = re.sub(pattern, "", mystr) 
    upper_case = len([t for t in chars_only if t.isupper()])
    lower_case = len(chars_only) - upper_case
    return {"string" : mystr, "chars_only": chars_only, "upper_case_count": upper_case, "lower_case_count" : lower_case}
print(case_counter("CUNY sps"))
print(case_counter("CUNYsps"))
print(case_counter("TwoUpper"))

#4. Write a Python function to sum all the numbers in a list
import re
def sum_my_list(my_list: list) -> int: 
    just_numbers = [x for x in my_list if type(x) == int]
    return sum(just_numbers)
print(sum_my_list(["no", 1,3,-3]))


def is_var(var_name):
    return var_name in globals() or var_name in locals()
global_var= 10
def my_function():
    local_var = 5
    print("## Local scope, all is set.")
    print(f"global_var: {global_var}")
    print(f"local_var: {local_var}")

my_function()

print("## Global scope")
print(f"Is global var set? Yes. global_var: {global_var}")
print(f"Is local_var set? {is_var('local_var')}")



#6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number} 


########
#1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.



#2. What is the ndarray in numPy?



#3. Create a 1D array of numbers from 0 to 9 
#Desired Output: array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


#4. Extract all odd numbers from array1 
#array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


#5. Get the common items between a and b  
#input
#a = np.array([1,2,3,2,3,4,3,4,5,6])
#b = np.array([7,2,10,2,7,4,9,4,9,8])
#Desired Output:
#array([2, 4])
#6. From array a remove all items present in array b 

#Input:

#a = np.array([1,2,3,4,5])
#b = np.array([5,6,7,8,9])

#Desired Output:

#array([1,2,3,4])


#7. Find out if iris has any missing values. 



# Input
#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])



#1. What are the similarities and differences between pandas and numpy?   Include some type of example with code.

"""
They are both python libraries used for data manipulation, but they mostly do different things. Numpy is low-level number-crunching system mostly, think of linear algebra, scientific math, and multiplying math matrices together. Pandas is more widely used as columnar format data manipulation, think anything you can do in excel, but a whole lot more, and with a whole lot more excel sheets at the same time.

Most in this field probably don't know a lot about Numpy, but most of Pandas's math functionality runs on the Numpy API. 
Pandas is huge and maybe it's all you need most of the time, but know that your code is most likely running through Numpy.


Here's a simple example.


In [1]: import numpy as np
   ...: import pandas as pd
   ...:
   ...: # Caffeine content in ounces
   ...: # Diet Drinks, Energy Drinks, Sugar-Free Drinks
   ...: np_caffeine = np.array([[12, 10, 8], [30, 35, 40], [10, 12, 15]])
   ...:
   ...: # Creating a DataFrame with Pandas
   ...: pd_caffeine = pd.DataFrame(np_caffeine,
   ...:                            columns=["Drink 1", "Drink 2", "Drink 3"],
   ...:                            index=["Diet Drinks", "Energy Drinks", "Sugar
   ...: -Free Drinks"])
   ...:
   ...: # Example Operation: Calculating the average caffeine content for each c ategory
   ...: # Using NumPy
   ...: np_mean_caffeine = np.mean(np_caffeine, axis=1)
   ...:
   ...: # Using Pandas
   ...: pd_mean_caffeine = pd_caffeine.mean(axis=1)
   ...:
   ...: print("Average Caffeine Content with NumPy:", np_mean_caffeine)
   ...: print("Average Caffeine Content with Pandas:\n", pd_mean_caffeine)
Average Caffeine Content with NumPy: [10.         35.         12.33333333]
Average Caffeine Content with Pandas:
 Diet Drinks          10.000000
Energy Drinks        35.000000
Sugar-Free Drinks    12.333333
dtype: float64



2. What is the ndarray in numPy?

N-dimensional-array, aka ndarray,  is the most core structure in numpy. To use this data type, you load data and then put it into one of these ndarrays. From there, the ndarray is an engine. You can ue it to slice, index, search, apply math, etc. And it's fast. NDArray was designed with one thing in mind, to be fast. 



3. Create a 1D array of numbers from 0 to 9 
Desired Output:  array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

## 3 answer ## 
In [5]: import numpy as np
   ...:
   ...: array_range = np.arange(10)
   ...: print(array_range)
[0 1 2 3 4 5 6 7 8 9]


## 4. Extract all odd numbers from array1 
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

## 4 answer ## 
[x for x in array1 if x % 2 != 0]


## 5. Get the common items between a and b  
#input
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#Desired Output:
array([2, 4])

## 5 answer ## 
In [13]: common_elements = np.intersect1d(a, b)
    ...: print(common_elements)
[2 4]



6. From array a remove all items present in array b 
#Input:
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
#Desired Output:
array([1,2,3,4])

## 6 answer ## 
result = np.setdiff1d(a, b)
print(result)



7. Find out if iris has any missing values. 
# Input
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

I don't think it's missing anything, but I'm not really sure.  Usually if you're asking for missing data it's either from a time series, or it's n records from population N. This is neither of those. It could e missing a field within a row, so we can check for that.

Also, pandas understands the structure within the csv reader, so I used that.


In [36]: import pandas as pd
In [37]: url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
In [38]: iris = pd.read_csv(url)
In [39]: pd.isnull(iris).any()
Out[39]:
5.1            False
3.5            False
1.4            False
0.2            False
Iris-setosa    False
dtype: bool



"""


# 1. What is pandas and why use it?

# 2. Give an example of how to import a csv file using pandas
# use the read_csv method.
df = pd.data_frame() 

# 3. Show how to view the first 10 rows of a dataset using pandas

# 4. Write a Pandas program to compare the elements of the two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]

# 5. Change the first character of each word to upper case in each word of df1
# df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])



# 1. What is pandas and why use it?

# According to the makers of Pandas, "Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# built on top of the Python programming language." To me, it's one of the primary python columnar data store systems that many technologies build on top of. Many tools sit on to of Pandas, including Seaborn, Prophet, etc. 

# 2. Give an example of how to import a csv file using pandas
# 3. Show how to view the first 10 rows of a dataset using pandas
In [1]: import pandas as pd
   ...: usecols = ['Age', 'Citizenship', 'Position', 'Fate']
   ...: lusitania = pd.read_csv("https://raw.githubusercontent.com/tonythor/cuny-datascience/develop/data/lusitania_manifest.csv", usecols=usecols)
   ...: lusitania.head(10)
Out[1]:
    Fate   Age      Citizenship              Position
0   Lost    38          British                   NaN
1   Lost    37          British                   NaN
2  Saved    30          British                Violin
3  Saved    25          British                 Cello
4  Saved    27          British           Double Bass
5   Lost    48          British         Staff Captain
6   Lost   NaN        Norwegian    Able-Bodied Seaman
7  Saved   NaN  British (Irish)    Able-Bodied Seaman
8  Saved    24  British (Irish)  Junior Third Officer
9  Saved  19 ?          British    Able-Bodied Seaman


# 4. Write a Pandas program to compare the elements of the two Pandas Series.
In [3]: import pandas as pd
   ...: def compare_series(series1, series2):
   ...:     # Check if the series are of the same length
   ...:     if len(series1) != len(series2):
   ...:         return False
   ...:     for elem1, elem2 in zip(series1, series2):
   ...:         if elem1 != elem2:
   ...:             return False
   ...:     return True
   ...:
   ...: series1 = pd.Series([2, 4, 6, 8, 10])
   ...: series2 = pd.Series([1, 3, 5, 7, 10])
   ...: series3 = pd.Series([2, 4, 6, 8, 10])
   ...: print(compare_series(series1, series2))
   ...: print(compare_series(series1, series3))
   ...:
False
True


# 5. Change the first character of each word to upper case in each word of df1
import pandas as pd
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
df1 = df1.apply(lambda x: x.capitalize())
print(df1)



import pandas as pd
usecols = ['Age', 'Citizenship', 'Position', 'Fate']
lusitania = pd.read_csv("https://raw.githubusercontent.com/tonythor/cuny-datascience/develop/data/lusitania_manifest.csv", usecols=usecols)
lusitania.head(10)

# Resetting the index (and dropping the old one)
lusitania.reset_index(drop=True, inplace=True)
# Dropping the  'Position' column
lusitania.drop('Position', axis=1, inplace=True)
# Deleting the first row (which has index 0 after resetting index)
lusitania.drop(0, axis=0, inplace=True)
# Display the modified DataFrame
lusitania.head(10)


# let's do some aggregations .
band_members = ['Cello', 'Double Bass', 'Violin']


kitchen_staff = ['Assistant Baker', 'Assistant Butcher', 'Assistant Cook', 'Assistant Matron', 
                 'Assistant Pantry Steward', 'Chief Baker', 'Chief Butcher', 'Chef', 
                 'Confectioner', 'Extra Chief Steward', 'Extra Extra Second Baker', 'Extra Extra Second Cook', 
                 'Extra Fourth Baker', 'Extra Second Baker', 'Extra Second Cook', 'Extra Third Baker', 
                 'Extra Third Cook', 'Extra Vegetable Cook', 'Fourth Baker', 'Grill Cook', 'Kitchen Porter', 
                 'Larder Cook', "Night Fireman's Cook", 'Passenger Cook', 'Roast Cook', 'Sauce Cook', 
                 'Scullion', 'Second Baker', 'Second Butcher', "Ship's Cook", 'Soup Cook', 'Stewardess', 
                 'Third Baker', 'Third Butcher', 'Third Cook', 'Vegetable Cook']

wait_staff = ['Assistant Deck Steward', 'Assistant Smokeroom Steward', 'Assistant Steward (Waiter)', 
              'Barkeeper', 'Deck Steward', 'Deck Steward, Second Cabin', 'First Waiter', 
              'First Waiter (Head Waiter)', 'Library Steward', 'Linenkeeper', 'Lounge Steward', 
              'Night Watchman', 'Pantry Steward', 'Saloon Cabin Bed Steward', 'Saloon Steward', 
              'Second Cabin Cabin Bed Steward', 'Second Steward', 'Second Waiter', 'Smokeroom Barkeeper', 
              'Smokeroom Steward', "Steward's Boy", 'Third Waiter', 'Waiter']

kitchen_staff = ['Assistant Baker', 'Assistant Butcher', 'Assistant Cook', 'Assistant Matron', 
                 'Assistant Pantry Steward', 'Chief Baker', 'Chief Butcher', 'Chef', 
                 'Confectioner', 'Extra Chief Steward', 'Extra Extra Second Baker', 'Extra Extra Second Cook', 
                 'Extra Fourth Baker', 'Extra Second Baker', 'Extra Second Cook', 'Extra Third Baker', 
                 'Extra Third Cook', 'Extra Vegetable Cook', 'Fourth Baker', 'Grill Cook', 'Kitchen Porter', 
                 'Larder Cook', "Night Fireman's Cook", 'Passenger Cook', 'Roast Cook', 'Sauce Cook', 
                 'Scullion', 'Second Baker', 'Second Butcher', "Ship's Cook", 'Soup Cook', 'Stewardess', 
                 'Third Baker', 'Third Butcher', 'Third Cook', 'Vegetable Cook']

ship_crew = ['Able-Bodied Seaman', 'Captain', 'Chief Officer', 'First Officer', 
             'Fireman', 'Junior Third Officer', 'Leading Fireman', 'O Seaman', 
             'Purser', 'Second Officer', 'Senior Third Officer', 'Seaman', 
             'Staff Captain', 'Telegraphist', 'Assistant Telegraphist']

maintenance_staff = ['Baggage Master', 'Boatswain', "Boatswain's Boy", "Boatswain's Mate", 
                     'Carpenter', 'Donkeyman', 'Electric Attendant', 'Engineering Storekeeper', 
                     'Greaser', 'Inspector', 'Joiner', 'Junior 4th Engineer', 'Junior 5th Engineer', 
                     'Junior 6th Engineer', 'Junior 7th Engineer', 'Master-at-Arms', 'Plumber', 
                     'Refrigeration Greaser', 'Senior Boilermaker', 'Steering Engineer', 
                     'Trimmer', 'Trimmer (promoted to Fireman)', 'Ventilation Engineer']

engineering_technical_staff = ['Chief Electrician', 'Chief Engineer', 'First Intermediate 3rd Engineer', 
                               'First Junior 3rd Engineer', 'First Senior 3rd Engineer', 
                               'Intermediate 2nd Engineer', 'Intermediate 5th Engineer', 
                               'Intermediate 6th Engineer', 'Second Electrician', 'Second Intermediate 3rd Engineer', 
                               'Senior 2nd Engineer', 'Senior 4th Engineer', 'Senior 5th Engineer', 
                               'Senior 6th Engineer', 'Senior 7th Engineer', 'Second Senior 3rd Engineer', 
                               'Third Electrician', 'Third Junior 3rd Engineer', 'Third Senior 3rd Engineer']


navigation_staff = ['Deck Engineer', 'First Officer', 'Junior Third Officer', 'Second Officer', 
                    'Senior Third Officer', 'Staff Captain']


general_services = ['Barber', 'Boots Steward', 'Cellarman', 'Deck Steward, Second Cabin', 
                    'Library Steward', 'Linenkeeper', 'Lounge Steward', 'Pantry Steward', 
                    'Smokeroom Barkeeper', 'Smokeroom Steward', 'Typist']




kitchen_staff = [
    "Assistant Baker",
    "Assistant Butcher",
    "Assistant Cook",
    "Assistant Matron",
    "Assistant Pantry Steward",
    "Chief Baker",
    "Chief Butcher",
    "Chef",
    "Confectioner",
    "Extra Chief Steward",
    "Extra Extra Second Baker",
    "Extra Extra Second Cook",
    "Extra Fourth Baker",
    "Extra Second Baker",
    "Extra Second Cook",
    "Extra Third Baker",
    "Extra Third Cook",
    "Extra Vegetable Cook",
    "Fourth Baker",
    "Grill Cook",
    "Kitchen Porter",
    "Larder Cook",
    "Night Fireman's Cook",
    "Passenger Cook",
    "Roast Cook",
    "Sauce Cook",
    "Scullion",
    "Second Baker",
    "Second Butcher",
    "Ship's Cook",
    "Soup Cook",
    "Stewardess",
    "Third Baker",
    "Third Butcher",
    "Third Cook",
    "Vegetable Cook",
]

wait_staff = [
    "Assistant Deck Steward",
    "Assistant Smokeroom Steward",
    "Assistant Steward (Waiter)",
    "Barkeeper",
    "Deck Steward",
    "Deck Steward, Second Cabin",
    "First Waiter",
    "First Waiter (Head Waiter)",
    "Library Steward",
    "Linenkeeper",
    "Lounge Steward",
    "Night Watchman",
    "Pantry Steward",
    "Saloon Cabin Bed Steward",
    "Saloon Steward",
    "Second Cabin Cabin Bed Steward",
    "Second Steward",
    "Second Waiter",
    "Smokeroom Barkeeper",
    "Smokeroom Steward",
    "Steward's Boy",
    "Third Waiter",
    "Waiter",
]

kitchen_staff = [
    "Assistant Baker",
    "Assistant Butcher",
    "Assistant Cook",
    "Assistant Matron",
    "Assistant Pantry Steward",
    "Chief Baker",
    "Chief Butcher",
    "Chef",
    "Confectioner",
    "Extra Chief Steward",
    "Extra Extra Second Baker",
    "Extra Extra Second Cook",
    "Extra Fourth Baker",
    "Extra Second Baker",
    "Extra Second Cook",
    "Extra Third Baker",
    "Extra Third Cook",
    "Extra Vegetable Cook",
    "Fourth Baker",
    "Grill Cook",
    "Kitchen Porter",
    "Larder Cook",
    "Night Fireman's Cook",
    "Passenger Cook",
    "Roast Cook",
    "Sauce Cook",
    "Scullion",
    "Second Baker",
    "Second Butcher",
    "Ship's Cook",
    "Soup Cook",
    "Stewardess",
    "Third Baker",
    "Third Butcher",
    "Third Cook",
    "Vegetable Cook",
]

ship_crew = [
    "Able-Bodied Seaman",
    "Captain",
    "Chief Officer",
    "First Officer",
    "Fireman",
    "Junior Third Officer",
    "Leading Fireman",
    "O Seaman",
    "Purser",
    "Second Officer",
    "Senior Third Officer",
    "Seaman",
    "Staff Captain",
    "Telegraphist",
    "Assistant Telegraphist",
]

maintenance_staff = [
    "Baggage Master",
    "Boatswain",
    "Boatswain's Boy",
    "Boatswain's Mate",
    "Carpenter",
    "Donkeyman",
    "Electric Attendant",
    "Engineering Storekeeper",
    "Greaser",
    "Inspector",
    "Joiner",
    "Junior 4th Engineer",
    "Junior 5th Engineer",
    "Junior 6th Engineer",
    "Junior 7th Engineer",
    "Master-at-Arms",
    "Plumber",
    "Refrigeration Greaser",
    "Senior Boilermaker",
    "Steering Engineer",
    "Trimmer",
    "Trimmer (promoted to Fireman)",
    "Ventilation Engineer",
]

engineering_technical_staff = [
    "Chief Electrician",
    "Chief Engineer",
    "First Intermediate 3rd Engineer",
    "First Junior 3rd Engineer",
    "First Senior 3rd Engineer",
    "Intermediate 2nd Engineer",
    "Intermediate 5th Engineer",
    "Intermediate 6th Engineer",
    "Second Electrician",
    "Second Intermediate 3rd Engineer",
    "Senior 2nd Engineer",
    "Senior 4th Engineer",
    "Senior 5th Engineer",
    "Senior 6th Engineer",
    "Senior 7th Engineer",
    "Second Senior 3rd Engineer",
    "Third Electrician",
    "Third Junior 3rd Engineer",
    "Third Senior 3rd Engineer",
]


navigation_staff = [
    "Deck Engineer",
    "First Officer",
    "Junior Third Officer",
    "Second Officer",
    "Senior Third Officer",
    "Staff Captain",
]


general_services = [
    "Barber",
    "Boots Steward",
    "Cellarman",
    "Deck Steward, Second Cabin",
    "Library Steward",
    "Linenkeeper",
    "Lounge Steward",
    "Pantry Steward",
    "Smokeroom Barkeeper",
    "Smokeroom Steward",
    "Typist",
]


## let's use the same dataset we used last week.
import pandas as pd
usecols=['Fate', 'Department/Class', 'Passenger/Crew', 'Adult/Minor', 'Sex', 'Position']
cuny  = "https://raw.githubusercontent.com/tonythor/cuny-datascience"
lusitania = pd.read_csv(f"{cuny}/develop/data/lusitania_manifest.csv") 
lusitania.columns = lusitania.columns.str.lower().str.replace(' ', '_').str.replace('/', '_')

# 1. How would you delete:
## An index from your dataframe
lusitania = lusitania.reset_index(drop=True)
# A column from your dataframef
lusitania = lusitania.drop('position', axis=1)
    # A row from your dataframe
lusitania = lusitania.drop(0, axis=0)

# 2. How do you iterate over a pandas dataframe?
for  row in lusitania.iterrows():
    print(f"Row:{row}")

# 3. How would you convert a string to a date?    
from datetime import datetime
moon_landing = "1969-07-16"
d = datetime.strptime(moon_landing, "%Y-%m-%d").date() #<- not a datetime! 
print(type(d))

# 4. What is data aggregation?  Give an example in Python. 
# It's rolling up data. You might want reduce hourly data to daily data, 
# or something more like groupBy().count(). GroupBy/count or GroupBy/Sum
# are probably the two most common types of aggregations. 

sex_count = lusitania.groupby('sex').size()
print(sex_count)
# sex
# Female     518
# Male      1443



# 5. What is GroupBy in Pandas (groupby()). Give an example in Python.
# let's use groupby and bins together.
lusitania_age = (
    lusitania['age']
    .pipe(pd.to_numeric, errors='coerce')  # Convert 'age' to numeric, coerce errors to NaN
    .dropna()                              # Drop NaN values
    .astype(int)                           # Convert remaining 'age' values to integers
)

bins = range(0, max(lusitania_age) + 10, 10)
labels = [f"{i}-{i+9}" for i in range(0, max(lusitania_age), 10)]
age_groups = pd.cut(lusitania_age, bins=bins, labels=labels, right=False)
age_group_counts = age_groups.value_counts().sort_index()
print(age_group_counts)
# age
# 0-9       73
# 10-19     73
# 20-29    337
# 30-39    389
# 40-49    212
# 50-59    117
# 60-69     28
# 70-79      6
# Name: count, dtype: int64



# 1. What is matplottlib and seaborn?  When would you choose one over the other?

# Matplotlib is like a basic art set for graph drawing in Python. It's great for simple and customizable graphs, like lines and dots. Seaborn is like an advanced art kit that builds on Matplotlib. It makes fancier and more complex graphs easier, like those showing trends in lots of data. When to choose which? Use Matplotlib for simple graphs. When you have lots of data and want nicer looking graphs without much extra work, go for Seaborn.


# 2. Image you are creating a visualization for a presentation at work.  What are some recommendations or guidelines you would follow to make engaging and informative visuals?

# I have a few suggestions for graphics.
# 1. Simple is better. If your high school child can't understand it, it's probably not done.
# 2. Don't need to show everything, just show what you need to show.
# 3. Use colors and legends to make things crystal clear.
# 4. Use tangible metrics and labels. "$1.2BN" is easier to read on a chart than "1200000000" or "1.2e9"


# 3. Give an example of either a matplotlib or seaborn graphic (give code). 

# Here's a simple but super clear example you can cut and paste. 
import pandas as pd
import matplotlib.pyplot as plt
cuny  = "https://raw.githubusercontent.com/tonythor/cuny-datascience"
lusitania = pd.read_csv(f"{cuny}/develop/data/lusitania_manifest.csv") 
lusitania.columns = lusitania.columns.str.lower().str.replace(' ', '_').str.replace('/', '_')
lusitania['age_group'] = pd.cut(
    lusitania['age'].pipe(pd.to_numeric, errors='coerce'), 
    bins=bins, 
    labels=labels, 
    right=False
)
grouped_data = lusitania.groupby(['fate', 'age_group']).size().unstack(fill_value=0)
grouped_data.T.plot(kind='bar', stacked=False)
plt.xlabel('Age Groups')
plt.ylabel('Count')
plt.title('Survival Count by Age Group')
plt.show()

# 4. Read the following: https://speedwell.com.au/en/insights/2019/the-manifesto-of-the-data-ink-ratio  What is the data-ink ratio? 

# It's the fictitious percentage of ink on a chart that is for showing data, versus for not showing data. The concept is -- use your ink to show data and don't use any ink to show stuff that's not data. 

# How can you use python libraries such as matplotlib, seaborn, plotly, etc. to incorporate this data-ink ratio in your visualizations?
#
# I don't quite understand the wording of that question. I think a better question is, with respect to the data-ink ratio, what can we do with our plots and charts to make graphics more legible. The answer is pretty simple, keep the chart to just the fact you are trying to show. Filter out everything that isn't exactly what you want to show. If your graphic is exploratory and you're not showing something specific, even then show just the exploratory data you are showcasing and nothing else (except labels and legends) 



# 1. How do you plot a histogram in Seaborn?  
# 2. Plot a histogram with NAs dropped.
# 3. How do you set the color for a histogram?
import pandas as pd
import seaborn as sns 
from sodapy import Socrata
import matplotlib.pyplot as plt
client = Socrata("data.cityofnewyork.us", None)
results = client.get("pvqr-7yc4", limit=5000)
results_df = pd.DataFrame.from_records(results) 
results_df['vehicle_year'] = pd.to_numeric(results_df['vehicle_year'], errors='coerce')
filtered_df = results_df[(results_df['vehicle_year'] >= 1920) & (results_df['vehicle_year'] <= 2024)]
cleaned_df = filtered_df.dropna(subset=['vehicle_year']) #<- drop NA
plt.figure(figsize=(10, 6))
sns.histplot(cleaned_df['vehicle_year'], bins=(2024 - 1920), kde=False, color="olive") #<- army green
plt.title('Histogram of Vehicle Years in Violations Data (1920-2024)')
plt.xlabel('Vehicle Year')
plt.ylabel('Frequency')
plt.show()


# 4.  What type of plot would allow you to compare two continuous features?  
## Scatterplots, maybe feet from curb, to year of car? Maybe older cars are further from the curb.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cleaned_df['feet_from_curb'] = pd.to_numeric(cleaned_df['feet_from_curb'], errors='coerce')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='vehicle_year', y='feet_from_curb', data=cleaned_df)
plt.title('Vehicle Year vs. Feet From Curb')
plt.xlabel('Vehicle Year')
plt.ylabel('Feet From Curb')
plt.show()

# 5. Give example of a correlation plot.
# 6. Change the figure size of your plot(s).
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
cleaned_df_is_numeric = cleaned_df.apply(pd.to_numeric, errors='coerce')
cleaned_df_is_numeric = cleaned_df_is_numeric.dropna(axis=1, how='all')
correlation_matrix = cleaned_df_is_numeric.corr()
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", center=0, linewidths=0.5, linecolor='black')
plt.title('Correlation Matrix of Numeric Features')
plt.show()


