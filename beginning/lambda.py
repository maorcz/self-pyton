#list sorting by the second value in the tuples
a = [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key=lambda x: x[1])
print(a) 