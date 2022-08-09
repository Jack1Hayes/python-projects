# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:36:08 2022

@author: Hayes
"""

import numpy as np

#def remove_chars(text, remove):
#    return text[remove:]

#x = remove_chars("pynative", 4)
#print(x)

#numbers_x = [10, 20, 30, 40, 10]
#numbers_y = [75, 65, 35, 75, 30]

#def firstlast(l):
#    if l[0] == l[-1]:
#        return print('True')
#    else:
#        return print('false')

#firstlast(numbers_y)

#oldarray = [10, 20, 33, 46, 55]
#newarray =[]


#def divnum(array, num):
#    for i in range(len(array)):
#        if array[i] % num == 0:
#            newarray.append(oldarray[i])
#    return print(newarray)

#divnum(oldarray, 5)


#str_x = "Emma is good developer. Emma is a writer"

#def findword(string, word):
#    return print(string.count(word))

#findword(str_x, 'Emma')

#def pyramid(pn):
#    for num in range(pn):
#        for i in range(num):
#           print (num, end=" ") #print number
#        # new line after each row to display pattern correctly
#        print("\n")
#    return

#pyramid(10)
'''
revr_num = 0

def recur_reverse(num):  
    global revr_num   # We can use it out of the function  
    if (num > 0):  
        Reminder = num % 10  
        revr_num = (revr_num * 10) + Reminder  
        recur_reverse(num // 10)  
    return revr_num  

def palindromechecker(number):
    if number == recur_reverse(number):
        return print('True')
    else:
        return print('False')
    
palindromechecker(100071)

'''
'''
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
oddevenlist = []

def odd_even_list(list1, list2):
    for i in range(len(list1)):
        if list1[i]%2 == 0:
            oddevenlist.append(list1[i])
    for i in range(len(list2)):
        if list2[i]%2 != 0:
            oddevenlist.append(list2[i])
    return print(oddevenlist)

odd_even_list(list1, list2)
'''
'''
def tax_calculator(ammount):
    if 0 < ammount < 10000:
        return print(0)
    elif 10000 < ammount < 20000:
        return print((ammount - 10000) * 0.1)
    elif ammount > 20000:
        return  print((10000*0.1) + (ammount-20000) * 0.2)
    else:
        return print('error')

tax_calculator(45000)
'''
'''
def times_table(num):
    for i in range(1, num+1):
        for j in range(1, num+1):
            print(i*j, end=' ')
        print('\n')
    return

times_table(10)
'''
'''
def reverse_pyramid(size):
    for i in range(size, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")
    return

reverse_pyramid(5)
'''
'''
def exponent(base, exp):
    return print(base ** exp)

exponent(3, 3)
'''
'''
def adder(num):
    zero = 0
    while num > 0:
        zero += num
        num = num-1
    return print(zero)

adder(3)
'''
'''
def multiplier(num1, num2):
    for i in range(1,num2+1):
        print (num1*i)
    return

multiplier(2,10)
'''
'''
numbers = [12, 75, 150, 180, 145, 525, 50]
new_list=[]

def list_maker(list1):
    for i in range(len(list1)):
        if list1[i] > 500:
            break
        elif list1[i] > 150:
            continue
        elif list1[i] % 5 == 0:
            new_list.append(list1[i])       
    return print(new_list)

list_maker(numbers)
'''
'''
def number_size_counter(num):
    size = 0
    while num > 1:
        size += 1
        num = num // 10
    return print(size)

number_size_counter(9232)
'''
'''
list1 = [10, 20, 30, 40, 50]

def rev_list(array):
    for i in range(len(array)-1, -1,-1):
        print(array[i])
    return
rev_list(list1)
'''
'''
def neg_count(num):
    for i in range(num,0,-1):
        print(i*(-1))
    return

neg_count(10)
'''
'''
def list_done(num):
    for i in range(num+1):
        if i < num:
            print(i)
        elif i == num:
            print('done!')
    return
list_done(5)
'''
'''
def prime_number_finder(start, finish):
    for i in range(start, finish):
        for j in range(2, i-1):
           if i % j == 0:
               break                        
        else:
            print(i)
            
                
    return

prime_number_finder(25, 50)
'''
'''
def fib(num):
    x1 = 0
    x2 = 1
    for i in range(0,num):
        if i % 2 == 0:
            print(x1)
            x1 += x2
        elif i % 2 != 0:
            print(x2)
            x2 += x1
    return

fib(10)
'''
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_array = []

def index_odd_even(text, array):
    if text == 'odd':
        for i in range(len(array)):
            if i % 2 != 0:
                new_array.append(array[i])
        print(new_array)
    if text == 'even':
        for i in range(len(array)):
            if i % 2 == 0:
                new_array.append(array[i])
        print(new_array)
    return
index_odd_even('odd', my_list)
'''
'''
def sum_series(num, times):
    x = num
    sum_array = []
    for i in range(times):
        sum_array.append(x)
        x =+ x + (num*(10**(i+1)))
    z = sum(sum_array)
    print(z)
        
        

    return

sum_series(2, 5)
'''
'''
list1 = [54, 44, 27, 79, 91, 41]

def array_mover(array, move, to):
    mover = array.pop(move)
    array.insert(to, mover)
    print(array)
    return

array_mover(list1, 2, 4)
'''
'''
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
def slice_reverse(array, groups):
    length = len(sample_list)
    chunk_size = int(length / groups)
    start = 0
    end = chunk_size
    
    # run loop 3 times
    for i in range(groups):
        # get indexes
        indexes = slice(start, end)
        
        # get chunk
        list_chunk = sample_list[indexes]
        print("Chunk ", i, list_chunk)
        
        # reverse chunk
        print("After reversing it ", list(reversed(list_chunk)))
    
        start = end
        end += chunk_size
    return

slice_reverse(sample_list, 3)
'''       
    
    