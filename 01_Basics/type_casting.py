# 🐍 Type Casting
#
# Solve the following 5 problems.
# Do not just copy the solution — try solving each problem yourself.
#
# ============================================================
# Problem 1: Convert String to Integer
# ============================================================
#
# Create a variable:
#
# age = "22"
#
# Convert age from a string to an integer.
# Add 5 to the age and print the result.
#
# Why solve this?
# Input received from users is commonly stored as a string.
# You need to know how to convert it before performing
# numerical calculations.
#
# What you will learn:
# - str to int
# - int()
# - Arithmetic after type conversion
age = "22"
a = int(age)
print(a+5)
# ============================================================
# Problem 2: Convert String to Float
# ============================================================
#
# Create a variable:
#
# price = "1499.50"
#
# Convert the value into a float.
# Add 500 to it and print the final price.
#
# Why solve this?
# Real-world data often comes as text, especially when reading
# data from files, APIs, or user input.
#
# What you will learn:
# - str to float
# - float()
# - Using converted values in calculations
price = "1499.50"
a=float(price)
print(a+1500)
# ============================================================
# Problem 3: Student Marks
# ============================================================
#
# Create three variables containing marks as strings:
#
# math = "85"
# science = "90"
# python = "95"
#
# Convert all three values into integers.
# Calculate and print:
# - Total marks
# - Average marks
#
# Why solve this?
# This combines multiple type conversions with calculations
# and gives you practice with a common data-processing situation.
#
# What you will learn:
# - Multiple type conversions
# - str to int
# - Calculations using converted values
# - Average calculation
math = "85"
science = "90"
python = "95"
math=int(math)
science=int(science)
python=int(python)
total = math + science + python
print(total)
print(total/3)
# ============================================================
# Problem 4: Integer to Float and String
# ============================================================
#
# Create a variable:
#
# salary = 30000
#
# Convert salary into:
# 1. A float
# 2. A string
#
# Print the value and type of each converted variable.
#
# Why solve this?
# Type casting is not only about converting strings into numbers.
# You should also understand conversions between numeric and
# string types.
#
# What you will learn:
# - int to float
# - int to str
# - float()
# - str()
# - type()
salary = 30000
str = str(salary)
flot = float(str)
print(salary, type(salary))
print(flot , type(flot))
print(str , type(str))
# ============================================================
# Problem 5: User Input and Type Casting
# ============================================================
#
# Ask the user to enter:
# - Their name
# - Their age
# - Their height in centimeters
#
# Convert age into an integer.
# Convert height into a float.
#
# Print the information along with the data types.
#
# Example:
#
# Enter your name: Rakesh
# Enter your age: 22
# Enter your height: 180.5
#
# Why solve this?
# This is one of the most important uses of type casting.
# input() returns data as a string, so you must convert it when
# you need to perform numerical operations.
#
# What you will learn:
# - input()
# - str to int
# - str to float
# - type()
# - Combining input handling with type casting
name = input("Enter your name:")
age = input("Enter your age:")
height = input("Enter your height:")
age = int(age)
height=float(height)
print(name, type(name))
print(age, type(age))
print(height, type(height))
# ============================================================
# 🎯 Goal
# ============================================================
#
# After solving these 5 problems, you should understand:
#
# 1. Why type casting is needed
# 2. str -> int
# 3. str -> float
# 4. int -> float
# 5. int -> str
# 6. Type casting with user input
#
# Try solving all 5 problems yourself before looking for help.