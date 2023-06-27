#!/usr/bin/env python
# coding: utf-8

# 1)Explain with an example each when to use a for loop and a while loop.
# 
# -A while loop is used when we want to repeat a block of code as long as a specific condition is true. The loop continues executing the code until the condition becomes false. 
# 
# -A for loop is used when we want to iterate over a sequence of elements (such as a list, tuple, string, or range) or any object that is iterable. It allows you to loop over each element in the sequence and perform some operation on it. 

# In[3]:


#2)Write a python program to print the sum and product of the first 10 natural numbers using for
#and while loop.


sum_num = 0
for i in range(1, 11):
    sum_num += i


product_num = 1
for i in range(1, 11):
    product_num *= i


print("Using for loop:")
print("Sum:", sum_num)
print("Product:", product_num)


# while loop
sum_r = 0
i = 1
while i <= 10:
    sum_r += i
    i += 1


product_r = 1
i = 1
while i <= 10:
    product_r *= i
    i += 1

print("Using while loop:")
print("Sum:", sum_r)
print("Product:", product_r)



# In[14]:


#3)Create a python program to compute the electricity bill for a household.
def calculate_electricity_bill(units):
    total_bill = 0

    if units <= 100:
        total_bill = units * 4.5
    elif units <= 200:
        total_bill = (100 * 4.5) + ((units - 100) * 6)
    elif units <= 300:
        total_bill = (100 * 4.5) + (100 * 6) + ((units - 200) * 10)
    else:
        total_bill = (100 * 4.5) + (100 * 6) + (100 * 10) + ((units - 300) * 20)

    return total_bill


# Test the function
units_consumed = int(input("Enter the number of units consumed: "))
bill_amount = calculate_electricity_bill(units_consumed)
print("Electricity Bill Amount: Rs.", bill_amount)



# In[17]:


#4)Q4. Create a list of numbers from 1 to 100. Use for loop and while loop 

#for loop
n = list(range(1, 101))
result_l = []

for num in n:
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        result_l.append(num)

print("Using for loop:")
print(result_l)

#using while 
numbers = list(range(1, 101))
result_list = []

i = 0
while i < len(numbers):
    cube = numbers[i] ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        result_list.append(numbers[i])
    i += 1

print("Using while loop:")
print(result_list)


# In[18]:


#5)
def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in string.lower():
        if char in vowels:
            count += 1

    return count


string = "I want to become a data scientist"
vowel_count = count_vowels(string)

print("Number of vowels:", vowel_count)


# In[ ]:




