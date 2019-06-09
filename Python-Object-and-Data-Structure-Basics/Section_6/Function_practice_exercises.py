def lesser_of_two_evens(num1, num2):
    '''
    DOCSTRING: LESSER OF TWO EVENS
    :param num1: two given numbers
    :param num2:
    :return: returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶
    '''
    if num1%2 == 0 and num2%2 ==0:
        return min(num1,num2)
    else:
        return max(num1, num2)


# print(lesser_of_two_evens(2,5))


def animal_crackers(text):
    '''
    DOCSTRING: ANIMAL CRACKERS
    :param text: takes a two-word string
    :return: returns True if both words begin with same letter¶
    '''
    return text.lower().split()[0][0] == text.lower().split()[1][0]


# print(animal_crackers("Levelheaded Llama"))


def makes_twenty(num1, num2):
    '''
    DOCSTRING: MAKES TWENTY
    :param num1: Given two integers
    :param num2:
    :return: return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
    '''
    return  num1 == 20 or num2 == 20 or num1+num2 == 20

# print(makes_twenty(10,10))

# LEVEL 1 PROBLEMS


def old_macdonald(name):
    '''
    DOCSTRING: OLD MACDONALD
    Write a function that capitalizes the first and fourth letters of a name¶
    :param name: string
    :return: string
    '''
    print(name[0:3].capitalize()+ name[3:].capitalize())


# old_macdonald("natalia")


def master_yoda(text):
    '''
    DOCSTRING: MASTER YODA
    :param text: Given a sentence
    :return: return a sentence with the words reversed¶
    '''

    wordlist = text.split()
    wordlist.reverse() # or can reverse with wordlist[::-1] and than join
    return ' '.join(wordlist)

# print(master_yoda('I am home'))


def almost_there(num):
    """
    DOCSTRING: ALMOST THERE
    :param text: Given an integer n
    :return: return True if n is within 10 of either 100 or 200¶
    """
    return abs(num-100)<=10 or abs(num-200)<=10


# print(almost_there(201))

# LEVEL 2

def has_33(nums):
    '''
    DOCSTRING: FIND 33
    :param nums: Given a list of ints
    :return: return True if the array contains a 3 next to a 3 somewhere.
    '''
    if len(nums) >1:
        for i in range(1,len(nums)-1):
            if nums[i] == 3 and nums[i+1] == 3:
            # nums[i,i+2] == [3,3]:
                return True
    return False

# print(has_33([1,3,1,4,5,3,5,3]))


def paper_doll(text):
    '''
    DOCSTRING: PAPER DOLL
    :param text: Given a string
    :return: return a string where for every character in the original there are three characters¶
    '''
    return ''.join([letter*3 for letter in text])

# print(paper_doll("Hello"))


def blackjack(a,b,c): # TODO: DO NOT UNDERSTAND THIS PROBLEM
    '''
    DOCSTRING: BLACKJACK
    :param a:Given three integers between 1 and 11
    :param b:
    :param c:
    :return:if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    '''
    if sum([a+b+c]) <= 21:
        return sum([a+b+c])

    elif sum([a+b+c]) > 21 and 11 in [a,b,c]:
        new_sum = sum([a+b+c]) - 10
        if new_sum < 21:
            return new_sum
        else:
            return "BUST"


# print(blackjack(9,9,11))


def summer_69(arr):
    '''
    DOCSTRING: SUMMER OF '69:
    :param arr: numbers in the array
    :return: Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6
    and extending to the next 9 (every 6 will be followed by
    at least one 9). Return 0 for no numbers.
    If we have 6 it will always nine than
    '''

    # my solution - correct???
    # total = 0
    # add = True
    # for num in arr:
    #     if num != 6 and add:
    #         total += num
    #         continue
    #     if num == 6:
    #         add = False
    #         continue
    #     if num == 9:
    #         add = True
    #         continue
    # return total

    # Jose solution
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total


# print(summer_69([9,9,9,9,6]))


# CHALLENGING PROBLEMS
def spy_game(nums):
    '''
    SPY GAME
    :param nums: list of integers
    :return: True if it contains 007 in order
    '''
    # list_007 = []
    # add = True
    # for index,num in enumerate(nums):
    #     if num == 0 or num == 7:
    #         list_007.append(num)
    #         print(list_007)
    # return list_007 in nums

    # my solution - not correct
    # list_007 = [0,0,7]
    # new_list = []
    # for num in nums:
    #     if num in list_007:
    #         new_list.append(num)
    #
    # return list_007 == new_list

    # Soje solution - genius
    code = [0,0,7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1


# print(spy_game([4,6,0,10,7,0,6,5,7]))


def count_primes(num):
    '''
    COUNT PRIMES
    Write a function that returns the number of prime numbers
    that exist up to and including a given number¶
    :param num:
    :return:
    '''
    #  check for 0 and 1 input
    if num < 2: return 0

    # 2 or greater
    # Store out prime numbers in a list
    list_prime = [2]
    # Counter going up to the input num
    x = 3
    # x is going through every number up to input num
    while x <= num:
        # print(x)
        # check if x is prime number
        for y in range (3,x,2): #  we want to check odd numbers there, even numbers we can divide by 2 so it is NOT a prime numbers
        # for y in list_prime: #  we want to check odd numbers there, even numbers we can divide by 2 so it is NOT a prime numbers
            # print(f'x={x}, y={y}')
            if x%y == 0: # in this case it is not a prime number there
                x += 2 # to hop ahead past that even number
                break
        else: #for/else statment unique to python
            list_prime.append(x)
            x+=2 # we pass even number
    print(list_prime)
    return len(list_prime)


print(count_primes(100))





