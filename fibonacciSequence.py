# @mauriciopanata - San Diego, CA - 01/19/2021
# Step 1 - Creating The Fibonacci Sequence Generator function.
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


# Step 2 - Insert here the max limit of the Fibonacci Sequence desired.
fib = fibonacci(200)
print(fib)
