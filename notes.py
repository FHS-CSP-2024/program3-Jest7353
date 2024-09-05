# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers

myString="somthing"
myInt=100
myFloat=2.5

#casting exmple
print(myInt/2)
myNewInt="100"
print(int(myNewInt)/2)

num1 = input("please enter a number")
print(int(num1) + int(num1))

print("my int = " + str(myInt))

thing = 500/6
print(thing)
print("my result is " + str(thing))
print("My result is", thing)
print(f"My result is {thing}") #Fstring - {} are for variables


print("FIrst line\nSecond line\nthird line")
print("List header ")
print("\t*item1")
print("\t*item2")
print("\t*item3\n\t*item4\n\t*item5")

#File path example
#c:\Users\myname\Documents\onenote notebooks

print("C:\\User\\mrJohnson\\Document\\odafasfsafasfdsafsa")







## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your name? ")
#print(name)
#print(Name)
#
# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \
