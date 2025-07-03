"""Inputs of python"""
"""Name=input("Enter your name: ")
age=int(input("Enter your age: "))
degree=float(input("Enter your degree: "))
Equation=eval(input("Enter your equation: "))
age=float(age)
print('The name is:',Name)
print(age)
print(degree)
print(Equation)"""
"""Swaping values"""
"""a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)"""
"""Operators"""
"""a=58
b=7
print(a/b)
print(a//b)
print(a%b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b or a==b)
print(not(a>b and a<b))"""
"""Identity Operator: checks weather both variables have same datatype or not"""
"""print(a is b)
print(a is not b)"""
"""Bitwise: make answers according to the bit values of those numbers"""
"""print(a & b)
print(a | b)
print(a ^b)
print(a<<1)
print(a>>2)"""
"""Condotional statements"""
"""if a!=b:
    print('a is equal to b')
    print('a is less than b') if a<b else print('a is greater than b')

if a%2==0:
    print('a is even')
else:
    print('a is odd')"""
e=int(input("Enter an Number to get Table: "))
for i in range(1,11):
    print(e*i)
