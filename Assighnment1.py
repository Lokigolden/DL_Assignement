#!/usr/bin/env python
# coding: utf-8
# 1) Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.

# In[10]:


mynum = []
for x in range(2000,3200):
    if(x%7==0) &(x%5==1):
        mynum.append(str(x))
print(','.join(mynum))

# 2) Write a Python program to accept the user's first and last name and then getting them
printed in the the reverse order with a space between first name and last name.
# In[14]:


name = input ("What's in your full name")
reversed_name = name[::-1]
print(reversed_name)
    

# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
        Formula: V=4/3 * π * r^3
# In[17]:


pi = 3.14
r = 6
v = 4/3*pi*6**3
print("The volume of sphere is: " , v)


# In[ ]:




