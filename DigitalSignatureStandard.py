'''
Project: Final Project - Digital Signature Standard
Created By: Skyler Norgaard, Jacob Scott, and Alex Cadigan
Date Created: 3/10/2017
'''

# Imports:
import random;
import hashlib;

# Determines if a given hexadecimal value is an integer
def isNumber(number):

	# Attemps to convert the value into an integer
    try:

    	int(number, 16);
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
	greatestCommonDivisor, coefficient1 = extendedEuclideanAlgorithm(number, modulo);

	# Checks if there is no modular multiplicative inverse for the given number and modulo
	if greatestCommonDivisor != 1:

		print("\nError!  This signature is not valid!\n");
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

# Creates the user's private key
def calculatePrivateKey(q):

    return random.randrange(1, q);

# Creates the user's secret number
def calculateSecretNumber(q):

    return random.randrange(1, q);

# Calculates the value 'r' used for signing a document
def calculateR(p, q, g, secretNumber):

    return ((g ** secretNumber) % p) % q;

# Calculates the value 's' used for signing a document
def calculateS(message, q, privateKey, secretNumber, r):

	return ((calculateModularMultiplicativeInverse(secretNumber, q) * secureHashAlgorithm1(message)) + (privateKey * r)) % q;

# Creates the user's secret number
def calculateSecretNumber(q):

    return random.randrange(1, q);

# Calculates the value 'w' used for verifying a signature
def calculateW(s, q):

	return calculateModularMultiplicativeInverse(s, q);

# Calculates the value 'u1' used for verifying a signature
def calculateU1(q, w, hashValue):

	return (hashValue * w) % q;

# Calculates the value 'u2' used for verifying a signature
def calculateU2(q, w, r):

	return (r * w) % q;

# Creates the signer's public key
def calculatePublicKey(p, g, privateKey):

    return (g ** privateKey) % p;

# Calculates the value 'v' used for verifying a signature
def calculateV(p, q, g, u1, u2, publicKey):

	return (((g ** u1) * (publicKey ** u2)) % p) % q;

# Initiates the signing of a document
def signDocument(message, p, q, g, privateKey):

	# Generates the user's secret number
	secretNumber = calculateSecretNumber(q);

	print("\nThe secret number is:\t" + str(secretNumber));

	# Generates the 'r' value of the signature
	r = calculateR(p, q, g, secretNumber);

	# Generates the 's' value of the signature
	s = calculateS(message, q, privateKey, secretNumber, r)

	print("\nYour signature is:\t(" + str(r) + ", " + str(s));

# Initiates the verification of a signature
def verifySignature(message, p, q, g, privateKey):

	# Calculates the signer's secret number
	secretNumber = calculateSecretNumber(q);

	# Calculates the signer's 'r' signature value
	r = calculateR(p, q, g, secretNumber)

	# Calculates the value 'w'
	w = calculateW(calculateS(message, q, privateKey, secretNumber, r), q);

	print("\nThe value of 'w' is:\t" + str(w));

	# Calculates the value 'u1'
	u1 = calculateU1(q, w, secureHashAlgorithm1(message));

	print("\nThe value of 'u1' is:\t" + str(u1));

	# Calculates the value 'u2'
	u2 = calculateU2(q, w, r);

	print("\nThe value of 'u2' is:\t" + str(u2));

	# Generates the signer's public key
	publicKey = calculatePublicKey(p, g, privateKey);

	print("\nThe public key is:\t" + str(publicKey));

	# Generates the value 'v'
	v = calculateV(p, q, g, u1, u2, publicKey);

	# Verifies the signature
	if (v != r):

		print("\nError!  This signature is not valid!");

	else:

		print("\nSuccess!  This signature is valid!");

# Initiates the program
def beginProgram():

	# Defines the 'p', 'q', and 'g' values to use for signing and verification
	p = int("E0A67598CD1B763BC98C8ABB333E5DDA0CD3AA0E5E1FB5BA8A7B4EABC10BA338FAE06DD4B90FDA70D7CF0CB0C638BE3341BEC0AF8A7330A3307DED2299A0EE606DF035177A239C34A912C202AA5F83B9C4A7CF0235B5316BFC6EFB9A248411258B30B839AF172440F32563056CB67A861158DDD90E6A894C72A5BBEF9E286C6B" ,16);
	q = int("E950511EAB424B9A19A2AEB4E159B7844C589C4F",16);
	g = int("D29D5121B0423C2769AB21843E5A3240FF19CACC792264E3BB6BE4F78EDD1B15C4DFF7F1D905431F0AB16790E1F773B5CE01C804E509066A9919F5195F4ABC58189FD9FF987389CB5BEDF21B4DAB4F8B76A055FFE2770988FE2EC2DE11AD92219F0B351869AC24DA3D7BA87011A701CE8EE7BFE49486ED4527B7186CA4610A75",16);

	# Creates the private key, which is used for both signing and verifying
	privateKey = calculatePrivateKey(q);

	# Asks the user if they want to sign or verify a document
	purpose = input("\nEnter 'Sign' to sign a document, or 'Verify' to verify a signature:\t").upper();

	# Makes sure the user enters an appropriate value
	while (purpose != "SIGN" and purpose != "VERIFY"):

		purpose = input("\nInvalid entry!  Please enter 'Verify' to verify a signature, or 'Sign' to sign a document:\t").upper();

	# Checks if the user wants to verify or sign a document
	if (purpose == "SIGN"):

		# Asks the user to input the message
		message = input("\nPlease enter the message to sign:\t");

		# Makes sure the user enters an appropriate message
		while (not isNumber(message)):

			message = input("\nInvalid entry!  Please enter the message to sign:\t");

		print("\nThe private key is:\t" + str(privateKey));

		signDocument(message, p, q, g, privateKey);

	else:

		# Asks the user to input the message
		message = input("\nPlease enter the signed message:\t");

		# Makes sure the user enters an appropriate message
		while (not isNumber(message)):

			message = input("\nInvalid entry!  Please enter the signed message:\t");

		print("\nThe private key is:\t" + str(privateKey));

		verifySignature(message, p, q, g, privateKey);

beginProgram();
print();