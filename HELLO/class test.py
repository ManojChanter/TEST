print("12345" + "!")
a = "12345"
print(str(a) + "!")

"""The try block lets you test a block of code for errors. The except block lets you handle the error. 
The finally block lets you execute code, regardless of the result of the try- and except blocks."""

""" #range in for loop
python range() function generates the immutable sequence of numbers starting from the given start integer to the stop integer. It is a built-in function that returns a range object consists of a series of integer numbers, which we can iterate using a for loop.

In Python, Using a for loop with range(), we can repeat an action a specific number of times. For example, let’s see how to use the range() function of Python 3 to produce the first six numbers.

Example

# Generate numbers between 0 to 6
for i in range(6):
    print(i)

Output

0
1
2
3
4
5"""

def adjacentElementsProduct(inputArray: List[int]) -> int:
    return max(inputArray[i] * inputArray[i+1]
        for i in range(len(inputArray) - 1))