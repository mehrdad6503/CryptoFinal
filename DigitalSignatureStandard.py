'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/10/2017
'''

# Determines if a given value is an integer
def isNumber(s):

	# Attemps to convert the value into an integer
    try:

    	int(s);
    	return True;

    # Catches the error if the value is not an integer	
    except ValueError:

        return False;

'''
Algorithm from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
'''
# Runs the extended euclidean algorithm given two numbers
def extendedEuclideanAlgorithm(number1, number2):

	# Creates variables to be used in the calculations
	temporaryValue1, temporaryValue2, temporaryValue3, temporaryValue4 = 1, 0, 0, 1;

	# Runs until number2 has been reduced to 0
	while (number2 != 0):

		# Updates the greatest common divisor values
		number3, number1, number2 = number1 // number2, number2, number1 % number2;

		# Updates the coefficient values
		temporaryValue1, temporaryValue2 = temporaryValue2, temporaryValue1 - number3 * temporaryValue2;
		temporaryValue3, temporaryValue4 = temporaryValue4, temporaryValue3 - number3 * temporaryValue4;

	# Returns the greates common divisor, and the two coefficients
	return  number1, temporaryValue1;

'''
Algorithm from: http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
'''
# Computes the modular multiplicative inverse for the given number and modulo
def calculateModularMultiplicativeInverse(number, modulo):

	# Uses the extended euclidean algorithm to get the starting values
	greatestCommonDivisor, coefficient1 = extendedEuclideanAlgorithm(number, modulo)

	# Checks if there is no modular multiplicative inverse for the given number and modulo
	if greatestCommonDivisor != 1:

		print("\nError!  This signature is not valid!\n");
		exit();

	else:

		# Calculates the modular multiplicative inverse
		return coefficient1 % modulo

# Calculates the value 'w' used for verifying a signature
def calculateW():

	# Gets the signature that the user is trying to verify
	s = input("\nEnter the signature you have received:\t");

	# Makes sure the user enters an appropriate signature value
	while (not isNumber(s)):
		
		# Prompts the user for another input
		s = input("\nInvalid entry!  Please enter the signature you have received:\t");

	# Gets the prime divisor 'q' used to generate the public key
	q = input("\nEnter the 'q' value for the signature:\t");

	# Makes sure the user enters an appropriate signature value
	while (not isNumber(q)):

		# Prompts the user for another input
		q = input("\nInvalid entry!  Please enter the 'q' value for the signature:\t");

	return calculateModularMultiplicativeInverse(int(s), int(q));

# Initiates verification of a signature
def verifySignature():

	# Calculates the value 'w'
	w = calculateW();

# Initiates the program
def beginProgram():

	# Asks the user if they want to sign or verify a document
	purpose = input("\nEnter 'Verify' to verify a signature, or 'Sign' to sign a document:\t").upper();

	# Makes sure the user enters an appropriate value
	while (purpose != "VERIFY" and purpose != "SIGN"):

		# Prompts the user for another input
		purpose = input("\nInvalid entry!  Please enter 'Verify' to verify a signature, or 'Sign' to sign a document:\t").upper();

	# Checks if the user wants to verify or sign a document
	if (purpose == "VERIFY"):

		# Begins verifying the signature
		verifySignature();

beginProgram();

print();