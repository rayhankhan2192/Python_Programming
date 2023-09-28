with open('file.txt', 'r') as f:
    file_contetnt = f.read()

    print("File name:",f.name) #to show the file name
    print("File Mode:",f.mode) #to show the file mode
    print(file_contetnt) #print the hole file content
    print("CHAR read:",f.tell()) #how many character are read