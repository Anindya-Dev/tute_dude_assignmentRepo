# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

# try:
#     with open('sample.txt', 'r') as file:
#         print("Reading file content:")
#         for i, line in enumerate(file, 1):
#             print(f"Line {i}: {line.strip()}")
# except FileNotFoundError:
#     print("Error: The file 'sample.txt' was not found.")

#  Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

x=input("Enter text to write to the file: ")
with open('output.txt','w')as file:
    file.write(x+"\n")
    print("Data succesfully written to the file.")
y=input("Enter additional text to append: ")
with open('output.txt','a')as file:
    file.write(y+"\n")
    print("Data succesfully appended")
print("Final content of output.txt: ")
with open('output.txt','r')as file:
    for line in file:
        print(line.strip())


