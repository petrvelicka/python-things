# naive implementation, crashes for n >= 999
# uses explicit recursion, good for understanding how factorial is defined
def naive_factorial(n):
    if n < 2:
        return 1
    return n * naive_factorial(n - 1)

# better implementation, doesn't use explicit recursion
def better_factorial(n):
    if n < 1:
        return 1
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product

number = int(input())

print(better_factorial(number))