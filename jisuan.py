#[356, 544, 1212, 1523, 1618, 2069, 2150, 2296, 2800, 3681, 4965]
# x = [2150, 2069, 1212, 2296, 2800, 544, 1618, 356, 1523, 4965, 3681]
#sstf[2150,2069,2296,2800,3681,4965,1618,1523,1212,544,356]
# y = sorted(x)
# print(y)   2069,1618,1523,1212,544,356,
a=[2150, 2296, 2800, 3681, 4965, 356, 544, 1212, 1523, 1618, 2069]
print(len(a))
##
b = 0
for i in range(len(a) - 1 ):
    c = a[i+1] - a[i]
    c = abs(c)
    b += c

print(b)

