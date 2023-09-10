li = [1, 'Rayhan', 'khan', 831, 'learning', 'python', 
      'programming', 3.66, 'CGPA']
print(li)#print the hole List
print(li[1:4])#to print specific declared index
print("length of the List: ",len(li))#length of the List

#2d List 2D List  2D List

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [55, 64, 23],
]

matrix[0][1] = 100 #override 20 t0 100

print("1*2 matrix: ",matrix[0][1])
print("2*1 matrix: ",matrix[1][0])
print("3*3 matrix: ",matrix[2][2])
print(matrix)

for row in matrix: #print the all value of the List
    for items in row:
        print(items, end=' ')

print("\nLength of 2D List: ", len(matrix))