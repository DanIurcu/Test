from random import randint

fruits=["Banana","Apple","Kiwi","Pear","Orange"]

name=input("What's your name? ")

print("Hello "+name+", your favourite fruit is "+fruits[randint(0,len(fruits)-1)])

print()
input("Press return to continue...")
