'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/12/2017

Description: This file contains all the code for a Digital Signature Standard algorithm.
'''

# Imports:

import random
import hashlib
import sympy
import gmpy2

# Determines if a given value is an integer
def isPositiveNumber(number):

	# Attemps to convert the value into an integer
	try:

		if (int(number) > 0):

			return True

    # Catches the error if the value is not an integer	
	except ValueError:

		return False

'''
Algorithm from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
'''
# Runs the extended euclidean algorithm given two numbers
def extendedEuclideanAlgorithm(number1, number2):

	# Determines the coefficients and gcd for the given two numbers
	temporaryValue1, temporaryValue2, temporaryValue3, temporaryValue4 = 1, 0, 0, 1;
	while (number2 != 0):

		number3, number1, number2 = number1 // number2, number2, number1 % number2;
		temporaryValue1, temporaryValue2 = temporaryValue2, temporaryValue1 - number3 * temporaryValue2;
		temporaryValue3, temporaryValue4 = temporaryValue4, temporaryValue3 - number3 * temporaryValue4;

	return  number1, temporaryValue1;

'''
Algorithm from: http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
'''
# Computes the modular multiplicative inverse for the given number and modulo
def calculateModularMultiplicativeInverse(number, modulo):

	# Uses the extended euclidean algorithm to get the starting values
	greatestCommonDivisor, coefficient1 = extendedEuclideanAlgorithm(number, modulo);

	# Checks if there is no modular multiplicative inverse for the given number and modulo
	if greatestCommonDivisor != 1:

		print("\nError!  This signature is not valid!\n");
		print("\n--------------- End of program! ---------------\n")
		exit();

	else:

		# Calculates the modular multiplicative inverse
		return coefficient1 % modulo;

'''
Found this hash function from: https://docs.python.org/3.0/library/hashlib.html
'''
# Runs the Secure Hash Algorithm 1
def secureHashAlgorithm1(message):

	# Gets the SHA1 hash function
	hashFunction = hashlib.sha1(message.encode("utf-8"));

	# Returns the hash value of the message
	return int(hashFunction.hexdigest(), 16);

# Generates the value 'p'
def calculateP():

	# Calculates the value 'L' used in 'p' generation
	L = random.randint(512, 1024)
	while ((L % 64) != 0):

		L = random.randint(512, 1024)

	# Calculates the value 'p'
	p = random.randint((2 ** (L - 1)) + 1, (2 ** L) - 1)
	while (not sympy.isprime(p)):

		p = random.randint((2 ** (L - 1)) + 1, (2 ** L) - 1)

	return p

# Generates the value 'q'
def calculateQ(p):

	# Generates a 'q'
	counter = 0
	q = random.randint((2 ** 159) + 1, (2 ** 160) - 1)
	while (not sympy.isprime(q) or (p - 1) % q != 0):

		q = random.randint((2 ** 159) + 1, (2 ** 160) - 1)
		counter = counter + 1
		if (counter == ((2 ** 160) - 1) - ((2 ** 159) + 1)):

			return None

	return q

# Generates the value 'g'
def calculateG(p, q):

	# Generates the value 'g'
	h = random.randint(2, (p - 1) - 1)
	g = gmpy2.powmod(h, (p - 1) / q, p)

	while (g <= 1):

		h = random.randint(2, (p - 1) - 1)
		g = gmpy2.powmod(h, (p - 1) / q, p)

	return g

# Creates the user's private key
def calculateX(q):

    return random.randint(1, q - 1);

# Creates the signer's public key
def calculateY(p, g, x):

    return gmpy2.powmod(g, x, p)

# Creates the user's secret number
def calculateK(q):

    return random.randint(1, q - 1)

# Calculates the value 'r' used for signing a document
def calculateR(p, q, g, k):

    return gmpy2.powmod(g, k, p) % q

# Calculates the value 's' used for signing a document
def calculateS(q, x, r, kInverse, H):

	return ((kInverse * H) + (x * r)) % q

# Calculates the value 'w' used for verifying a signature
def calculateW(q, sInverse):

	return sInverse % q

# Calculates the value 'u1' used for verifying a signature
def calculateU1(q, w, H):

	return (H * w) % q;

# Calculates the value 'u2' used for verifying a signature
def calculateU2(q, r, w):

	return (r * w) % q;

# Calculates the value 'v' used for verifying a signature
def calculateV(p, q, g, y, u1, u2):

	return ((gmpy2.powmod(g, u1, p) * gmpy2.powmod(y, u2, p)) % p) % q