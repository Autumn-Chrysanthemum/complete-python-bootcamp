# and - both conditions to be True
# or - one of the condition to be True
# not - return the opposite boolean of that you just did

print(1 < 2 < 3)
print(1 > 2 < 3)

print(1 < 2 and 2> 3)
print("h" == "h" and 2 == 2)

# some libraries required

print(1==1 or 2==2)
print(1==3 or 2==2)
print(1==3 or 5==2) # only if both false we get False

print(not (1 == 1)) # opposite boolean
print(not 1 == 1)
print(not 1 != 1)