## Tuples
## Tuples are immutable. 
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3
print my_list


try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"

    ## Tuples are a convenient way to return multiple values from functions:
def sum_and_product(x, y):
    return (x + y),(x * y)

sp = sum_and_product(2, 3)
print sp

s, p = sum_and_product(5, 10) # s is 15, p is 50
print s
pring p

## multiple assignment:
x, y = 1, 2
print x, y
x, y = y, x
print x, y
