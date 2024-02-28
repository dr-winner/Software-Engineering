
# Creating user input program

"""
this program asks user to input their
a. name
b. age
c. location
the prints a specialised message to the user with the inputs

"""
name = input('What is your name: ')
age = int(input('Would you mind telling me your age: '))
location = str(input('Please what is your location: '))
print('Hello! Welcome ', name + ' you are ',age,'years old, and you stay at ',location + '. Have a good day!')