## By Tony Fraser
## 31 January 2024

# Q1 Fix all the syntax and logical errors in the given source code 
# add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95

test1 = int(input('Enter the score for test 1: ')) #<- TF converted these to ints
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: ')) #<- TF needed to add test 3

# Calculate the average test score.
average = (test1 + test2 + test3) / 3              #<- TF added parentheses 
# Print the average.
print('The average score is', average)

if average >= HIGH_SCORE:                          #<- TF changed case to look like static on top
    print('Congratulations!')
    print('That is a great average!')              #<- TF added indent, otherwise it prints every time

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

print("\n")
print("We're going to find the area of a bunch of rectangles.") 
print("When asked, enter a length,width. Just enter the numbers with a comma between, no extra spaces.")
print("Like:: Enter length  (or stop to exit):  10,3")
print("\n")

while True:
    dims = input("Enter length (or stop to exit):")
    if dims.lower() == 'stop':
        break
    [l,w] = dims.split(",")
    print(f"You entered length={l} and width={w}  Area:{int(l)*int(w)}\n\n")

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
f_name = input("first name:") #<- comes in as a string
age = int(input("age: ")) 
# the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print(f"Hey {f_name}... Wouldn't it be great to be {age-2} again? But still, go old people!")




