# Sets are unordered collections of unique elements

myset = set()

myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2)
print(myset)

# usually we don't add like that we are casting a list to a set that have only unique values

mylist = [1,1,1,1,2,2,2,2,3,3,4,5]

# sets don't have an order
myset = set(mylist)
print(myset)


# assessment

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))