# A lambda_map_filter_reduce function is a small anonymous function.
# A lambda_map_filter_reduce function can take any number of arguments, but can only have one expression.
# The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.


#regular function

def double(x):
    return x*2


# same thing can be achieved using lambda_map_filter_reduce function
val = lambda x: 2 * x
add = lambda x, y: x+y
max = lambda x, y: x if x> y else y


print(val(3))
print(add(3, 7))
print(max(1000, 90000))

