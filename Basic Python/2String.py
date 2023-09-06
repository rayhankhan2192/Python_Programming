str = 'I like python programming'
str2 = " also i like JAVA"
str3 = "Khan"
print(str)
print(str + str2)
print("Rayhan [" +str3+"]" +str2)
print(len(str))
print(str.upper())#convert to Upper case
print(str.lower())#convert to lower case
print(str.find('l'))#find the character
print(str.find('python'))#find the word
print(str.replace("like", "love"))#replace the word like to love
print(str)#main variable still no change
print("python" in str)#retutn True if exist