import os
# Write a Python program to count the number of lines in a text file. 
f = open("myfile2.txt", "r")
lines = f.readlines()
num_lines = len(lines)
print(num_lines)
print("===========================================================")
# Write a Python program to count the frequency of words in a file.
f = open("myfile2.txt",'r')
print(f.readlines(0,))
f.close()
print("===========================================================")

# Write a Python program to write a list to a file.
f = open("myfile2.txt",'r')
print(f.readlines())
f.close()
print("===========================================================")

# Write a Python program to copy the contents of a file to another file
f2 = "myfile2.txt"
f3 = "myfile3.txt"
f2 = open(f2, "r")
content = f2.read()
f3 = open(f3, "w")
f3.write(content)print("File copied successfully.")
print("===========================================================")

