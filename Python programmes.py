#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

# In[1]:


str="aitam1234AECEColLege$%^%$"
upper,lower,number,special=0,0,0,0
for i in str:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
    elif i.isnumeric():
        number= number+1
    else:
        special=special+1
print(upper,lower,number,special)


# In[2]:


str="aitam1234AECEColLege$%^%$"
upper,lower,number,special=0,0,0,0
for i in range(len(str)):
    if str[i].isupper():
        upper=upper+1
    elif str[i].islower():
        lower=lower+1
    elif str[i].isnumeric():
        number= number+1
    else:
        special=special+1
print(upper,lower,number,special)


# # tables

# In[8]:


def multi_number(i):
    a=1
    print("MULTIPLICATION TABLE OF",i)
    while a<=10:
        result=i*a
        print('{} X {}='.format(i,a),result)
        a=a+1
multi_number(5)
    


# In[25]:


num=5
n=int(input("enter number of terms required"))
print("MULTIPLICATION TABLE OF",num)
for i in range(1,n+1):
    print("{} * {} = {}".format(i,num,i*num))


# In[19]:


def mul_table(num):
    """print multiplication table of given number"""
    n=int(input("enter number of terms required"))
    print("MULTIPLICATION TABLE OF",num)
    for i in range(1,n+1):
        print("{} * {} = {}".format(i,num,i*num))
mul_table(3)


# # Matrix Multiplication

# In[13]:


def matrix_multiplication():
    a = [[1,3,2],
     [4,3,5],
     [7,8,9],
     [1,2,3]]
    b = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0]]
    result=[]
    add=0 
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(b)):
                add=add+a[i][k]*b[j][k]
            result.append(add)
    print(result)
    result1=[]
    for x in range(0,len(result),len(b)):
        result1.append(result[x:x+len(a)])
    print(result1)


# In[14]:


matrix_multiplication()


# # Replace the digits in the string with "# "

# In[27]:


str1= "ret%45*6&*hter^&%1/24.3"
digits="0123456789"
lis=[]
for i in str1:
    if i in digits:
        lis.append(i)
        
print(len(lis))
print('#'*len(lis))


# # Students marks dashboard

# In[60]:


Students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] 
Marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]
dictionary=dict(zip(Students,Marks))
top_five=(sorted(dictionary.values())[5:])[::-1]
bottom_five=sorted(dictionary.values())[:5]
print("Top five students")
for x in top_five:
    print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(x)])
    print("Marks:",x)
print()  
print("Bottom five students")
for y in bottom_five:
    print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(y)])
    print("Marks:",y)
print()  
print("students marks between 25 & 75")
for z in dictionary.values():
    if z>25 and z<75:
        print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(z)])
        print("Marks:",z)
    


# In[63]:


Students=['student1','student2','student3','student4','student5','student6','student7','student8','student9','student10'] 
Marks = [45, 78, 12, 14, 48, 43, 47, 98, 35, 80]
def student_marks(Students,Marks):
    dictionary=dict(zip(Students,Marks))
    top_five=(sorted(dictionary.values())[5:])[::-1]
    bottom_five=sorted(dictionary.values())[:5]
    print("Top five students")
    for x in top_five:
        print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(x)])
        print("Marks:",x)
    print()  
    print("Bottom five students")
    for y in bottom_five:
        print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(y)])
        print("Marks:",y)
    print()  
    print("students marks between 25 & 75")
    for z in dictionary.values():
        if z>25 and z<75:
            print("Name of Student:",list(dictionary.keys())[list(dictionary.values()).index(z)])
            print("Marks:",z)


# In[64]:


student_marks(Students,Marks)


# In[ ]:




