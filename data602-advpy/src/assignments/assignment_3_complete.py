
# Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”

while True:
    meal = input("What meal are we talking about? (type 'stop' to stop)")
    if meal == "breakfast":
        print("How about some pancakes!")
    elif meal == "lunch":
        print("Pancakes make a good brunch.")
    elif meal == "dinner":
        print("Pancakes for dinner!")
    elif meal == "stop":
        break 
    else:
        print("That's not a meal. And PS there's no such thing as the fourth meal either!")


# Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
# You should take in the user’s input for the number of hours worked, and their rate of pay.
        
while True:
    print("")
    print("Gross pay calculator  (stop to stop)")
    hours = input("How many hours did you work?")
    rate = input("What is your hourly rate?")
    if rate == "stop" or hours == "stop":
        break
    else:
        print(f"You earned: ${float(hours) + float(rate)}")

#Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
        
def times_ten(factor):
    print(factor * 10)
times_ten(10)

#Q4: Find the errors, debug the program, and then execute to show the output.
# def main()
#       Calories1 = input( "How many calories are in the first food?")
#       Calories2 = input( "How many calories are in the first food?")
#       showCalories(calories1, calories2)
# def showCalories()   
#    print(“The total calories you ate today”, format(calories1 + calories2,.2f))

def showCalories(calories1, calories2):   
    print(f"The total calories you ate today is: {calories1 + calories2:.2f}")
def main():
    calories1 = float(input( "How many calories are in the first food?"))
    calories2 = float(input( "How many calories are in the first food?"))
    showCalories(calories1 = calories1, calories2 = calories2)
main()
# There were lots of little adjustments here.
# Also, I learned something about outbound formatting with the little .2f.

#Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
#         1/30 + 2/29 + 3/28 ............. + 30/1
## total = sum(i / (31 - i) for i in range(1, 31))
subtotal = 0
for i in range(1,31):
    numerator = i
    denominator = 31 - i
    print(f"Adding {numerator} / {denominator}")
    subtotal = subtotal + (numerator / denominator)
print(f"Total: {subtotal:.2f}")

# Q6: Write a function that computes the area of a triangle given its base and height.
# The formula for an area of a triangle is: AREA = 1/2 * BASE * HEIGHT
def triangle_area(base, height):
    return 1/2 * base * height
base=5
height=4
print(f"A triangle with a base of {base} and height of {height} has an area of {triangle_area(base = base, height = height)}")