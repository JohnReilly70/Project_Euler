def prime_generator():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

def nth_prime(n):
    p = prime_generator()
    counter = 0
    for value in p:
        counter += 1
        if counter == n:
            print(value)
            break

nth_prime(10001)