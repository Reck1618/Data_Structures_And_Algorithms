"""
Write a Python program using Sieve of Eratosthenes method for 
computing primes upto a specified number.
"""

def sieve_prime(n):
    prime_set = set()
    ans = []

    if n < 2:
        return []

    for i in range(2, n+1):
        if i not in prime_set:
            ans.append(i)
        
        for j in range(i*i, n + 1, i):
            prime_set.add(j)
    
    return ans




def main():

    print(sieve_prime(1))
    print(sieve_prime(55))
    print(sieve_prime(100))

main()