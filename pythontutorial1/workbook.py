def addition(a, b):
    return a + b
def subtractionO (a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    return a / b
print("""
1.addition
2.subtraction
3.multiplication
4.division
""")
choice = int(input("enter your choice"))
a = int(float(input("enter the first number")))
b = int(float(input("enter the second number")))


if choice ==1:
    print(a + b)
elif choice ==2:
    print(a - b)
elif choice ==3:
    print(a * b)
elif choice ==4:
    print(a / b)
else:
    print("enter the correct choice ")



