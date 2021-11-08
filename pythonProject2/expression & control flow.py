print("hello world")

#greet me
print("hello_Manoj")

#rearranging the sentence
print("Humpty Dumpty sat on a wall,")
print("Humpty Dumpty had a great fall.")
print("All the king's horses and all the king's men")
print("Couldn't put Humpty together again.")

#print classmates names
print("hi, manoj")
print("hi, chanter")
print("hi, sekharrao")

#INT, FLOATING POINT & String
print(int(100))
print(float(5.5))
print(str("manoj"))

#Integers
print(100)
print(200)
print(5)

#Floats
print(15.5)
print(100.2)
print(1.1)

#Number Operations : + * / -
print(15 + 5)
print(100 + 250)
print(25 - 50)
print(85 - 98)
print(15 * 68)
print(25 * 89)
print(100 / 25)
print(68 // 78) #only shows values before decimal point
print(2 + 5)

#Booleans
print(True)
print(False)
print(True)
print(False)

#Strings
print("manoj")
print("chanter")
print("manoj" + "chanter")
print("\" what is you name \"- question")

## Write a program that prints a few details to the terminal window about you
# It should print each detail to a new line.

name = "manoj chanter"
age = 25
weight_kg = 74
height_cms = 179.2
print(name)
print(age)
print(weight_kg)
print(height_cms)

## Create a program that prints a few operations on two numbers: 22 and 13
a = 22
b = 13
print(a + b)
print(a * b)
print(a / b)
print(a - b)
print(a // b)

# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

working_hours = 6
sememster_Week = 17
print(working_hours * sememster_Week * 5)

#Creating different variables for each type

#string
mk = "manoj"
print(mk)
#BOOLEAN
km = True
print(km)
#integer
mank = 143
print(mank)
#floating point

mankee = 143.25
print(mankee)

# Assigning and creating a variable, (define its value)
a = 100
# Mutate a variable, (redefine its value)
a = 150
print(a)

#Arithmetic Assignment Operators
a = 12
a += 4  #increement the value
print(a)
b = 12
b -= 4 #decreement
print(b)
c = 15
c *= 3 #multiplies the value
print(c)
d = 10
d /= 3 #divides the value #prints without decimal numbers : //
print(d)

# Store your favorite number in a variable (as a number)
# And print it like this: "My favorite number is: 8"
number = 8
word = "my favourite number is"
print(word, number)  #we can also combine by using print((word + str(number))

## Swap the values of the variables
a = 123
b= 526
c = a   #creating a new variable to swap
a = b
b = c
print(a)
print(b)

#BMI
name = "manoj"
massInKg = 81.2
heightInM = 1.78
bmi = massInKg / (heightInM ** 2)
print(bmi)

## Define several things as a variable then print their values
# Your name as a string
# Your age as an integer
# Your height in meters as a float
# Whether you are married or not as a boolean

name = "manoj"
age = 24
height_cms = 179.5
martial_status = False
print(name+"\n" + str(age)+"\n" + str(height_cms)+"\n"+ str(martial_status)+"\n")  #used this +"\n" to print horizontally #used str to print the int values


#variable Mutation
a = 3   # make the "a" variable's value bigger by 10
a += 10
print(a)

#b = 100
# make b smaller by 7

b = 100
b -= 7
print(b)

#c = 44
# please double c's value

c = 44
c *=2
print(c)

#d = 125
# please divide by 5 d's value

d = 125
d /= 5
print(d)

#e = 8
# please cube of e's value

e = 8
e= e**3
print(e)

#f1 = 123
#f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)

f1 = 123
f2 = 345
if f1 < f2:
    print(True)
else:
    print(False)

#can be done in another way
print(f1<f2)

#g1 = 350
#g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)

g1 = 350
g2 = 200
g2 += g2
print(g1<g2)

#h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)

h = 1357988018575474
print(h%11 ==0) #used == to equal both leftandright #divisor is 0

#i1 = 10
#i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)
i1 =10
i2 = 3
print(i1 > (i2**2) < (i2**3))

#j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)

j = 1521
print(j%3==0 or j%5==0)


## Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000
Surface_Area = 600
Volume =1000
l = 10.0
b = 10.0
h = 10.0
Surface_Area = l*b*h
Volume = 2*l*b+ 2*b*h + 2*l*h
print(Surface_Area, Volume)


current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented by the variables

def secondsToText(secs):
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60
    result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
    ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
    ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
    ("{0} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    return result





