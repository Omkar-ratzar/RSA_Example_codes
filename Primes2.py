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

def largest_two_primes(n):
    """Finds the two largest primes ≤ n using segmented sieve"""
    limit = int(math.sqrt(n)) + 1
    primes = simple_sieve(limit)

    largest = -1
    second_largest = -1

    # Check primes less than sqrt(n)
    for p in primes:
        if p > largest:
            second_largest = largest
            largest = p

    low = limit
    high = 2 * limit

    while low < n:
        if high > n:
            high = n + 1
        mark = [True] * (high - low)

        for p in primes:
            start = max(p * p, ((low + p - 1) // p) * p)
            for j in range(start, high, p):
                mark[j - low] = False

        for i in range(high - 1, low - 1, -1):  # reverse to find largest quickly
            if mark[i - low]:
                second_largest = largest
                largest = i
                break  # only need the largest in this segment

        low += limit
        high += limit

    print("The two largest primes ≤", n, "are:", second_largest, "and", largest)

# Example usage
n = int(input("Enter a number: "))
largest_two_primes(n)
