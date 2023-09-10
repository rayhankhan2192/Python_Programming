from array import*

arr = array('I',[2,4,6,8,10])
for i in range(len(arr)):{
   print(arr[i], end=' ')
}
print()
# for val in arr:{#Another way to print Array
#     print(val)
# }

arr2 = array('u',['R', 'a', 'y', 'h', 'a', 'n'])
for i in range(len(arr2)):
    print(arr2[i], end=' ')
    
print()
    
arr4 = array('d', [1.1, 4.5, 6.7, 23.4])
for v in arr4:
    print(v, end=' ')

arr3 = array('I',[])    
n = int(input("\nEnter the length of the Array: "))
for i in range(n):
    x = int(input("Enter the vaue: "))
    arr3.append(x)
print(arr3)

pos = 0
val = int(input("Enter the value for search: "))
for i in range(len(arr3)):
    if(val == arr3[i]):
        print("value found!")
    else:
        print("Value not available")

    

