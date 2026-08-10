# 🐍 Comments & Docstrings
#
# Solve the following 5 problems.
# Do not just copy the solution — try solving each problem yourself.
#
# ============================================================
# Problem 1: Single-Line Comments
# ============================================================
#
# Create variables for:
# - Your name
# - Your age
# - Your current learning goal
#
# Add a comment above each variable explaining what it stores.
#
# Print all three values.
#
# Why solve this?
# Comments help you explain code to yourself and other developers.
# Good comments make code easier to understand and maintain.
#
# What you will learn:
# - Single-line comments using #
# - Writing useful comments
# - Keeping comments related to the code
#name of the person
name="Rakesh"
#age of the person
age =22
#learning goal of the person
current_learning_goal ="Data Engineering"
print(f"{name} is a {age} old boy who's learning goal is {current_learning_goal}")
# ============================================================
# Problem 2: Comment Out Code
# ============================================================
#
# Create two numbers:
#
# a = 20
# b = 10
#
# Write code to calculate:
# - Addition
# - Subtraction
# - Multiplication
#
# Comment out the subtraction operation so that it does not execute.
#
# Print the addition and multiplication results.
#
# Why solve this?
# Sometimes you temporarily need to disable a piece of code
# without deleting it.
#
# What you will learn:
# - Commenting out code
# - Understanding that comments are ignored by Python
a = 20
b = 10
print("Addition :",a+b)
# print("Subtraction :",a-b)
print("Multiplication:",a*b)
# ============================================================
# Problem 3: Function with a Docstring
# ============================================================
#
# Create a function called calculate_square(number).
#
# Add a docstring inside the function explaining what the
# function does.
#
# The function should return the square of the given number.
#
# Call the function with 5 and print the result.
#
# Why solve this?
# Docstrings document what a function, class, or module does.
# They are especially useful when working on larger projects.
#
# What you will learn:
# - Function docstrings
# - Triple quotes
# - return
# - __doc__
#
# Bonus:
# Print the function's docstring using:
#
# calculate_square.__doc__
def calculate_square(number):
    """
     function to calculate the square of a number
    :param number:
    :return:
    """
    return number*number
print(calculate_square(5))
print(calculate_square.__doc__)
# ============================================================
# Problem 4: Function with Multiple Parameters
# ============================================================
#
# Create a function called student_details(name, age, course).
#
# Add a docstring explaining:
# - What the function does
# - What each parameter represents
#
# Print the student's details from inside the function.
#
# Call the function with your own information.
#
# Why solve this?
# In real projects, functions may have multiple parameters.
# A clear docstring makes the purpose of each parameter easier
# to understand.
#
# What you will learn:
# - Multi-line docstrings
# - Function parameters
# - Documenting parameters
def student_details(name, age, course):

    """
    function is to print the name ,age and course of the student
    :param name:
    :param age:
    :param course:
    :return:
    """
    print(f"{name} is {age} and learns {course}")
student_details("Rakesh",22,"CSE")
# ============================================================
# Problem 5: Comment vs Docstring
# ============================================================
#
# Create a function called calculate_total(price, quantity).
#
# Requirements:
#
# 1. Add a comment explaining why the calculation is being done.
#
# 2. Add a docstring explaining what the function does.
#
# 3. Calculate:
#
#    total = price * quantity
#
# 4. Return the total.
#
# 5. Call the function with:
#
#    price = 500
#    quantity = 3
#
# 6. Print the result.
#
# 7. Print the function's docstring.
#
# Why solve this?
# This helps you understand the difference between:
#
# Comment:
# A note for humans reading the source code.
#
# Docstring:
# Documentation attached to a function, class, or module
# that Python can access.
#
# What you will learn:
# - Comments
# - Docstrings
# - return
# - Function documentation
# - __doc__
def calculate_total(price, quantity):
   # to calculate total price
    """
    function to calculate the total price and quantity
    :param price:
    :param quantity:
    :return:
    """
    return (price*quantity)
print(calculate_total(500, 3))
# ============================================================
# 🎯 Goal
# ============================================================
#
# After solving these 5 problems, you should understand:
#
# 1. How to write single-line comments
# 2. How to temporarily disable code
# 3. What a docstring is
# 4. How to document functions
# 5. The difference between comments and docstrings
# 6. How to access a function's docstring
#
# Try solving all 5 problems yourself before looking for help.