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

	# Determines if the user wants to use authentic values, or provide their own values
	if (userChoice == "AUTHENTIC"):

		q = Helper.calculateQ()

		p = Helper.calculateP(q)


		#p = Helper.calculateP()
		q = Helper.calculateQ()

	else:

		# Gets 'p' from the user
		p = input("\nEnter your public value 'p':\t")
		while (not Helper.isPositiveNumber(p)):

			p = input("\nInvalid entry!  Please Enter your public value 'p':\t")