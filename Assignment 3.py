#!/usr/bin/env python
# coding: utf-8

# Q1: Why are functions advantageous to have in your programs? Ans: With the help of function, the codes are: a) Reliable b) Systematic c) Maintainable d) Precise

# Q2: When does the code in a function run: when it's specified or when it's called? Ans: The time when it is called

# Q3: What statement creates a function? Ans: def statement

# Q4: What is the difference between a function and a function call? Ans: Function: It is basically creation of the function for doing a particular command. Function call: It is the time when the function is created and by the specific name given to the is called out

# Q5: How many global scopes are there in a Python program? How many local scopes? Ans: There is one global scope which is accessible through the entire program And there are multiple local scope. Each loacl scope is separate and accessible only within its specific scope and nested scopes.

# Q6: What happens to variables in a local scope when the function call returns? Ans: They are created when the function is called and destroyed when the function call returns or the scope is exited. Once the function call is complete, the local variables are no longer accessible or available for use.

# Q7: What is the concept of a return value? Is it possible to have a return value in an expression? Ans: The return value refer to the value of function that provide its output when executed. It is not possible to have a return value in an expression itself. A return statement is used specifically within the context of a function to indicate the value that should be returned from that function.

# Q8: If a function does not have a return statement, what is the return value of a call to that function?
# Ans: "None"

# Q9. How do you make a function variable refer to the global variable?
# Ans: 
# 
# global_var = 10
# 
# def my_fuction():
#     global global_var ("using the global keywords")
#     print(global_var) ("Accessing the global variable")
#     
# my_function()
# 
# 
# In this code, we have a global variable called global_var with a value of 10. Inside the my_function function, we use the global keyword before referencing global_var. This informs the machine that we are referring to the global variable, even though there is a local variable with the same name.
# 
# 
# global_var = 20
# 
# def my_function():
#     global global_var
#     global_var = 20  ("Modfying the global variable")
# 
# my_function()
# print(global_var) ("output will be 20")
# 
# In this updated code, we modify the value of global_var to 20 within the function using the global keyword. After calling the function, when we print the value of global_var outside the function, it reflects the updated value.

# Q10. What is the data type of None?
# Ans: <NoneType>

# Q11. What does the sentence import areallyourpetsnamederic do?
# Ans: There is no import statement like this and this would result in "ModuleNotFoundError"

# Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# Ans: If we want to call out a function bacon() from spam. Below is the statement -
# 
# import spam
# spam.bacon()

# Q13. What can you do to save a programme from crashing if it encounters an error?
# Ans: We can encounter an error with the help of "Exception Handling" - by using try, except syntax.

# Q14. What is the purpose of the try clause? What is the purpose of the except clause?
# Ans: The try and except clauses are used together in Python's exception handling mechanism. 
# By using the try and except clauses together, you can control the flow of your program and handle exceptions in a controlled manner, allowing you to handle errors gracefully and prevent program crashes.

# In[ ]:




