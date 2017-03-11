'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/10/2017
'''

# Imports:
import hashlib;

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
def calculateW(s, q):

	return calculateModularMultiplicativeInverse(int(s), int(q));

'''
Found this hash function from: https://docs.python.org/3.0/library/hashlib.html
'''
# Runs the Secure Hash Algorithm 1
def secureHashAlgorithm1(message):

	# Gets the SHA1 hash function
	hashFunction = hashlib.sha1(bin(int(message))[2:].encode("utf-8"));

	# Returns the hash value of the message
	return int(hashFunction.hexdigest(), 16);

# Calculates the value 'u1' used for verifying a signature
def calculateU1(hashValue, w, q):

	# Calculates the value 'u1'
	return (hashValue * w) % q;

# Calculates the value 'u2' used for verifying a signature
def calculateU2(r, w, q):

	# Calculates the value 'u2'
	return (r * w) % q;

# Calculates the value 'v' used for verifying a signature
def calculateV(g, u1, y, u2, p, q):

	# Calculates the value 'v'
	return (((g ** u1) * (y ** u2)) % p) % q;

# Initiates verification of a signature
def verifySignature():

	# Gets the received message from the user
	message = input("\nEnter the message you have received:\t");

	# Makes sure the user enters an appropriate message
	while (not isNumber(message)):

		message = input("\nInvalid entry!  Please enter the message you have received:\t");

	# Gets the 'r' value of the signature from the user
	r = input("\nEnter the signature's 'r' value:\t");

	# Makes sure the user enters an appropriate signature value
	while (not isNumber(r)):

		r = input("\nInvalid entry!  Please enter the signature's 'r' value:\t");

	# Gets the 's' value of the signature from the user
	s = input("\nEnter the signature's 's' value:\t");

	# Makes sure the user enters an appropriate signature value
	while (not isNumber(s)):

		s = input("\nInvalid entry!  Please enter the signature's 's' value:\t");

	# Gets the signer's public key
	y = input("\nEnter the signer's public key:\t");

	# Makes sure the user enters an appropriate signature value
	while (not isNumber(y)):

		y = input("\nInvalid entry!  Please enter the signer's public key:\t");

	# Gets the 'p' value of the signer's public key from the user
	p = input("\nEnter the 'p' value of the signer's public key:\t");

	# Makes sure the user enters an appropriate value for 'p'
	while (not isNumber(p)):

		p = input("\nInvalid entry!  Enter the 'p' value of the signer's public key:\t");

	# Gets the 'q' value of the signer's public key from the user
	q = input("\nEnter the 'q' value of the signer's public key:\t");

	# Makes sure the user enters an appropriate value for 'q'
	while (not isNumber(q)):

		q = input("\nInvalid entry!  Please enter the 'q' value of the signer's public key:\t");

	# Gets the 'g' value of the signer's public key from the user
	g = input("\nEnter the 'g' value of the signer's public key:\t");

	# Makes sure the user enters an appropriate value for 'g'
	while (not isNumber(g)):

		g = input("\nInvalid entry!  Please enter the 'g' value of the signer's public key:\t");

	# Calculates the value 'w'
	w = calculateW(int(s), int(q));

	# Calculates the value 'u1'
	u1 = calculateU1(secureHashAlgorithm1(int(message)), w, int(q));

	# Calculates the value 'u2'
	u2 = calculateU2(int(r), w, int(q));

	# Calculates the value 'v'
	v = calculateV(int(g), u1, int(y), u2, int(p), int(q));

	# Checks if the signature is valid
	if (v != r):

		print("\nError!  This signature is not valid.\n");

	print("\nSuccess!  This signature is valid!\n");

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