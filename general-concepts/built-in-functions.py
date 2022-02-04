# List of built in functions
####### sum()
# argument has to be an iterable
print(sum(set([1,2,3,4,5])))

####### divmod()
# returns set with integer div (a//b) and remainder
# One of the built-in functions of Python is divmod, 
# which takes two arguments  and  and returns a tuple 
# containing the quotient of  first and then the remainder .

# >>> print divmod(177,10)
# (17, 7)
print(divmod(177, 10))

####### pow() or a**b
# It's also possible to calculate a**b mod m (pow(a,b,m))
# modulo can't be negative
print(pow(17,10)) 
print(pow(17,10,3)) # returns remainder when divided by modulo

####### all()
# The all() function returns True if all items in an iterable 
# are true, otherwise it returns False.
print(all([True, False, True]))
print(all([True, True, True]))

####### eval()
# the eval() built in function will look at a string and replace variables in the 
# formula that instatiated as local objects
# also works for method objects and function objects
x = 5
y = 5
print(eval("x+y+1"))
eval("print('HELLO EVAL()!')")

######## reversed()
# great for reversing an iterable
# returns an iterator object
 
# returns reversed iterator object
print(str(reversed(str(9))))

# returns reversed items
print(*reversed(str(90001)))

# returns reversed string
print(''.join(reversed(str(90001))))


