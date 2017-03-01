#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:41:52 2017

@author: Skyler Norgaard and Jacob Scott... not Cadigan
"""

import random
import sympy


#these three methods are used to generate the Global Public Key Components

#generating random numbers that fit the condition
#will want to tell user what i values are value in our interface
#i must be between 0 and 8!
def pgen(i):
    #make sure that the user generated L value is <=1024
    if(512+64*i<=1024):
        L = 512+64*i #generate L value to use for bounds
        a=2**(L-1) #generate lower bound
        b=2**L #upper bound

        #generates number in range 2^(L-1)<2^(L)
        p = random.randrange(a+1,b,1)
        #check if p is prime, if not continue generating until it is
        while not sympy.isprime(p):
            p = random.randrange(a+1,b,1)
        return p
        
    else:
        print("Enter valid i value!")
        
#I dont think it's the logic, I think it's that
#the q being a prime divisor condition is never met. Or it just takes
#way too long to generate...
def qgen(p):
    #make sure prime is entered
    if(sympy.isprime(p)):
        #generate random q such that 2^159<q<2^160
        q = random.randrange((2**159)+1,2**160,1)
        #Cant get division condition to be true!!!!
        while not sympy.isprime(q):
            q = random.randrange((2**159)+1,2**160,1)
        return q
    else:
        print("p is not prime!")
        
def ggen(p,q):
    h = random.randrange(2,p-1)
    while not (h**((p-1)/q))%p > 1:
        h = random.randrange(2,p-1)
    g = (h**((p-1)/q))%p
    return g
          

#these methods are used to generate the public and private key
def privatekey(q):
    return random.randrange(1,q)
    
def publickey(g,x,p):
    return (g**x)%p
        
p = pgen(8)        
print(qgen(p))

#print("Should say true " + str(((p-1)%q)==0))
#print("Shouls say true " + str(sympy.isprime(q)))
           