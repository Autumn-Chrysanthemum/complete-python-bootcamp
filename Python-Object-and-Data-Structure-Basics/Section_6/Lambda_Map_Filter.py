#Lambda is one time use function, use one time, never refer to it again
# map = > if some function takes argument and
# you would like to run this function with different arguments (list of them instead of one)

def square(num):
    return num**2

my_num = [1,2,3,4,5,6]

for item in map(square, my_num): # pass function and whatever you want this function to iterate through
    print(item)

# if you want a list back:
print(list(map(square, my_num)))


def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ["Natalia","Alex","Matt","Tatyana"]

print(list(map(splicer,names))) # do NOT call function when passing for example: splicer(), map will do it for us

# filter function


def check_even(num): # create the function which returns True/False
    return num%2 == 0 # return True if number is even


mynums = [1,2,3,4,5,6] # we want to grab only numbers based on function condition

# print(list(filter(check_even,mynums)))
for item in filter(check_even,mynums):
    print(item)

# DIFFERENCE: map applies function to every element on a list BUT filter function will filter based on a function condition

# LAMBDA is anonymous function. You use it only one time. We don't use a name
def square(num):
    result = num**2
    return result


def square(num):
    return num**2

def square(num): return num**2

lambda num: num**2 # == lambda expression

square = lambda num: num**2 # we can check that square is still working
# print(square(5))

# we use lambda with map or filter, because in this case you don't have to define function if you plan to use in once

print(list(map(lambda num: num**2, my_num)))
print(list(filter(lambda num:num%2 == 0, my_num)))
print(list(map(lambda name: name[::-1], names)))
print(list(map(lambda name: name[0], names)))

print(list(map(lambda name:'EVEN' if len(name)%2 == 0 else name[0], names)))

