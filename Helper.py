'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/12/2017

Description: This file contains all the code for a Digital Signature Standard algorithm.
'''

# Imports:

import random
import sympy

# Determines if a given value is an integer
def isPositiveNumber(number):

	# Attemps to convert the value into an integer
	try:

		if (int(number) > 0):

			return True

    # Catches the error if the value is not an integer	
	except ValueError:

		return False

# Generates the value 'q'
def calculateQ():

	# Generates a 'q'
	q = random.randint(2 ** 159, 2 ** 160)
	while (not sympy.isprime(q)):

		q = random.randint((2 ** 159) + 1, (2 ** 160) - 1)

# Generates the value 'p'
def calculateP():

	# Calculates the value 'L' used in 'p' generation
	L = random.randint(512, 1024)
	while ((L % 64) != 0):

		L = random.randint(512, 1024)

	# Generates the value 'p', which must be a prime number
	p = random.randint((2 ** (L - 1)) + 1, (2 ** L) - 1)
	while (not sympy.isprime(p)):

		p = random.randint((2 ** (L - 1)) + 1, (2 ** L) - 1)

	return p



	print(q)