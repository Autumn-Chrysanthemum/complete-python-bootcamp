# argument and key-word arguments

def myfunc(a,b):
    return sum((a,b))*0.05

print(myfunc(40,60)) # positional arguments because 40 is assing to a, and 60 is assing to 60

def myfunc(a,b,c=0,d=0):
    return sum((a,b,c,d))*0.05

print(myfunc(40,60,100))


def myfunc(*args): # name can be anything *args = *natalia = *spam, by convention use *args
    print(args) # all parameters will be a tuple
    return sum(args)*0.05

print(myfunc(34,67,34,234))


def myfunc(**kwargs): # name can be anything *kwargs = *natalia = *spam, by convention use *kwargs
    print(kwargs) # return back a dictionary
    if 'fruit' in kwargs:
        print("My fruit of chose is: {}".format(kwargs['fruit']))
    else:
        print("I did not fund any fruit here")

myfunc(fruit="apple", veggie = "avocado")

def myfunc(*args,**kwargs): # have to be the same order as we define
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))


myfunc(10,30,50, fruit="orange", food="eggs", animal = 'dog') # have to be the same order as we define, do not mix


def mynum(mystring):
    new_string = ''
    for item in enumerate(mystring):
        if item[0]%2==0:
            new_string += item[1].upper()
        else:
            new_string += item[1].lower()
    print(new_string)

mynum("asdfghjkl")

