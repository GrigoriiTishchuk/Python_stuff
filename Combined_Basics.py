# 1
# Type Casting:
# a) Convert the string "1234" into an integer and the number 5678 into a string. Assign these to variables.
# Note: you can use the methods int() and str().
# Test that you got it right by using the type() function on the variables (you can display the result in the console).
string_number = "1234"
number_number = 5678

new_number = int(string_number)
new_string = str(number_number)

# b) Try to turn the values into floats using float() and see what happens.
float_number = float(new_number)
float_string = float(new_string)

print(new_number)
# 2
# a) Basic for loop:
# Given a list of numbers, print out each number
lista = [2, 5, 7, 8, 5, 42]

for i in lista:
    print(i)

# b) Basic while loop:
# Do the same, but use a while loop

while i < len(lista):
    print(i)
    i += 1

# c)
# Using a loop, print Hello World! 100 times into the console.

for i in range(100):
    print("Hello World!")
# 3
# Write a program that accepts a word from the user and reverses it
# Have the user type in the word using input
# To reverse a word, you can use reversed()

inp_word = input("Enter a word: ")
result = inp_word[::-1]
print("Result is: ", result)

# 4
# Write a function that displays the first and last colors from the following list.
color_list = ["Red", "Green", "White", "Black"]

def first_and_last(color):
    print(color[0], color[-1])

first_and_last(color_list)

# 5
# Pack and unpack PC parts
# a)
# Write a program that concatenates all elements in a list into a string and returns it. 
# You can use a for loop to concatenate the elements and to save them inside a variable.
# Add spaces between the elements
# Note: the join method can be used here.
computer_parts_list = ["GPU", "CPU", "RAM", "HDD", "SSD", "Case", "Fans", "Cables"]

# b)
# Take the new string you created, and turn it back into a list that looks like the original computer_parts_list
# The string split method can be used in this part of the exercise.

# 6
# Create a list of five fruits. Write a loop that prints each fruit in the list.

# a) Write a function multiply that takes two numbers as arguments and returns their sum

# b) Modify the function, or create a new function that only multiplies odd numbers.
# Add a conditional to the function that tests that both numbers are odd.
# If both are odd, print or return the result of the multiplication
# In case of either of the numbers being even, print a message that describes the situation

# 7
# Write a function convert_currency that converts euros to dollars. 
# The function should take the amount, the current exchange rate, and return the converted amount.
# 1 Euro = 1.10 USD 29.11.23