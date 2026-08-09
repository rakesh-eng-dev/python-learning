# 🐍 Variable Scope
#Local->Enclosing->Global->Builtin
# Solve the following 5 problems.
# Do not just copy the solution — try solving each problem yourself.
#
# ============================================================
# Problem 1: Local Variable
# ============================================================
#
# Create a function called display_student().
# Inside the function, create a variable called student_name
# and assign your name to it.
#
# Print the variable inside the function.
#
# Why solve this?
# To understand that a variable created inside a function
# normally belongs to that function.
#
# What you will learn:
# - Local variables
# - Function scope
# - Using variables inside functions
def display_student():
    name = "Rakesh"
    print(name)
display_student()
# ============================================================
# Problem 2: Global Variable
# ============================================================
#
# Create a global variable called college_name.
#
# Create a function called display_college() that prints
# the college_name variable.
#
# Call the function.
#
# Why solve this?
# To understand how a function can access a variable
# created outside the function.
#
# What you will learn:
# - Global variables
# - Accessing global variables
# - Difference between local and global scope
college_name= "Sathyabama University"
def display_college():
   print(college_name)
display_college()
# ============================================================
# Problem 3: Same Variable Name in Different Scopes
# ============================================================
#
# Create a global variable called message with the value:
# "Global Message"
#
# Create a function called show_message().
#
# Inside the function, create another variable called message
# with the value:
# "Local Message"
#
# Print message inside the function.
# Print message outside the function.
#
# Why solve this?
# To understand what happens when local and global variables
# have the same name.
#
# What you will learn:
# - Local scope vs global scope
# - Variable shadowing
# - How Python chooses which variable to use
message = "Global Message"
def show_message():
    message = "Local Message"
    print(message)
print(message)
show_message()
# ============================================================
# Problem 4: Modify a Global Variable
# ============================================================
#
# Create a global variable called counter and assign 0 to it.
#
# Create a function called increase_counter().
#
# Inside the function, increase counter by 1.
#
# Call the function three times and print the final value.
#
# Hint:
# You will need to understand the 'global' keyword.
#
# Why solve this?
# This helps you understand why Python does not normally allow
# direct modification of a global variable from inside a function.
#
# What you will learn:
# - global keyword
# - Modifying global variables
# - Reading vs modifying variables from another scope
counter = 0
def increase_counter():
    global counter
    counter += 1
increase_counter()
increase_counter()
increase_counter()
print(counter)

# ============================================================
# Problem 5: Scope Practice
# ============================================================
#
# Create a global variable called company_name = "Google".
#
# Create a function called employee_details().
#
# Inside the function:
# - Create a local variable employee_name
# - Create a local variable salary
# - Print employee_name
# - Print salary
# - Print company_name
#
# Outside the function:
# - Print company_name
#
# Then try to print employee_name outside the function.
#
# Observe what happens.
#
# Why solve this?
# This combines local and global scope and helps you understand
# which variables are accessible from different parts of a program.
#
# What you will learn:
# - Local scope
# - Global scope
# - Variable accessibility
# - Function boundaries
# - NameError caused by accessing an unavailable local variable
company_name = "Google"
def employee_details():
    employee_name ="Rakesh"
    salary = 27000.00
    print(employee_name)
    print(salary)
    print(company_name)
employee_details()
print(company_name)

# ============================================================
# 🎯 Goal
# ============================================================
#
# After solving these 5 problems, you should understand:
#
# 1. What local scope means
# 2. What global scope means
# 3. How functions access variables
# 4. What happens when local and global names are the same
# 5. How the global keyword works
#
# Try solving all 5 problems yourself before looking for help.