# 🐍 Variables & Data Types
#
# Solve the following 5 problems.
# Do not just copy the solution — try solving each problem yourself.
#
# ------------------------------------------------------------
# Problem 1: Student Information
# ------------------------------------------------------------
# Create variables to store:
# - Your name
# - Your age
# - Your CGPA
# - Whether you are currently a student
#
# Print all the values and their data types.
#
# Why solve this?
# To understand how variables store different types of values.
#
# What you will learn:
# - Variable creation
# - str
# - int
# - float
# - bool
# - type()
#
name = "Rakesh"
age = 22
CGPA=7.55
is_student = False

print(name , type(name))
print(age , type(age))
print(CGPA , type(CGPA))
print(is_student , type(is_student))
# ------------------------------------------------------------
# Problem 2: Product Details
# ------------------------------------------------------------
# Create variables for:
# - Product name
# - Product price
# - Quantity
# - Whether the product is available
#
# Calculate and print the total price.
#
# Why solve this?
# To understand how different data types can be used together
# in a simple real-world calculation.
#
# What you will learn:
# - Variables
# - int and float
# - Strings
# - Boolean values
# - Arithmetic with variables
product_name="iPhone"
product_price = 82000.00
quantity=2
is_available = True

print("Total price:",product_price*quantity)
# ------------------------------------------------------------
# Problem 3: Employee Information
# ------------------------------------------------------------
# Create variables for an employee:
# - Name
# - Employee ID
# - Salary
# - Years of experience
#
# Print each value along with its data type.
#
# Why solve this?
# Data Engineering programs constantly work with structured
# information containing different types of data.
#
# What you will learn:
# - Choosing appropriate data types
# - Understanding how Python represents data
# - Using type()
name = "Rakesh"
emp_id = 2492922
salary = 26500.00
years_of_experience = 1

print(name , type(name))
print(emp_id , type(emp_id))
print(salary , type(salary))
print(years_of_experience , type(years_of_experience))
# ------------------------------------------------------------
# Problem 4: Temperature Conversion
# ------------------------------------------------------------
# Store a temperature in Celsius in a variable.
#
# Convert it to Fahrenheit using:
#
# Fahrenheit = (Celsius * 9/5) + 32
#
# Print both Celsius and Fahrenheit.
#
# Why solve this?
# To practice storing numerical data and performing calculations
# using variables.
#
# What you will learn:
# - Numeric data types
# - Arithmetic operators
# - Variables in calculations
temperature_in_celsius = 37
temperature_in_fahrenheit = (temperature_in_celsius * 9/5) + 32
print(temperature_in_fahrenheit)
# ------------------------------------------------------------
# Problem 5: Data Type Checker
# ------------------------------------------------------------
# Create variables containing:
# - A string
# - An integer
# - A float
# - A boolean
# - A list
# - A tuple
# - A set
# - A dictionary
#
# Print each value and its data type using type().
#
# Why solve this?
# This gives you a basic understanding of the major Python
# data types that you will use throughout your Python and
# Data Engineering journey.
#
# What you will learn:
# - str
# - int
# - float
# - bool
# - list
# - tuple
# - set
# - dict
# - type()
name = "Rakesh"
age = 22
CGPA=7.55
is_student = False
subjects = ["Big Data", "Spark","Python"]
working_days =("Monday","Tuesday","Wednesday","Thursday","Friday")
tech_stack = {"Python", "SQL", "HDFS", "Spark", "ETC"}
learnt_checklist ={"java":"intermediate","python":"basic","sql":"intermediate"}
print(name , type(name))
print(age , type(age))
print(CGPA , type(CGPA))
print(is_student , type(is_student))
print(subjects , type(subjects))
print(working_days , type(working_days))
print(tech_stack , type(tech_stack))
print(learnt_checklist , type(learnt_checklist))
# ------------------------------------------------------------
# 🎯 Goal
# ------------------------------------------------------------
# After solving these 5 problems, you should be comfortable with:
#
# 1. Creating variables
# 2. Storing different types of data
# 3. Identifying data types
# 4. Using variables in calculations
# 5. Understanding basic Python data types
#
# Try solving everything yourself before looking for help.