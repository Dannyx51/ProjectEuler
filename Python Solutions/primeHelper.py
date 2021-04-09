# Holder class for useful prime functions
from math import gcd

class Prime:
    @staticmethod
    def relativePrime(n:int, tot = False) -> list:
        ret = 0
        if tot:
            for i in range(n):
                if gcd(i,n) == 1:
                    ret += 1
        else:
            ret = [i for i in range(n) if gcd(i,n) == 1]
        if n % 1000 == 0:print(n)
        return ret

    @staticmethod
    def genPrime(n:int) -> list: # Generates a boolean list where all true indices are prime
        prime = [True for i in range(n+1)] 
        p = 2
        while (p * p <= n):             
            # If prime[p] is not changed, then it is a prime 
            if (prime[p] == True): 
                # Update all multiples of p 
                for i in range(p * p, n+1, p): 
                    prime[i] = False
            p += 1
        return prime

    @staticmethod
    def isPrime(n:int) -> bool:
        if n <= 1: return False
        if n == 2: return True
        if not n % 2: return False
        if n < 9: return True
        if not n % 3: return False
        
        c = 5
        while c ** 2 <= n:
            if not n % c: return False
            if not n % (c + 2): return False
            c += 6
        
        return True

    @staticmethod
    def isPseudoPrime(n:int) -> bool:
        if n <= 1: return False 
        if n == 2: return True
        if not n % 2: return False
        if n < 9: return True
        if not n % 3: return False
        if not n % 5: return False

        arr = [2,3]
        return not any([Prime.__Witness(x,n) for x in arr])

    def __Witness(a:int, n:int) -> bool:
        t = 0
        u = n - 1
        while ((u & 1) == 0):
            t += 1
            u >>= 1

        xi1 = pow(a,u,n)
        xi2 = 0

        for i in range(t):
            xi2 = xi1 * xi1 % n
            if ((xi2 == 1) and (xi1 != 1) and (xi1 != (n - 1))): return True
            xi1 = xi2

        if xi1 != 1: return True
        return False