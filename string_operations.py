
name = "Michael Jackson"

print(name[0:4]) #Mich   /  Slicing

print(name[8:12]) # Jack   /  Slicing 

print(name[::2]) # McalJcsm   / Stride

statement = name + "is the best !"

print(statement)

print(len(name))

print( 3 * "Homer ")

print("Michael Jackson \n is the best")

print("Michael Jackson \t is the best")

print("Michael Jackson \\ is the best")

print(r"Michael Jackson \is the best")

simpson = "Homer Simpson"

print(simpson.upper())

print(simpson.replace('Homer', 'Bart'))

print(name.find("el")) # 5

nome = "Tio Talhadão"
idade = 54

print(f"My name is {nome} and my age is {idade}.")

print("My name is {} and my age is {}.".format(nome, idade))

print("My name is %s and my age is %d."%(nome, idade))

"""
import re
s1 = "Michael Jackson is the best"
pattern = r"Jackson"
result = re.search (pattern, sl)
if result:
    print('Match found')
else:
    print("Not found") 
"""