#Catching Exceptions with try and except
try:
    f = open('pyt_hon.txt')
except FileNotFoundError:
    print("This file doesn't exist!")

print()
#Catching Exceptions with try and except
try:
    res = 10/0

except ZeroDivisionError:
    print("Division by zero is not possible")

except Exception as e:
    print(f"An error occured: {e}")

print()
#Handling Multiple Exceptions
try:
    value = int("int")

except(ValueError, TabError) as e:
    print(f"An error occured: {e}")

print()
#else Block
try:
    num = int("100")
except ValueError:
    print("invalid value")
else:
    print(f"value: {num}")

print()
#finally Block
try:
    f = open('python.txt', 'r')
except IOError as e:
    print("Error occured while reading the file!")
else:
    print(f.read())
finally:
    f.close()
    print("File close successfully!")