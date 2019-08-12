# ordered sequence of objects(mutable)
# we can slice, index, and it is mutable (can affect elements inside)

my_list = [1,2,3]
my_list = ["srting", 100, 23.4]
len(my_list)

mylist = ["one", "two", "three"]
mylist[0]

mylist[1:]

another_list = ["four", "five"]

mylist + another_list # not saving that, have to assign
new_list = mylist + another_list
print(new_list)

new_list[0] = "ONE ALL CAPS"
print(new_list)

new_list.append("six") # affecting in place, will modify list

print(new_list)

new_list.pop() # from the end of the list with position -1
print(new_list)

print(new_list.pop()) # and return it
print(new_list)

popped_item = new_list.pop() # we can save popped item
print(popped_item)


new_list.pop(0) # can remove particular element
print(new_list)

new_list =  ["a", "e", "x", "b", "c"]
num_list = [4,1,8,3]

new_list.sort() # in place method, does not return anything, just sort permanently
print(new_list)

my_sorted_list = new_list.sort() # INCORRECT WAY TO DO IT!!!!
type(my_sorted_list) # NoneType
print(my_sorted_list)

new_list.sort()
my_sorted_list = new_list # correct way to do it
print(my_sorted_list)

num_list.reverse()  # in place method, does not return anything, just sort permanently
print(num_list)

# assessment

list1 = [0]*3
print(list1)
list2 = [0,0,0]
print(list2)
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)


list4 = [5,3,4,6,1]
list4.sort()
print(list4)

print(sorted([5,3,4,6,1])) # in place
