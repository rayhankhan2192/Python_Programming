print("Select operation: (+, -, *, %)")
charr = input("Enter an operator: ")
num1 = input("First Num  : ")
num2 = input("Second Num : ")

if charr=="+":
    sum = float(num1) + float(num2)
    print("SUM: ",sum)
elif charr=="-":
    sub = float(num1) - float(num2)
    print("SUB: ",sub)

elif charr=="*":
    mul = float(num1) * float(num2)
    print("MUL: ",mul)
elif charr=="%":
    div = float(num1) / float(num2)
    rem = float(num1) % float(num2)
    print("DIV: ",div)
    print("REM: ",rem)

else:
    print("Select Wrong Operator")