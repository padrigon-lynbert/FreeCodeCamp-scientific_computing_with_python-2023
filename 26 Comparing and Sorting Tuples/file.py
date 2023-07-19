lst = []
counts = {"a":1, "b":2, "c":3}
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )