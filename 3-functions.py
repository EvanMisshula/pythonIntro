def double(x):
    """ This is the docstring
    It can cover many lines."""
    return x*2

def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)

my_double = double
x = apply_to_one(my_double)
print x

# Anonymous functions

y = apply_to_one(lambda x: x + 4)


another_double = lambda x: 2 * x
def another_double(x):
    return 2*x

#default arguments
def my_print(message="my default message"):
    print message

my_print("hello")
my_print()

#named arguments

def subtract(a=0, b=0):
    return a - b

subtract(10,5)
subtract(0,5)
subtract(b=5)
