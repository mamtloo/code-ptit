import sys


def eratosthenes(n):

    if n < 2:
        return []
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False

    so_nguyen_to = [str(i) for i in range(n) if primes[i]]
    
    return sys.stdout.write('\n'.join(so_nguyen_to) + '\n')

input_data = sys.stdin.read().split()
n = int(input_data[0])
eratosthenes(n)