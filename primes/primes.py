# very unoptimized implementation, calculates every division every time if_prime is executed
def is_prime(n):
    # we try every number from 2 to sqrt(n) and see if our target number n is divisible by that i
    # if yes, n isn't prime
    # otherwise, if n is divisible by none of this numbers, n is prime
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

number = int(input())

for i in range(2, number + 1):
    print(i, is_prime(i))