# 🐍 Operators in Python
#
# Solve the following 5 problems.
# Do not just copy the solution — try solving each problem yourself.
#
# ============================================================
# Problem 1: Basic Arithmetic
# ============================================================
#
# Create two variables:
#
# a = 25
# b = 10
#
# Perform and print:
# - Addition
# - Subtraction
# - Multiplication
# - Division
#
# Why solve this?
# Arithmetic operators are the foundation for calculations in
# almost every program.
#
# What you will learn:
# - +
# - -
# - *
# - /
a = 25
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# ============================================================
# Problem 2: Division Operators
# ============================================================
#
# Create:
#
# a = 17
# b = 5
#
# Print:
# - Normal division
# - Floor division
# - Remainder
# - Power
#
# Why solve this?
# Python has different division-related operators. Understanding
# them is important when processing numbers and calculating
# positions, batches, partitions, and remainders.
#
# What you will learn:
# - /
# - //
# - %
# - **
a = 17
b = 5
print(a/b)
print(a//b)
print(a%b)
print(a**b)
# ============================================================
# Problem 3: Comparison Operators
# ============================================================
#
# Create:
#
# age = 22
# required_age = 18
#
# Check and print whether:
# - age is greater than required_age
# - age is less than required_age
# - age is equal to required_age
# - age is greater than or equal to required_age
# - age is not equal to required_age
#
# Why solve this?
# Comparison operators are heavily used in conditions and
# decision-making.
#
# What you will learn:
# - >
# - <
# - ==
# - >=
# - !=
# - Boolean results
age = 22
required_age = 18
print(age>required_age)
print(age<required_age)
print(age==required_age)
print(age>=required_age)
print(age!=required_age)
# ============================================================
# Problem 4: Logical Operators
# ============================================================
#
# Create:
#
# age = 22
# has_id = True
#
# Check whether the person is allowed to enter when:
#
# 1. Age must be 18 or above AND they must have an ID.
# 2. Either age is 18 or above OR they have an ID.
# 3. The person does NOT have an ID.
#
# Print the result of each condition.
#
# Why solve this?
# Real programs often combine multiple conditions instead of
# checking only one condition.
#
# What you will learn:
# - and
# - or
# - not
# - Combining Boolean expressions
age = 22
has_id = True
print((age>=required_age)and has_id)
print((age>=required_age)or has_id)
print(not has_id)

# ============================================================
# Problem 5: Assignment Operators
# ============================================================
#
# Create:
#
# score = 100
#
# Modify score using assignment operators:
#
# - Add 20
# - Subtract 10
# - Multiply by 2
# - Divide by 2
#
# Print the value after each operation.
#
# Use compound assignment operators where appropriate.
#
# Why solve this?
# Assignment operators are commonly used when updating values
# such as counters, scores, balances, totals, and record counts.
#
# What you will learn:
# - =
# - +=
# - -=
# - *=
# - /=
score =100
score+=20
score-=10
score*=2
score//=2
print(score)
# ============================================================
# 🎯 Goal
# ============================================================
#
# After solving these 5 problems, you should understand:
#
# 1. Arithmetic operators
# 2. Comparison operators
# 3. Logical operators
# 4. Assignment operators
# 5. Division, floor division and remainder
# 6. How operators produce Boolean results
#
# Try solving all 5 problems yourself before looking for help.