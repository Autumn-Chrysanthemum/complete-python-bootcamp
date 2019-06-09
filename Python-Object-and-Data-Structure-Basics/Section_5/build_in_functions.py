# generator

mylist = [1,2,3]
for num in range(10): # will generate from 0 till 10 (not included) , looks like slicing
    print(num)

for num in range(3, 10): # will generate from 3 till 10 (not included) , looks like slicing
    print(num)

for num in range(3, 10, 2): # will generate from 3 till 10 (not included) with step 2, looks like slicing
    print(num)

print(range(10)) # not working this way
print(list(range(10))) # we have to pass in into list

# enumirate function

index_count = 0
for letter in "abcde": # we can replace it with enumerate
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1


index_count = 0
word = "asdfads"
for letter in word:
    print(word[index_count]) # for every letter in a word we print index value location == printing the letter
    index_count += 1 # and in this case we need index count

# there is building enumerate function to replace it:
for item in enumerate(word):
    print(item) # it is doing index count in a form of tuples

for index, letter in enumerate(word):
    print(letter)
    print(index)
    print("\n")

# zip function zips together 2 lists, it is opposite of enumerate

mylist1 = [1,2,3,4,5]
mylist2 = ["a", "b", "c"]
for item in zip(mylist1,mylist2): # it will return tuples
    print(item)

mylist1 = [1,2,3,4,5]
mylist2 = ["a", "b", "c"]
mylist3 = [100,200,300,400]
for item in zip(mylist1,mylist2, mylist3): # it will return tuples and it will zip by shortest list
    print(item)

list(zip(mylist1, mylist2, mylist3)) # if we want to have a list

# in operator
# works for lists
print("x" in [1,2,3])
print("x" in ["x","y","z"])

# works for string
print("a" in "a world")

# work in dictinaries, for keys
print("key" in {"key": 345})
d = {"key": 345}
print(345 in d.values())
print(345 in d.keys())

# min, max
mylist = [1,3,5,78,9,0]
print(min(mylist))
print(max(mylist))

# random function, shuffle
from random import shuffle
mylist = [2,5,3,6,8,4]
shuffle(mylist) # not returning anything, in place function == change it permanently
print(mylist)
shuffle(mylist) # will reshuffle anytime
print(mylist)

from random import randint
randint(0,100) # will return random integer from 0 to 100
mynum = randint(0,100)
print(mynum)

#  input function
name = input("Enter a name here:") # input except everything as a string
result = "Her name is "+ name
print(result)

result = input("Your favorite number:")
print(type(result))
print(float(result))
print(int(result))


result = int(input("Your favorite number:"))




