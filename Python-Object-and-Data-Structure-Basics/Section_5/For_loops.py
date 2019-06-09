my_itarable = [1,2,3,4]
for item in my_itarable:
    print(item)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
    print("hello")

for num in mylist:
    if num%2 == 0:
        print(num)
    else:
        print((f'Odd number: {num}'))


mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum) # if print here I get back running tally of this sum

print(list_sum) # if we only want to see the sum print outside the loop

mystring = "Hello world"
for letter in mystring:
    print(letter)

for letter in "Hello world":
    print(letter)

for _ in "Hello world": # if you want to iterate certain amount of times.
    print("Cool")

tup = (1,2,3)
for item in tup:
    print(item)

# tuple unpacking
mylist = [(1,2), (3,4), (5,6), (7,8)]
print(len(mylist))
for item in mylist:
    print(item)

for (a,b) in mylist: # tuple unpacking when you duplicate the structure of the items
    print(a) # we have access to individual items
    print(b)


for a,b in mylist: # can be done without parentheses
    print(a)
    print(b)

mylist = [(1,2,3), (4,5,6), (7,8,9)]
for item in mylist:
    print(item)

for a,b,c in mylist:
    print(a)
    print(b) # we can just print middle numbers
    print(c)

my_dic = {"k1":1, "k2": 2, "k3": 3}
for item in my_dic: # by default we iterated through the keys
    print(item)

for item in my_dic.items(): # if you want to iterated through the items
    print(item)

# for key, value in my_dic: # we can use tuple unpacking method
for key, value in my_dic.items(): # we can use tuple unpacking method
    print(key)
    print(value)
    print(key,value)

for value in my_dic.values(): # if we need only values
    print(value)

# dictonary unordered 