import math

def vol(rad):
    '''
    Write a function that computes the volume of a sphere given its radius.
    :param rad: radius
    :return: volume
    '''
    return (4/3)*math.pi*(rad**3)

print(vol(2))

def ran_check_1(num,low,high):
    if low < num < high:
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is NOT in the range between {low} and {high}"

def ran_check(num,low,high):
    if num in range(low,high):
        return f"{num} is in the range between {low} and {high}"
    else:
        return f"{num} is outside the range between {low} and {high}"

print(ran_check(6,2,7))
print(ran_check(-4,-7,-3))

def ran_bool(num,low,high):
    return num in range(low,high)

print(ran_check(0,2,7))
print(ran_check(-3,-7,-3))



def up_low_1(s):
    upper_counter = 0
    lower_counter = 0
    for letter in s:
        if letter == letter.upper() and letter.isalpha():
            upper_counter = upper_counter + 1
        elif letter != letter.upper() and letter.isalpha():
            lower_counter = lower_counter + 1
    return f"No. of Upper case characters : {upper_counter}\n" f"No. of Lower case Characters : {lower_counter}"

def up_low(s):
    d = {"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    return f"Original String :  {s}\n" \
           f"No. of Upper case characters : {d['upper']}\n" \
           f"No. of Lower case Characters : {d['lower']}"


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
print(up_low(s))


def unique_list_1(lst):
    return list(set(lst))

def unique_list(lst):
    x = []
    for num in lst:
        if num not in x:
            x.append(num)
    return x

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))


def multiply_1(numbers):
    result = 1
    for num in numbers:
        result = result*num
    return result

def multiply(numbers):
    result = numbers[0]
    for num in numbers:
        result *= num
    return result

print(multiply([1,2,3,-4]))


def palindrome_1(s):
    s = s.replace(' ', '')
    first_half = s[:int(len(s)/2)]
    second_half = s[int(len(s)/2):]
    if first_half == second_half[::-1] or first_half == second_half[::-1][:-1]:
        return True

def palindrome(s):
    return s == s[::-1]

print(palindrome('helleh'))
print(palindrome('madam'))
print(palindrome('nurses run'))


import string

def ispangram_1(str1, alphabet=string.ascii_lowercase):
    result = ""
    for letter in str1:
        if letter not in result and letter.isalpha():
            result +=letter.lower()
    return ''.join(sorted(result)) == alphabet

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    # print(alphaset)
    # print(alphabet)
    # print(set(str1.lower()))
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))