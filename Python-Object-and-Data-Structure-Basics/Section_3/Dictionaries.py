# Key-Value pairing that is unordered
# unordered mappings for storing objects
# no need to know an index location

# when we choose Dictionary and when we choose Lists???

# Dictionaries: Objects retrieved by key name
# Unordered and can not be sorted

# Lists: Objects retrieved by location.
# Ordered Sequences can be indexed and sliced.

my_dict = {"key1": "value1", "key2": "value2"}
print(my_dict)

print(my_dict["key1"])

prices_lookup = {"apples": 2.99, "orages": 4.88, "milk": 2.77}
print(prices_lookup["apples"])

d = {"k1": 123, "k2": [0,1,2], "k3": {"insidekey":100}}
print(d["k2"])
print(d["k3"]["insidekey"])
print(d["k2"][2])

d = {"key1": ["a", "b", "c"]}
print(d["key1"][2])
print(d["key1"][2].upper())

d = {"k1":100, "k2": 200}
d["k3"]=300
print(d)

d["k1"] = 'NEW VALUE'
print(d)

d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())

# assessment

d = {'simple_key':'hello'}
print(d["simple_key"])

d = {'k1':{'k2':'hello'}}
print(d["k1"]["k2"])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"][0]["nest_key"][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])