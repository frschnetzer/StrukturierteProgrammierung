# 1.fülle eine liste mit n-2 Wahrheitswerten (boolean)
# 2.wähle Primzahl (schleife, bis keine primzahl mehr gibt)
# 3.markiere die vielfachen mit false (schleife)
# wiederhohlen
#bsp: 
# FFTTTTTTT...
# 012345678....

def main():
    def define_primes(n):
        sieve = [True] * (n + 1)  # Füllt die Liste mit True-Werten bis n+1
        sieve[0], sieve[1] = False, False 
        primes = []
        i = 2
        while i <= n: #initialize with the assumption we only have primes
            sieve.append(True)
            i += 1
            prime = 2
            while prime < n:
                multiplicator = 2
                while (prime * multiplicator) <= n: # prime * multiplicator gibt vielfache
                    primes.append(prime)
                    #problem: position existiert derzeit noch nicht
                    sieve[prime * multiplicator] = False # alle vielfachen von prime werden auf false gesetzt
                    multiplicator +=1
                    prime += 1
                while prime < n and sieve[prime] == False: #wähle nächste primzahl
                    prime +=1
        return primes


    print(define_primes(10))
main()
