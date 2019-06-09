'hello'
"Hello"
" I don't do that"

# order sequences if characters
# use indexing and slicing

# white spaces count as caracters

print("hello \nworld")
print("hello \tworld")

len("hello")
len("I am")

mystring = "Hello World"
mystring[0]
mystring[8]
mystring[9] # the same as mystring[-1]

mystring = 'abcdefghijk'
mystring[2:] #cdefghijk
mystring[:3] # stop index, up to but not included
mystring[3:6]
mystring[1:3]
mystring[::] # all string
mystring[::2]
mystring[::-1] # reverse string

# immutability of strings
name = "Sam"
# does not support item assignment
last_letters = name[1:]
"P" + last_letters
x = "Hello world"
x = x + " it is beautiful outside"
print(x)

letter = "z"
letter = letter * 10
print(letter)

x = "Hello Word"
x = x.upper()
print(x)

x = "Hello Word"
x.lower()

x = "Hello Word life is beautiful"
x = x.split("o") # it will remove "o"
print(x)

print("hello")

print("This is a string {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {0} {0} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# Float formatting
result = 100/777
print("The result was {}".format(result))
print("The result was {r:1.3f}".format(r =result))
print("The result was {r:10.3f}".format(r =result))

# f string formating

name = "Jose"
print(f"Hello, his name is {name}")

name = "Jose"
age = 3
print(f"{name} is {age} years old.")


# assessment
s = "hello"
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])