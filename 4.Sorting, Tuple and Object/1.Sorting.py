li_1 = [9,2,6,3,1,7,10,5,4,8]

li_2 = sorted(li_1)

print("Unsorted List:",li_1)
print("Sorted List  :",li_2)

#tupple
tup = (9,2,6,3,1,7,10,5,4,8)
s_tup = sorted(tup)
print("\n\nSorted Tupple:",s_tup)

#dictionary
dic = {'Name':'Rayhan Khan', 'Position':'Software Engineer', 'Age':'22'}
s_dic = sorted(dic)
print("Sorted Dictionary:",s_dic)

#Example

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)
    

e1 = Employee("Rayhan Khan", 21, 1000000)
e2 = Employee("Mostakim Hossain", 23, 1100000)
e3 = Employee("Abdullah Al Mamun", 22, 1200000)

employee = [e1,e2,e3] #List

#def sort_method(emp): #this method return the key value to sort
    #return emp.salary #sort in salary

#e_employee = sorted(employee, key=sort_method)
e_employee = sorted(employee, key=lambda e: e.name) #if we use this no need sort_method
print('\n',e_employee)