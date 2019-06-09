# while some_boolean_condition:
    # do something

# else:             # if condition no longer true or since beginning wasn't true
    # do something else

# be careful and do not create infinite while loop
x  = 0
while x< 5:
    print(f'The current value of x is {x}')
    x = x + 1
    # x += 1
else:
    print('X is not less than 5')

# break: Breaks out of the current closest enlosing loop
# continue: Goes to the top ob the closest enclosing loop
# pass: does nothing at all

x = [1,2,3]
for item in x:
    pass

print("end of my script")

mystring = "Natalia"
for letter in mystring:
    if letter == "a": # if we don't want to print letter "a", we have go back to top of loop (for letter in mystring)
        continue
    print(letter)

mystring = "Natalia"
for letter in mystring:
    if letter == "a": # if we don't want to continue after we found letter = "a", not going to execute anything inside the loop anymore
        break
    print(letter)


x = 0
while x < 5:
    if x == 2:
        break # if we don't want to continue after x = 2, no print statement for 2 will be executed.
    print (x)
    x += 1