""" 
Program to act as a calculator for Old Irish Money - Pounds, Shillings and Pence. 
The program will add, subtract, multiply and divide values. 
Author: Nicola Mahon
Created: 2018-09-06
"""

"""""""""""""""""""""""""""""""""
Imported Libraries
"""""""""""""""""""""""""""""""""

import time
import math
from os import system

"""""""""""""""""""""""""""""""""
Function Prototypes
"""""""""""""""""""""""""""""""""

# Explain the program
def print_welcome():
	print_header("Introduction")
	print ("\nThis program will perform calculations using Old Irish Money \ni.e. Pounds, Shillings and Pence\n")
	time.sleep(3)

# Specify user input
def print_instructions():
	print ("Values must be entered in the format of \n\tPounds.Shillings.Pence\n\ti.e. 3.11.6\n")

# Display the menu options
def print_menu():
	print_header("Main Menu")
	print ("\nThe following options are available:")
	print ("1: Add")
	print ("2: Subtract")
	print ("3: Multiply")
	print ("4: Divide")
	print ("5: Clear the Screen")
	print ("0: Exit Program\n")

# Exit Program
def print_goodbye():
	print ("\nProgram Terminated. Goodbye!")
	time.sleep(2)

# Check user input for non-string values
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("\n** ERROR: Not an integer! Try again.\n")
       continue
    else:
       return userInput 
       break 

# Get the values the user wants to calculate
def get_value(option):
	"""
	value1 = input("\nEnter value 1: ")
	if option == 3:
		multiplier = int(inputNumber("Enter the multiplier: "))
		get_values = [value1, multiplier]
		return get_values
	elif option == 4:
		divisor = int(inputNumber("Enter the divisor: "))
		get_values = [value1, divisor]
		return get_values
	else:
		value2 = input("Enter value 2: ")
		get_values = [value1, value2]
		return get_values
	"""
	if option == 1 or option == 2: # add / subtract
		value1 = input("\nEnter value 1: ") # string value, parsed later
		value2 = input("Enter value 2: ")
		get_values = [value1, value2]
		return get_values
	elif option == 3:
		value3 = input("\nEnter value: ") # string value, parsed later
		multiplier = int(inputNumber("Enter the multiplier: "))
		get_values = [value3, multiplier]
		return get_values
	else:
		value4 = input("\nEnter value: ") # string value, parsed later
		divisor = int(inputNumber("Enter the divisor: "))
		get_values = [value4, divisor]
		return get_values

# Convert old money value to smallest denomination i.e. Pence
def convertToPence(value):
	split_value = value.split(".")
	pence_value = 0
	for x in range(len(split_value)):
		if x == 0:
			pence_value += int(split_value[x]) * 240
		elif x == 1:
			pence_value += int(split_value[x]) * 12
		else:
			pence_value += int(split_value[x])
	return pence_value

# Addition
def add(add_values):
	convert_value1 = convertToPence(add_values[0])
	convert_value2 = convertToPence(add_values[1])
	added_value = convert_value1 + convert_value2
	add_total = convertBack(added_value)
	return add_total

# Subtraction
def subtract(subtract_values):
	convert_value1 = convertToPence(subtract_values[0])
	convert_value2 = convertToPence(subtract_values[1])
	if convert_value1 > convert_value2:
		subtracted_value = convert_value1 - convert_value2
	else:
		subtracted_value = convert_value2 - convert_value1
	subtract_total = convertBack(subtracted_value)
	return subtract_total

# Multiplication
def multiply(multiply_values):
	convert_value1 = convertToPence(multiply_values[0])
	multiplied_value = convert_value1 * int(multiply_values[1])
	multiply_total = convertBack(multiplied_value)
	return multiply_total

# Division
def divide(divide_values):
	convert_value1 = convertToPence(divide_values[0])
	divided_value = convert_value1 / int(divide_values[1])
	divided_total = convertBack(divided_value)
	return divided_total

# convert back to Pound.Shilling.Pence
def convertBack(value):
	pound = math.floor(value / 240)
	value -= pound * 240
	shilling = math.floor(value / 12)
	value -= shilling * 12
	pence = round(value)

	old_money_value = [pound, shilling, pence]
	return old_money_value

# Print old_money_value
def print_old_money(old_money):
	print("\nAnswer: ",denominations[0],old_money[0], denominations[1],old_money[1], denominations[2],old_money[2])
	time.sleep(3)

# Print headers
def print_header(title):
	print("\n\n")
	print("*" * (len(title) + 4))
	print(" ", title)
	print("*" * (len(title) + 4))

# Main Function
def main():	

	# initalise variable for menu options 
	option = 0
	
	# print menu options and instructions
	print_menu()
	print_instructions()
	print_header("Choose a Menu Option")

	# get user's menu option, ensure it is an integer
	option = inputNumber("\nEnter a menu option now: ")

	# check for valid integer value
	if option < 0 or option > 5:
		# print feedback: 
		print("\n** ERROR: Invalid Option Selected")
	# confirm user has selected valid menu option
	elif option != 0:
		if option == 1:
			print_header("Addition")
			add_values = get_value(option)
			add_total = add(add_values)
			print_old_money(add_total)
		elif option == 2:
			print_header("Subtraction")
			subtract_values = get_value(option)
			subtract_total = subtract(subtract_values)
			print_old_money(subtract_total)
		elif option == 3:
			print_header("Multiplication")
			multiply_values = get_value(option)
			multiply_total = multiply(multiply_values)
			print_old_money(multiply_total)
		elif option == 4:
			print_header("Division")
			divide_values = get_value(option)
			divided_total = divide(divide_values)
			print_old_money(divided_total)
		else:
			_ = system('cls')
	# terminate program
	else:
		run = False
		print_goodbye()
		exit()

"""""""""""""""""""""""""""""""""
Global Variables
"""""""""""""""""""""""""""""""""

# flag to run/exit program
run = True

# string values for printing
denominations = ['£', '.', '/']


"""""""""""""""""""""""""""""""""
Run Program
"""""""""""""""""""""""""""""""""

if __name__ == "__main__":
	print_welcome()

	# loop to keep program running until user terminates
	while run == True:
		main()