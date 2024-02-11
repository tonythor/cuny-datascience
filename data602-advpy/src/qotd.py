
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
