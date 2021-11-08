
tail_position = 0
if tail_position == 0:
    tail_position=1

else:
    tail_position=0

dog_on=False

while dog_on ==True:
    if tail_position ==0:
        tail_position =1
    else:
      print(tail_position)
for tail_movements in range(6,18,):
    print(tail_movements)

my_list=["apple, samsung, oneplus"]
for tail_movements in my_list:
    print(my_list)
my_tuple = ("num1, num2")
my_set = {10, 20, 30}
my_dictionary = {"xxx, yyy, zzz"}
for tail_movements in my_list:
   print(tail_movements)
x=0
while x<=10:
    print("i wont cheat on exams")
    x=x+1


for i in range(1,501,2):
  print(i)




num1=int(input("enter the number"))
i = 1
while i<=10:
    print(num1,"x", i,"=", num1*i)
    i=i+1

First = int(input("enter the first number"))
Second = int(input("enter the second number"))
if First < Second:
    print("The first number should be bigger")
else:
     for i in range(First,Second):
        print(i)

for i in range(1,100):
    if (i%3==0) and (i%5==0):
        print("fizzbuzz")
    elif (i%3==0) or (i%5==0):
        if (i%3 == 0):
            print("fizz")
        else:
            print("buzz")
    else:
            print(i)


x=int(input("enter the number"))
c = "*"
for num in range (1,(x+1)):
    print(num*c)

n=int(input("enter the number of rows:"))
for i in range(n):
  print(" "*(n-1-i)+"* "*(i+1))

n=int(input("Enter length of a side of a diamond : "))
m=n*2

for i in range(1,m+1):

    if(i>n):

        i=i-n
        print(" "*i+"* "*(n-i))

    else:

        print(" "*(n-i)+"* "*i)




