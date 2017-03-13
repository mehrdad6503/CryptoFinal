'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/12/2017

Description: This file contains code to verify a signature using a Digital Signature Standard Algorithm.
'''

# Imports:

import Helper

# Initiates the algorithm to verify a signature
def verifySignature():

	# Gets the signed message from the user
	message = input("\nEnter the signed message you have received:\t")

	# Gets the signer's public value 'p'
	p = input("\nEnter the signer's public value 'p':\t")
	while (not Helper.isPositiveNumber(p)):

		p = input("\nInvalid entry!  Enter the signer's public value 'p':\t")

	# Gets the signer's public value 'q'
	q = input("\nEnter the signer's public value 'q':\t")
	while (not Helper.isPositiveNumber(q)):

		q = input("\nInvalid entry!  Enter the signer's public value 'q':\t")

	# Gets the signer's public value 'g'
	g = input("\nEnter the signer's public value 'g':\t")
	while (not Helper.isPositiveNumber(g)):

		g = input("\nInvalid entry!  Enter the signer's public value 'g':\t")

	# Gets the signer's public key
	y = input("\nEnter the signer's public key 'y':\t")
	while (not Helper.isPositiveNumber(y)):

		y = input("\nInvalid entry!  Enter the signer's public key 'y':\t")

	# Gets the signed value 'r' from the user
	r = input("\nEnter the signature value 'r' you have received:\t")
	while (not Helper.isPositiveNumber(r)):

		r = input("\nInvalid entry!  Enter the signature value 'r' you have received:\t")

	# Gets the signed value 's' from the user
	s = input("\nEnter the signature value 's' you have received:\t")
	while (not Helper.isPositiveNumber(s)):

		s = input("\nInvalid entry!  Enter the signature value 's' you have received:\t")

	# Calculates the value 'w'
	sInverse = Helper.calculateModularMultiplicativeInverse(int(s), int(q))
	w = Helper.calculateW(int(q), sInverse)

	# Determines if the user wants to enter a hash value, or use their own
	decision = input("\nWould you like to enter your own hash value (enter 'Yes' or 'No')?\t").upper()
	while (decision != "YES" and decision != "NO"):

		decision = input("\nInvalid entry!  Would you like to enter your own hash value (enter 'Yes' or 'No')?\t").upper()
	
	# Gets the hash value
	if (decision == "YES"):

		H = input("\nEnter your own hash value:\t")
		while (not Helper.isPositiveNumber(H)):

			H = input("\nEntry invalid!  Enter your own hash value:\t")

		H = int(H)

	else:

		H = Helper.secureHashAlgorithm1(message)

	# Calculates the value 'u1'
	u1 = Helper.calculateU1(int(q), w, H)

	# Calculates the value 'u2'
	u2 = Helper.calculateU2(int(q), int(r), w)

	# Calculates the value 'v'
	v = Helper.calculateV(int(p), int(q), int(g), int(y), u1, u2)

	# Tests if the signature is valid
	if (v == int(r)):

		print("\nSuccess!  This signature is valid!")

	else:

		print("\nError!  This signature is not valid!")
