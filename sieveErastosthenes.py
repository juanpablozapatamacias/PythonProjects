# Python program to print all smaller than or equal to n using Sieve of Eratosthenes

from os import system, name
from time import sleep

def clear():
    
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    
    #_ = call('clear' if os.name == 'posix' else 'cls')

def SieveOfErastothenes(n):
    # create a boolean array "prime[0..n" and initialize all entries it as true

    prime = [True for i in range (n+1)]
    p = 2
    while(p*p <= n):
        if prime[p] is True:
            for i in range(p*2, n+1, p):
                prime[i] = False

        p += 1

    prime[0]=False
    prime[1]=False

    # print all prime numbers
    for p in range(n+1):
        if prime[p]:
            print (p)

# main
if __name__ == '__main__':
    clear()
    sleep(2)
    n = 50
    print ("Following are the prime numbers smaller")
    print ("Than or equal to " + str(n))
    SieveOfErastothenes(n)
