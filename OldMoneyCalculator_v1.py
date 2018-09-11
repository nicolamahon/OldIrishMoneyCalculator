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

"""""""""""""""""""""""""""""""""
Function Prototypes
"""""""""""""""""""""""""""""""""

# Explain the program
def print_welcome():
	print ("\nThis program will perform calculations using Old Irish Money i.e. Pounds, Shillings and Pence\n")
	time.sleep(3)

# Specify user input
def print_instructions():
	print ("Values must be entered in the format of 'Pounds.Shillings.Pence' i.e. 3.11.6\n")
	time.sleep(3)

# Display the menu options
def print_menu():
	print ("\nThe following options are available:")
	print ("1: Add")
	print ("2: Subtract")
	print ("3: Multiply")
	print ("4: Divide")
	print ("0: Exit Program\n")

# Exit Program
def print_goodbye():
	print ("\nProgram Terminated. Goodbye!")

# Check user input for non-string values
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("\nNot an integer! Try again.\n")
       continue
    else:
       return userInput 
       break 

# Get the values to be calculated
def get_value():
	value1 = input("Enter value 1: ")
	if option == 3:
		multiplier = int(input("Enter the multiplier i.e. 2, 5, 10: "))
		get_values = [value1, multiplier]
		return get_values
	elif option == 4:
		divisor = int(input("Enter the divisor i.e. 3, 6, 7: "))
		get_values = [value1, divisor]
		return get_values
	else:
		value2 = input("Enter value 2: ")
		get_values = [value1, value2]
		return get_values

# Convert old money value to smallest denomination i.e. Pence
def convertToPence(value):
	split_value = value.split(".")
	pence_value = 0
	#print("Starting Pence: ", pence_value)
	for x in range(len(split_value)):
		#print(denominations[x], split_value[x])
		if x == 0:
			#print("Pounds -> Pence: ", int(split_value[x]) * 240)
			pence_value += int(split_value[x]) * 240
		elif x == 1:
			#print("Shillings -> Pence: ", int(split_value[x]) * 12)
			pence_value += int(split_value[x]) * 12
		else:
			#print("Pence -> Pence: ", int(split_value[x]))
			pence_value += int(split_value[x])
	#print("Total Pence: ", pence_value)
	return pence_value

# Addition
def add(add_values):
	convert_value1 = convertToPence(add_values[0])
	convert_value2 = convertToPence(add_values[1])
	added_value = convert_value1 + convert_value2
	#print("\nAdded Pennies: ", added_value)
	add_total = convertBack(added_value)
	#print("\nConverted Sum Value: ", add_total)
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
	print("array[0] =", multiply_values[0])
	print("(multiplier) array[1] =", multiply_values[1])
	convert_value1 = convertToPence(multiply_values[0])
	print("converted value1 to pence = ", convert_value1)
	multiplied_value = convert_value1 * multiply_values[1]
	print("multiplied value x*y = ", multiplied_value)
	multiply_total = convertBack(multiplied_value)
	print("total converted back to old money = ", multiply_total)
	return multiply_total

# Division
def divide(divide_values):
	convert_value1 = convertToPence(divide_values[0])
	divided_value = convert_value1 / divide_values[1]
	divided_total = convertBack(divided_value)
	return divided_total

# convert back to Pound.Shilling.Pence
def convertBack(value):
	pound = math.floor(value / 240)
	value -= pound * 240
	#print("pound = ", pound, "value = ", value)
	shilling = math.floor(value / 12)
	value -= shilling * 12
	#print("shilling = ", shilling, "value = ", value)
	pence = round(value)
	#print("pence = ", pence, "value = ", value)

	old_money_value = [pound, shilling, pence]
	return old_money_value

# print old_money_value
def print_old_money(old_money):
	print("\nAnswer: ",denominations[0],old_money[0], denominations[1],old_money[1], denominations[2],old_money[2])

"""""""""""""""""""""""""""""""""
Global Variables
"""""""""""""""""""""""""""""""""

# flag to run/exit program
run = True

# string values for printing
denominations = ['£', '.', '/']

# selected menu option 
option = ""

"""""""""""""""""""""""""""""""""
Main Function
"""""""""""""""""""""""""""""""""

# main()
if __name__ == "__main__":

	print_welcome()

	# loop to keep program running until user terminates
	while run == True:
		
		# print menu options and instructions
		print_menu()
		print_instructions()

		# get user's menu option, ensure it is an integer
		option = inputNumber("Enter a menu option now: ")

		# check for valid integer value
		if option < 0 or option > 4:
			# print feedback: 
			print("\nERROR: Invalid Option Selected")
		# confirm user has selected valid menu option
		elif option != 0:
			if option == 1:
				print("\n** Adding **")
				add_values = get_value()
				add_total = add(add_values)
				print_old_money(add_total)
			elif option == 2:
				print("\n** Subtracting **")
				subtract_values = get_value()
				subtract_total = subtract(subtract_values)
				print_old_money(subtract_total)
			elif option == 3:
				print("\n** Multiplying **")
				multiply_values = get_value()
				multiply_total = multiply(multiply_values)
				print_old_money(multiply_total)
			else:
				print("\n** Dividing **")
				divide_values = get_value()
				divided_total = divide(divide_values)
				print_old_money(divided_total)
		# terminate program
		else:
			run = False
			print_goodbye()
			exit()