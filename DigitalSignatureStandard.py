'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/12/2017

Description: This file contains code to begin a simulation of the digital signature standard algorithm.  Users may choose to sign a document
or verify a signature.
'''

# Imports:

import SignDocument
import VerifySignature

# Initiates the program.  From here, users can choose to sign a document or verify a signature.
def beginProgram():

	print("\n--------------- Welcome to the Cadigan/Scott/Norgaards Digital Signature Program! ---------------")

	# The user decides if they want to run the program using realistic sized numbers, or sample numbers
	userChoice = input("\nEnter 'Authentic' to run this program using numerical values in the correct range of values being currently used in" +
					   " practice, and 'Realistic' to run this program using sample values that are not in the correct range of values being" + 
					   " currently used in practice:\t").upper()
	while (userChoice != "AUTHENTIC" and userChoice != "REALISTIC"):

		userChoice = input("\nError! Enter 'Authentic' to run this program using numerical values in the correct range of values being currently" + 
						   " used in practice, and 'Realistic' to run this program using sample values that are not in the correct range of" + 
						   " values being currently used in practice:\t").upper()

	# The user chooses to sign a document or verify a signature
	purpose = input("\nEnter 'Sign' to sign a document, or 'Verify' to verify a signature:\t").upper()
	while (purpose != "SIGN" and purpose != "VERIFY"):

		purpose = input("\nInvalid entry!  Please enter 'Verify' to verify a signature, or 'Sign' to sign a document:\t").upper()

	# Determines which choice the user made and begins the appropriate simulation
	if (purpose == "SIGN"):

		r, s = SignDocument.signDocument(userChoice)

		print("\nYour signature is:\t(" + str(r) + ", " + str(s) + ")")

	else:

		VerifySignature.verifySignature()

beginProgram()
print("\n--------------- End of program! ---------------\n")