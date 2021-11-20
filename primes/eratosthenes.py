number = int(input())

# useful constants, which we will use to avoid hard-coding states for primes
NOT_ENCOUNTERED = 0
PRIME = 1
NOT_PRIME = 2

def get_primes(n):
    primes = [0] * (number + 1) # one element for every number from 0 to n 
    # we're not going to use the first two elements, but for the sake of simplicity, as to not to deal with changing indices, two additional bytes
    # isn't a big price to pay

    # we go through every number from 2 to n
    # if we haven't encountered it yet, it's prime, therefore every multiply of that number isn't prime
    for prime in range(2, number + 1):
        if primes[prime] == NOT_ENCOUNTERED:
            primes[prime] = PRIME
            multiplied = prime * 2 # we skip prime * 1 and start directly with prime * 2
            while multiplied <= number:
                primes[multiplied] = NOT_PRIME
                multiplied += prime
    
    return primes

primes = get_primes(number)

for i in range(2, number + 1):
    if primes[i] == PRIME:
        print(i)