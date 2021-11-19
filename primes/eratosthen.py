number = int(input())

NOT_ENCOUNTERED = 0
PRIME = 1
NOT_PRIME = 2

def get_primes(n):
    primes = [0] * (number + 1)

    # we go through every number from 2 to n
    # if we haven't encountered it yet, it's prime, therefore every multiply of that number isn't prime
    for prime in range(2, number + 1):
        if primes[prime] == NOT_ENCOUNTERED:
            primes[prime] = PRIME
            multiplied = prime * 2
            while multiplied <= number:
                primes[multiplied] = NOT_PRIME
                multiplied += prime
    
    return primes

primes = get_primes(number)

for i in range(2, number + 1):
    if primes[i] == PRIME:
        print(i)