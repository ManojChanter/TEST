def say_hello(username):
    print("hello" + username)
user_name = input("Please enter your name")
say_hello(user_name)
say_hello("Manoj")

y= say_hello("Manoj")
print(y)
def multiply_by_three(num):
    return num * 3
def multiply(num1,num2):
    result = num1 * num2
    return result

print("multiplication test")
print(multiply(num2=20, num1=30))

y = multiply(3.5,27.99)
print(type(y))
print(y)

def hello_world_enterprise_edition(username, greeting_phrase="Hello"):
    return greeting_phrase + username
print(hello_world_enterprise_edition("Manoj"))
print(hello_world_enterprise_edition("Manoj", "Good Morning"))

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1,2,3)
print(result)

dummy_variable= 10




def my_function():
    global dummy_variable
    dummy_variable =5
print(dummy_variable)

my_function()
print(dummy_variable)

def test_function(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])
test_function(name= "Manoj", id=18)

def return_multiple_things():
    return(1, 2,"Manoj")

num11,num22, name = return_multiple_things()
print(num11,num22, name)


