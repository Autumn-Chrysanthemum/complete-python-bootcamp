# ordered sequence of objects (immutable)
# tuple are immutable, can't change them

t =(1,2,3)
mylist = [1,2,3]

print(type(t))
print(type(mylist))

print(len(t))

t = ("one", 2)
print(t[0])
print(t[-1])

t = ("a", "a", "b")
print(t.count("a"))
print(t.index("a")) # will return only first index. we can use FOR loop to get all indexes

mylist[0] = "NEW"
t[0] = "NEW" # will be error. Can't be reassign.

# we use tuples if we need to make sure that they don't accidentally get changed.

t = (2,3,4,5)