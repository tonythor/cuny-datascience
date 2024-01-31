##########################################################
# Q1. What will the following code display?
#     numbers = [1, 2, 3, 4, 5]
#     print(numbers[1:-5])
# Can you debug and fix the output? The code should return the entire list
numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])             #<- slicing syntax was off.
# [1, 2, 3, 4, 5]
print(numbers)                  #<- but you don't need it you're trying to print the whole list.
#[1, 2, 3, 4, 5]
##########################################################
# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

print("\nPlease enter sales data, one total per line.\n") 
dow = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] #<- no working on the weekends!
res = []
for day_num in range(len(dow)):
    sales_amount = input(f"Enter sales dollar amount for {dow[day_num]}: ")
    res.append(float(sales_amount))    
print(f"Your weekly total is: {sum(res)}")

# or for a loop
# total = 0;
# for entry in range(len(res)): 
#     total = total + res[entry]
# print(total)
#
# Output:
# Please enter sales data, one total per line.
#
# Enter sales dollar amount for Monday: 1
# Enter sales dollar amount for Tuesday: 2
# Enter sales dollar amount for Wednesday: 3
# Enter sales dollar amount for Thursday: 4
# Enter sales dollar amount for Friday: 5
# Your weekly total is: 15.0

##########################################################
#
# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
#     ● Print your list in its original order.
#     ● Use the sort() function to arrange your list in order and reprint your list.
#     ● Use the sort(reverse=True) and reprint your list.
# # Output:
lets_go = ['singapore', 'tokyo', 'denali', 'anacapa', 'newfoundland']
# In [47]: lets_go
# Out[47]: ['singapore', 'tokyo', 'denali', 'anacapa', 'newfoundland']
lets_go.sort()
# In [49]: lets_go
# Out[49]: ['anacapa', 'denali', 'newfoundland', 'singapore', 'tokyo'] 
lets_go.sort(reverse=True)
# In [51]: lets_go
# Out[51]: ['tokyo', 'singapore', 'newfoundland', 'denali', 'anacapa']      
#
##########################################################
#
# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.
courses = {
    602: {
        "instructor": "Mr. Fancy Pants",
        "room": 1024,
        "meeting_time": "1PM Mondays"
    },
    603: {
        "instructor": "Miss Jeans",
        "room": 2048,
         "meeting_time": "2PM Mondays"
    },
    605:{
        "instructor": "Mr. Johnny Black Shoes",
        "room": 512,
        "meeting_time": "3PM Mondays"
    }
}

print("Class lookup: This version supports 602, 603 and 604 only.")
course = int(input(f"Enter your course number, no spaces or commas: "))
print(courses.get(course, "Course not found"))
#
# Output:
# Class lookup: This version supports 602, 603 and 604 only.
# Enter your course number, no spaces or commas: 603
# {'instructor': 'Miss Jeans', 'room': 2048, 'meeting_time': '2PM Mondays'}
#
##########################################################
# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
#     ● look up a person’s email address,
#     ● add a new name and email address,
#     ● change an existing email address, and
#     ● delete an existing name and email address.

people = {
    "person_list": [
        {"email": "tony.fraser@gmail.com", "name": "tony.fraser"},
        {"email": "tony.fraser@nbcuni.com", "name": "tony.work"},
        {"email": "tony.fraser@cuny.edu", "name": "tony.school"}
    ]
}
# to look up:
def find_person_by_email(email):
    for person in people["person_list"]:
        if person["email"] == email:
            return person
    return None  # Return None if no matching email is found
lookup = "tony.fraser@gmail.com"
print(f"Lookup {lookup}: {find_person_by_email('tony.fraser@gmail.com')}")
# Output:
# Lookup tony.fraser@gmail.com: {'email': 'tony.fraser@gmail.com', 'name': 'tony.fraser'}
#
#to append:
people.get("person_list").append({"email": "nobody@nowhere.com", "name": "jackson.ghost"})
people
# Output:
# {'person_list': [{'email': 'tony.fraser@gmail.com', 'name': 'tony.fraser'},
#   {'email': 'tony.fraser@nbcuni.com', 'name': 'tony.work'},
#   {'email': 'nobody@nowhere.com', 'name': 'jackson.ghost'}]}
#
# to update:
def update_person_by_email(email, new_info):
    for person in people["person_list"]:
        if person["email"] == email:
            person.update(new_info)
            return True
    return False  # Return False if no matching email is found
update_person_by_email("tony.fraser@gmail.com", {"name": "Tony.F.", "email": "tony.fraser@gmail.com"})
print(f"Lookup {lookup}: {find_person_by_email('tony.fraser@gmail.com')}")
#Output
#Lookup tony.fraser@gmail.com: {'email': 'tony.fraser@gmail.com', 'name': 'Tony.F.'}


# deleting in place.
def delete_person_by_email(email):
    for person in people["person_list"][:]:  # Iterate over a copy of the list
        if person["email"] == email:
            people["person_list"].remove(person)
            return True
    return False

delete_person_by_email("tony.fraser@cuny.edu")
people
# Output
# {'person_list': [{'email': 'tony.fraser@gmail.com', 'name': 'Tony.F.'},
#   {'email': 'tony.fraser@nbcuni.com', 'name': 'tony.work'},
#   {'email': 'nobody@nowhere.com', 'name': 'jackson.ghost'}]}
# or, to delete using list comprehension, and overwriting itself.
def delete_person_by_email(email):
    people["person_list"] = [person for person in people["person_list"] if person["email"] != email]
    return people["person_list"]

people = delete_person_by_email("tony.fraser@gmail.com")
people
#
# output
[{'email': 'tony.fraser@nbcuni.com', 'name': 'tony.work'},
 {'email': 'nobody@nowhere.com', 'name': 'jackson.ghost'}]