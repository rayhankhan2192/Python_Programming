valuess = [1,2,13,6,20,7,200,15,18,200,3,11,6,9,16]
print(valuess, end="\n")

valuess.append(100) #add new value to the list
print(valuess, end= '\n')

valuess.insert(0, 200)#insert value to the declared index
print(valuess, end=" \n")

valuess.remove(1)#remove the value
print(valuess, end="\n")

valuess.pop()#remove last number of the List
print(valuess, end="\n")

print("2 in the index of:",valuess.index(2), end="\n")#get the index number of the value
print("831 is present:",831 in valuess)#to check the number is exist in the List
print("Total 200:",valuess.count(200))

valuess.sort()#to sort the List
print("Sorted List:",valuess)

valuess.reverse()#Reverse the sorted List
print("Reverse the List:",valuess)

newList = []
for numbers in valuess: #remove dupplicate and append to new List
    if numbers not in newList:
        newList.append(numbers)
print("After remove duplicate:", newList)

valuess.clear()#to clear all the value
print("clkear all the values:",valuess)