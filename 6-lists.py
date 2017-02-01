integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogeneous_list, [] ]
list_length = len(integer_list)

# equals 3
list_sum = sum(integer_list)
 # equals 6

 ## You can get or set the nth element of a list with square brackets:
x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]
x[0] = -1

## You can also use square brackets to “slice” lists:
first_three = x[:3]
print first_three

three_to_end = x[3:]
print three_to_end

one_to_four = x[1:5]
print one_to_four

last_three = x[-3:]
print last_three

without_first_and_last = x[1:-1]
print without_first_and_last

copy_of_x = x[:]
print copy_of_x

## Python has an in operator to check for list membership:

print(1 in [1, 2, 3])
print 0 in [1, 2, 3]


x = [1, 2, 3]
print x
print x.extend([4, 5, 6])
 
## If you don’t want to modify x you can use list addition:
x = [1, 2, 3]
y = x + [4, 5, 6]

print x
print y

## More frequently we will append to lists one item at a time:
x = [1, 2, 3]
print x.append(0)
 
y = x[-1]
print y


z = len(x)
print z
## unpacking
x, y = [1, 2]
print x
print y
## projection
_, y = [1, 7]
print y

