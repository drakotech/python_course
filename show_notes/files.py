# How to Create and Write to a File in Python

file_builder = open("logger.txt", "w+")
# w+ allows us to write to that file

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")


# file_builder.write("Hey, I'm in a file!")

file_builder.close()
# Required after write is called


"""
'open' is a function built into python used to open and 
create files.

When you open a file and use .write you will override 
its content.


"""