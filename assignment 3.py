#!/usr/bin/env python
# coding: utf-8

# # Write a program to convert fahrenheit to kelvin and celsius both?

# In[20]:


print("Convert 68 degrees Fahrenheit to degrees Celsius")
temperature = 68
T = (temperature-32)*5/9 
print(T)


# In[21]:


print("Convert 60 degrees Fahrenheit to degrees Kelvin:")
temperature1 = 60
T = (temperature1+459.67)*(5/9)
print(T)


# # Write a program to swap two numbers in Python without using a temporary variable.

# In[45]:


print(" Write a program to swap two numbers in Python without using a temporary variable.")
a = 8
print("The value of a ", a)
b = 5
print("The value of b ", b)
a = a+b
b = a-b
a = a-b
print(a)
print("The swap value of a and b are ")
print("the value of a after swapping is ", a)
print("the value of b after swapping  is ", b)


# # Write a program to find the fourth root of a number.
# 

# In[81]:


print("Write a program to find the fourth root of a number.")
import math as m 
number = 64
print("The Fourth Root of a Number 16 is ")
print(pow(number,1/4))
    


# # Write a program to subtract two complex numbers in Python

# In[80]:


print("Write a program to subtract two complex numbers in Python")
first_number = 5+6j
print("The value of first_number is ", first_number)
second_number = 8+6j
print("The value of second_number is ", second_number)
subtract = first_number-second_number
print("The subtraction of the two numbers is ",subtract)


# # Write a program to swap two numbers in Python with the help of a temporary variable

# In[46]:


print(" Write a program to swap two numbers in Python with using a temporary variable.")
a = 8
print("The value of a ", a)
b = 5
print("The value of b ", b)
c=b
b=a
a=c
print("The swap value of a and b are ")
print("the value of a after swapping is ", a)
print("the value of b after swapping  is ", b)


# # Write a program to demonstrate all the available data types in Python. Hint: Use type() function

# In[73]:


print("Write a program to demonstrate all the available data types in Python. Hint: Use type() function")
a = 4
print(type(a))
b = 5.23
print(type(b))
c = "MUKESH SHARMA"
print(type(c))
D = {"BIKE":"PULSAR", "FRUITS":"APPLE"}
print(type(D))
L = [1,2,3,4,5,6]
print(type(L))
B = 5>2 and 6<5
print(type(B))
C = 4>1 or 2>4
print(type(C))
sets = {1,2,3,4,4,4,5,5,6,7,7,8}
print(type(sets))
tuples = ("Mukesh" , "SHARMA" , 1 , 2 , 8)
print(type(tuples))


# # Create a Markdown cell in jupyter and list the steps discussed in the session by Dr. Darshan
# Ingle sir to create Github profile and upload Githubs Assignment link.

# To Create Github profile 
# Go to https://github.com/join 
# Choose Sign up for GitHub, and then follow the instructions.
# Type a user name, your email address, and a password.
# Pass the test to prove you are not a robot.
# Verify the email and after this your account will be created 
# Create a Github public repo and name it LetsUpgrade AI/ML 
# Upload the files/solution in the repo in day wise manner. 
# Copy the URL of the Folder of that day and paste in the Assignment Submission Form available in google forum

# In[ ]:




