#FOR n > 10⁸ → Miller–Rabin (or segmented sieve if you need all primes).

import random
def is_prime(n):
    if n < 2:
        return False
    # small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    # write n-1 as d * 2^s
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Deterministic bases for 64-bit integers
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def largest_two_primes_below(n):
    """Finds the two largest primes <= n"""
    primes = []
    candidate = n if n % 2 == 1 else n - 1  # start from odd

    while len(primes) < 2 and candidate >= 2:
        if is_prime(candidate):
            primes.append(candidate)
        candidate -= 2  # skip even numbers

    return primes[::-1]  # return in ascending order

# Example usage
n = int(input("Enter your number to find the "))
print("Two largest primes ≤", n, "are:", largest_two_primes_below(n))
