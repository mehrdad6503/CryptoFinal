'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/12/2017

Description: This file contains code to sign a document using the Digital Signature Standard algorithm.
'''

# Imports:

import Helper

# Initiates the algorithm to sign a document
def signDocument(userChoice):

	# Gets the message from the user
	message = input("\nEnter the message you want to sign:\t")

	# Determines if the user wants to use authentic values, or provide their own values
	if (userChoice == "AUTHENTIC"):

		# Generates valid 'p' and 'q' values
		p = Helper.calculateP()
		q = Helper.calculateQ(p)
		while (q == None):

			p = Helper.calculateP()
			q = Helper.calculateQ(p)

		# Generates the value 'g'
		g = Helper.calculateQ(p, q)

	else:

		# Gets 'p' from the user
		p = input("\nEnter your public value 'p':\t")
		while (not Helper.isPositiveNumber(p)):

			p = input("\nInvalid entry!  Please Enter your public value 'p':\t")

		# Gets 'q' from the user
		q = input("\nEnter your public key value 'q':\t")
		while (not Helper.isPositiveNumber(q)):

			q = input("\nInvalid entry!  Enter your public key value 'q':\t")

		# Gets 'g' from the user
		g = input("\nEnter your public key value 'g':\t")
		while (not Helper.isPositiveNumber(g)):

			g = input("\nInvalid entry!  Enter your public key value 'g':\t")

	# Generates the value 'x', the user's private key
	x = Helper.calculateX(int(q))

	# Generates the value 'y', the user's public key
	y = Helper.calculateY(int(p), int(g), x)

	print("\nYour public key is:\t" + str(y))

	# Generates the value 'k', the user's secret number
	k = Helper.calculateK(int(q))

	# Generates the value 'r'
	r = Helper.calculateR(int(p), int(q), int(g), k)

	# Calculates the value 's'
	kInverse = Helper.calculateModularMultiplicativeInverse(k, int(q))
	H = Helper.secureHashAlgorithm1(message)
	s = Helper.calculateS(int(q), x, r, kInverse, H)

	return r, s