""" x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis') """
#the above code acts as a else statement

#print(123)
# 123 is constant
#print('Hello world')
#variable name must start with letter or underscore

""" x=0.6
x = 3.9 * x * (1-x)
print(x) """

# ** --> This means power

# Paranthesis -> power -> multiplication -> addition -> left to right 
# above is the operator precedence

#concatenation
""" hi = 'Hello' + ' There'
print(hi) """

#type() function is used to find the data type of the variable
""" xx=1
print(type(xx)) """

#float() function used to convert to floating point number
# print(float(99)+100)

#python produces float answer even for integer division
# print(10/2)

""" sval = '123'
print(type(sval))
ival=int(sval)
print(ival)
print(type(ival)) """

#cannot convert string to int and float form only if it contains numeric characters

# input() function to get the input from the user
""" name=input('who are you? ')
print('Welcome', name) """

""" boolean expression
<
<=
==
>=
>
!= """

#indentation is very important in python
#avoid using tabs in python

""" for i in range(5) :
    print(i) """

""" print('this is nested decisions')
x=45
if x>1:
    print('More than one')
else:
    print('Less than 100')
print('All done') """

#if else ladder
""" x=5
if x<2 :
    print('small')
elif x<10 :
    print('Medium')
else :
    print('LARGE')
print('All done') """

# try and except is surrounded under dangerous code which can blow up
#  they help to stop the program if the program fails at the above functions

""" astr = 'Hello world'
try:
    istr = int(astr)
except:
    istr = -1
print('First ', istr) """

""" astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('First ', istr)  """

# do not overuse try/except it is like if else statements but used for
# dangerous code

# def is used to define a function 
""" def thing():
    print('Hello')

thing() #invocing the function
print('zip')
thing() """

# max  and min are built in functions in python 
""" big = max('Hello world')
print(big)
tiny=min('Hello world')
print(tiny) """

# min returns space as minimum if provided 
# int() and float() are built in functions
# you can also use the above functions in string but it must contain numeric characters

# big=max('Hello world')
# hello world above is an argument int the function


#lang is a parameter
""" def greet(lang):
    if lang<1:
        print('Hi')
    else:
        print('bye')
greet(2) """

#return used to come out of loop
""" def greet():
    return "Hello"
print(greet(),"Glenn") """

# multiple parameter in function can be used

# when loop becomes false it terminates
""" n = 5
while n > 0 :
    print(n)
    n=n-1
print('Over')
print(n) """

# True is a built in function 
""" while True:
    line = input('> ')
    if line =='done' :
        break
    print(line)
print('Done!') """
 
# continue stops the current iteration and jumps to top of the loop

# indefinite loops work until the condition becomes false 

# i values are changing in this loop 
""" for i in [5,4,3,2,1] :
    print(i)
print('Done!') """

""" friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy new year: ', friend)
print('Done!') """

""" iteration variable --> i
Block or body  --> print() or something
iteration sequence --> [5,4,3,2] """

# definite loop using strings 
""" freinds={'Joe','Rog','Rag'}
for friend in freinds :
    print("Hello: ",friend)
print('Done!') """

# loop idioms
#finding largest value
""" largest=-1
print('Before', largest)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest:
        largest=the_num
    print(largest,the_num)
print('After', largest) """

# counting in a loop 
""" zor=0
for thing in [9,41,12,3,74,15]:
    zor=zor+1
print(zor) """

# summing to get total and finding average
""" count=0
zor=0
for thing in [9,41,12,3,74,15]:
    zor=thing+zor
    count=count+1
print(zor/count)  """

#searching using boolean variables
""" found = False
for value in [9,41,12,3,74,15]:
    if value == 74:
        found=True
    print(found, value) """

# boolean has two value 
# none has one value it is a constant it is used to show emptyness

# is and isnot operators 
# is is used when we want to check if we have same type and value of the variable

# 0==0.0 is true but, 0 is 0.0 is False as both are of different type
""" smallest = None
for value in [3,41,129,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print(smallest) """


# use "is" an0d "is not" on boolean and num types only !!!!!!!!!!!!!!!!!!!!!!!!!!

# strings
# index starts from zero
""" fruit = 'banana'
letter = fruit[1] """

# [] index specifier 

""" x=3
letter = fruit[x-1]
print(letter)"""

# you cannot index beyond the string

# gets length of the string
""" fruit = 'banana'
x = len(fruit)
print(x) """

# remember to use [] brackets for index and not ()
# looping through strings
""" fruit = 'banana'
i=0
while i<len(fruit):
    letter = fruit[i]
    print(i,letter)
    i = i +1 """

# using definite loop 
# use letter in print statement
""" fruit = 'banana'
for letter in fruit:
    print(letter) """

#looping and counting the letters in the input

""" word ='banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count) """

""" for letter in 'banana':
    print(letter) """

# slicing strings
""" s= 'Monty Python'
print(s[0:4]) """
#upto 4 and not including 4 so 0,1,2,3 elements will be printed
""" print(s[6:20])
print(s[:2]) """
# upto 2 but not including 2
# print(s[8:]) 
# from 8 to end 
# print(s[:]) 
#prints everything

#using "in" as a logical operator

""" fruit = 'banana'
if 'n' in fruit:
    print('Found') """

#string comparision
""" word='fruit'
if word =='banana':
    print('B')
elif word>'banana':
    print('Yo')
elif word<'banana':
    print('dawg') """
#other operations works for sorting the alphabets

#string library

""" greet = 'Hello Bob'
print('Hi there',greet.lower()) """
# here lower() is a library function

# type(string_name) gives the class of string which it belongs to 

# dir(string_name) gives all the x._____() the methods that can fill the blank space 

#find() function
""" fruit = 'banana'
pos=fruit.find('na')
print(pos) """

#upper and lower method
""" greet = 'Hello world'
print(greet.upper())
print(greet.lower()) """

#search and replace
""" greet ='Hello bob'
nstr = greet.replace('bob', 'Jane')
print (nstr)
#replaces all o's with X's
nstr = greet.replace('o', 'X')
print (nstr) """

#stripping whitespace

""" greet ='     Hello bob       '
print(greet.lstrip()) #removes left space
print(greet.rstrip()) #removes right space
print(greet.strip()) #remove space on both left and right """

#prefixes 
# startswith() function 
#return boolean value if the string starts with any letter
""" line ='Hello'
print(line.startswith('He'))
print(line.startswith('p')) """

""" new line "\n" is the command 
\n is considered as a string and is considered when index of the 
string is considered """

# [] is used to write lists 
""" freinds = [ 'joe', 'Rogan']
print([1, 24, 76]) """

# list can have all the data types in it like [int , float, string]
# there are empty lists too
#for can be used to go through the list elements 

#indexing starts from index zero
""" freinds = ['Joe', 'Rogan', 'Josh']
print(freinds[0])
print(freinds[1]) """

# strings cannot be changed after you declare them 
# they are immutable
# but lists are mutable and can be changed 

# len() function
# x = [1, 2, 3] 
# print(len(x))

#range function
# can be used in the for loops
# print(range(len(x))) 


""" for i in range(len(x)):
    y = x[i]
    print(y) """

#lists can be declared in the below way too
""" fruit = "banana"
x = fruit[1]
print(x)
 """
# concatenate lists using + 
""" a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) """

#lists can be sliced too
""" t = [9 , 41, 12, 3, 74, 15]
print(t[1:3]) """
# index 1 to 2 will be printed 

#list methods
""" x = list()
print(type(x))
dir(x) you will get all the functions avaliable for lists """

""" stuff = list()
#assigns an empty list
stuff.append('Book')
#appends book value in list
print(stuff) """

# in operator can be used to find if something is present in the list
""" some = [1, 9 , 21, 10, 16]
print(9 in some)
#not in operator
print(21 not in some) """

#lists are in order and we can sort them up
#sort() function is used
""" friends = [ 'Joseph', 'Glenn', 'sally']
friends.sort()
print(friends)
print(friends[1]) """

# other lists functions
""" some = [1, 9 , 21, 10, 16]
print(len(some))
print(max(some))
print(min(some))
print(sum(some))
print(sum(some)/len(some)) """

#functions uses more memory than using loops to perfrom the operations













