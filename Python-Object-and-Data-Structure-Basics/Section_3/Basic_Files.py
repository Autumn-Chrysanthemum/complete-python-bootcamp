
# myfile = open("wrong_text.txt")

myfile = open("text.txt")
read = myfile.read()

print(read)
myfile.seek(0)
read = myfile.read()
print(read)

myfile.seek(0)
read = myfile.readlines()
print(read)

myfile.close() # because if you would like to use this file from different place it will complain that python is still using that file

myfile_1 = open("/Users/natalia/PycharmProjects/complete-python-bootcamp/Python-Object-and-Data-Structure-Basics/text_1.txt")
read = myfile_1.read()
print(read)

myfile_1.close()

# old way to open and new way to open
# new:
with open("text.txt") as my_new_file:
    contents = my_new_file.read()
    my_new_file.seek(0)
    contents_1 = my_new_file.readlines()

print("\nnew way:")
print(contents)
print(contents_1)


with open("text.txt", mode = "r") as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open("text.txt", mode = "r") as my_new_file:
    contents = my_new_file.read()
    print(contents)


with open("my_new_file.txt", mode = "r") as f:
    print(f.read())

with open("my_new_file.txt", mode = "a") as f:
    print(f.write("\n4444"))

with open("my_new_file.txt", mode = "r") as f:
    print(f.read())

with open("asfasdfda.txt", mode= "w") as f:
    f.write("I created file")

with open("asfasdfda.txt", mode= "r") as f:
    print(f.read())