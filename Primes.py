import math

def simple_sieve(limit):
    """Sieve of Eratosthenes up to sqrt(n)"""
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
    return [p for p, is_prime in enumerate(prime) if is_prime]

def segmented_sieve(n):
    """Prints all primes up to n using segmented sieve"""
    limit = int(math.sqrt(n)) + 1
    primes = simple_sieve(limit)  # primes up to sqrt(n)

    low = limit
    high = 2 * limit

    # Print primes less than sqrt(n)
    for p in primes:
        print(p, end=' ')

    while low < n:
        if high > n:
            high = n + 1
        mark = [True] * (high - low)

        for p in primes:
            # Find the minimum number in [low, high) divisible by p
            start = max(p * p, ((low + p - 1) // p) * p)
            for j in range(start, high, p):
                mark[j - low] = False

        for i in range(low, high):
            if mark[i - low]:
                print(i, end=' ')

        low += limit
        high += limit

n = int(input("Enter a number: "))
segmented_sieve(n)
