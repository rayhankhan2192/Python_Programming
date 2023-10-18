#basic function
def fun1(name):
    return f"F1: Hello {name}"
result1 = fun1("Rayhan Khan")
print(result1)

#Function with basic arguement
def fun2(name, greeting="Hello"):
    return f"F2: {greeting} {name}"
result2 = fun2("Rayhan Khan")
print(result2)

#variavle length argurmrnt
def sum_numbers(*value):
    return sum(value)
result3 = sum_numbers(1,2,3,4,5)
print("F3: SUM :",result3)

#recursive function Factorial
def factorial(value):
    if(value == 0):
        return 1
    else:
        return value * factorial(value-1)
result4 = factorial(5)
print("F4: Factorial :",result4)

#lambda function
addition = lambda x,y: x+y
result5 = addition(5,5)
print("F5: Addition:",result5)

square= [1, 2, 3, 4, 5]
result6 = list(map(lambda x: x**2, square))
print("F6: Square:",result6)  # Output: [1, 4, 9, 16, 25]
