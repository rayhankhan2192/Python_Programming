#we can store all types of data type in Dictionaries
student = {'name':'Rayhan Khan', 'age':22, 'courses':['Math','Physics','biology']}
print(student)

print(student['name'])
print(student['age'])
print(student['courses'])

print(student.get('number', 'Not Found'))# if data not exist it will return None

#to update multiple value in dictionaries 
student.update({'name':'Harry kane','age':30, 'number':5463656})
print(student)

#to delete key value from dictionaries
del student['age']
print(student)

print(len(student))#length of dictionaries

print()
print(student.keys())#return all keys
print(student.values()) #return all value 
print(student.items())#return all items

print()
for key in student:
    print(key)

print()
for keys, values in student.items():
    print(keys, values)