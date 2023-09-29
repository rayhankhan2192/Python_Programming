s1s = set([1,2,3,4,5,6,7,7])#set remove multiple value from set datalist
#s1 = set{1,2,3,4,5,6,7,8} #also we can create set with {}

s1s.add(8) #add value to set
s1s.update([10,11,12]) #to add multiple value use update method

#if value not exist in the list remove() throw error
#if we use discard() and if value not exist it will return existing list
s1s.remove(1) #to remove the value
s1s.discard(100)
#print(s1s)


#here some important operations abour sers
ss1 = {1,2,3,10}
ss2 = {2,3,4}
ss3 = {3,4,5}

ss4 = ss1.intersection(ss2) #returns just common value between 2 or more sets
ss5 = ss1.intersection(ss2,ss3)
print("\nIntersection between ss1 and ss2    :",ss4)
print("\nIntersection between ss1 and ss2,ss3:",ss5)

#return the difference value which is not present in the ss2
print("Difference between the sets:",ss1.difference(ss2))

#return the uncommoon value between the sets
print(ss2.symmetric_difference(ss1))

#from List we can remove duplicate by using set method
lists = [1,2,3,4,4,4,5]
print(list(set(lists)))