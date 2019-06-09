def name_of_function(name): # all lower case with underscore if needed.
    '''
    Docstring explains function
    :return:
    Hello
    '''
    # print("Hello " + name)
    return "Hello " + name


name = name_of_function("Natalia")
print(name)


def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input
    OUTPUT: Hello
    :return:
    '''
    print("Hello")


name_function() # calling the function


def say_hello(name="NAME"): # default value in case you did not provide name
    return "hello " + name


result = say_hello()
print(result)


def add(n1, n2):
    return n1 + n2


result = add(20,30)
print(result)


#  Find out if the word "dog" is in a string

def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

result = dog_check("My besteverdog is very cool")
print(result)


def dog_check(mystring):
    return 'dog' in mystring.lower()


result = dog_check("My besteverdog is very cool")
print(result)


def pig_latin(word):
    first_letter = word[0].lower()
    if first_letter in 'aeyuio':
        pig_word = word + "ay"
    else:
        pig_word = word[1:].capitalize() + first_letter + "ay"
    return pig_word


print(pig_latin('Ahwerlll'))

