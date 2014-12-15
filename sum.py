def sum(x,y):
    while (y != 0):
       carry = x & y
       x = x ^ y
       y = carry << 1
    return x

m = sum(2,3)
print m

