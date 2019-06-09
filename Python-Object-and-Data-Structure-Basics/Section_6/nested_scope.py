# nested statements

x = 25

def printer():
    x = 50
    return x

print(printer())
print(x)

# LOCAL
lambda num: num**2

# ENCLOSING FUNCTION LOCALS AND GLOBAL

name = 'THIS IS A GLOBAL STRING' # GLOBAL == and third rearching for global here. If we comment
def greet(): # this is enclosing function
    name = 'Samy'  # ENCLOSING == second searching for enclosing function locals here
    def hello(): # this is local function
        name = "Natalia" # LOCAL == first searching for local variables inside of this function
        print("Hello " + name)
    hello()
# JUST COMMENT ONE BY ONE TO UNDERSTAND WHAT IS CALLED

greet()

x = 50

def fun(x):
    print(f'X is {x}')
    # LOCAL REASSIGNMENT
    x = 200
    print(f'I have LOCALLY change X to {x}')

fun(x)
print(x)

x = 50

def func():
    global x # anything what happends with x inside this function will affect global x which define before the func()
    print(f'calling GLOBAL X for the first time: {x}')
    x = 200 # local reassignment on a global variable
    print(f'I have LOCALLY change GLOBAL X to: {x}')
func()
print(f'printing global X which defined before the function, after reassigment: {x}')