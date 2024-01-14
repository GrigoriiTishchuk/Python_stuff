# Lesson 4 tasks
# Test all of your functions by calling them. return is not needed unless specified.
# Feel free to rename the functions
# Remove pass before writing anything in the function
# After you finish a task, comment out the function call to speed up your work
# Don't overthink the assignments, just ask if there are any questions 

# Task 1
# a)
# Create a dictionary named pet_info that has keys for "name", "species", "age" and
# "favorite food"
# Fill in the values with information about a pet
# Print the dictionary

# b)
# Print only the name

# c)
# Change the age of the pet, print it to test

# d)
# d1) Add a key-value pair called "other_info" to pet_info
# d2) Delete other_info



pet_info = {
    "name": "Fido",
    "species": "dog",
    "age": 3,
    "favorite food": "meat"
    }

print(pet_info)

print(pet_info["name"])

pet_info["age"] = 4

print(pet_info["age"])


pet_info["other_info"] = "test"

print(pet_info["other_info"])

pet_info.pop("other_info")

print(pet_info)
# Task 2
# Create a function that takes input from the user
# Create a file in the same folder you have saved your exercise in
# You can create the file manually, or inside your function
# Make your function write the input from the user into the file
# Keywords: file write, with open

def note_to_self():
    us_inp = input("Userssss input: ")
    with open("user_input.txt", "w") as file:
        file.write(us_inp)

note_to_self()

# Task 3
# Ask the user for input, instruct them to write about what happened today
# Create a function that writes to a file you have created 
# You should append to the file, not overwrite it
# Test with calling the function repeatedly
# The existing entries shouldn't be deleted with new entries

def add_to_daily_log():
    use_inp = input("User's input: ")
    with open("user_daily_input.txt", "a") as file:
        file.write(use_inp + " ")


add_to_daily_log()
# Task 4
# Create an empty list
# Ask the user to input names, and tell them how to stop the program
# When the user inputs "done", the program stops and prints all the names
# Hint: you can use the list methods append and join for this exercise

def party_invite_list():
    user_input = input("Enter name: ")
    names = []
    while user_input != "done":
        user_input = input("Enter name: ")
        names.append(user_input)
    else:
        names.remove("done")
        print(names)


party_invite_list()
# Task 5
# Create an empty dictionary called movie inside the function movie_info()
# With 3 input calls, ask the user to add values to the keys "title", "year" and "rating" to the dictionary
# After taking the input, print the info in a way, that the key names are capitalized, and the values formatted
# Hint: you can use a for in loop to loop through the info: for key, value in info.items():




def movie_info():
    movie = {
        "title": "",
        "year": "",
        "rating": ""
    }
    for i in movie:
        user_inp = input(f"Enter movie's info: ")
        movie[i].values = user_inp

movie_info()
movie_info()
movie_info()

# Task 6
# Create a function that shows the current time
# Try to show the time in a human-readable format
# You can use the time module

def show_current_time():
    pass

# Task 7
# Create a list with bad words
# Write a function that asks the user to input a sentence that contains the bad words
# Print or return the sentence with all of the bad words replaced with stars *****
# As a bonus, try to make the number of stars the same as the amount of letters in the censored word
# One way to do this is to loop through the bad words and test if they are found in the sentence
# The string replace method can be useful here

bad_words=[]

def censor_profanities(list):
    pass




# Extra task

# Write a program that uses the time module to create a workout timer
# The user can input different exercises and the duration for each
# The program will then ask the user to press enter to start an exercise
# During the exercise, time remaining will be displayed
# When the exercise ends, tell the user the exercise is finished
# Proceed to the next exercise, repeat the process until no exercises remain
# When the workout ends, notify the user that the workout is complete
# Bonus: Prepare for invalid user input. Handle errors.

def workout_timer():
    pass