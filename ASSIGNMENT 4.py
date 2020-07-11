#!/usr/bin/env python
# coding: utf-8

# # Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
# Result as "square of that number minus 2"
# 

# In[9]:


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i%2==0:
        result = i**2-2
        print(result)
      

    


# # Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
# number is divided 2.

# In[16]:


numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i>7 and i%2==0:
        print(i)
        
        


# #  Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
# 25, print their multiplication result else print their division result.
# 

# In[18]:



if 
    
    if:
        result>25
      
    else:
       
    


# In[29]:


first_number = 45
second_number = 85
result = -first_number+second_number
print(result)
if result>25:
    product = (first_number*second_number)
    print(product)
else:
    division = (first_number/second_number)
    print(divison)


# In[32]:


first_number = 70
second_number = 95
result = -first_number+second_number
print(result)
if result>25:
    product = (first_number*second_number)
    print(product)
else:
    division = (first_number/second_number)
    print(division)


# # Research on range() functions and its parameters. Create a markdown cell and write in your own
# words (no copy-paste from google please) what you understand about it. Implement a small
# program of your choice on the same.
# The range function returns a sequence of numbers, starting from 0 and increments by 1 , and stops before a specified number.
# The syntax for range is given by range(start, stop, step) here start is the number we need to start from ; stop refers to the number where we have to end ; step refers to the gap or skip we need while grouping the nu,bers from start to end. 

# In[45]:


print("The natural numbers having gap of 2")
for i in range(1, 20, 2): 

    print(i) 
print() 


# # Research on whether addition, subtraction, multiplication, division, floor division and modulo
# operations be performed on complex numbers. Based on your study, implement a Python
# program to demonstrate these operations

# In[50]:


first_number = 2+3j 
second_number = 4+5j
add = first_number+second_number
print(add)


# In[52]:


first_number = 2+3j
second_number =4+5j
subtract = first_number-second_number
print(subtract)


# In[51]:


first_number = 2+3j
second_number = 4+5j
multiply = first_number*second_number
print(multiply)


# In[54]:


first_number = 2+3j
second_number = 4+5j
divide = first_number/second_number
print(divide)


# The Modulus divisoin is not possible for complex numbers. 

# In[ ]:





# In[ ]:




