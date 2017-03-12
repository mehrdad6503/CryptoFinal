/**
* Project: Final Project - Digital Signature Standard
* Created By: Alex Cadigan, Jacob Scott, Skyler Norgaard
* Date Created: 3/11/2017
*
* This code is based off of code from these links:
* http://www.java2s.com/Code/Java/Security/SignatureSignAndVerify.htm
* http://www.java2s.com/Code/Java/Security/KeyPairGeneratorForPublicKey.htm
*/

// Imports:

import java.util.Scanner;

import java.io.File;

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.PrivateKey;
import java.security.Signature;
import java.security.PublicKey;

/**
* This class contains code to verify a signature using the Digital Signature Standard algorithm.
*/
public class VerifySignature
{
	// Methods:

	/**
	* Runs the Digital Signature Standard algorithm to verify a signature.
	*/
	public void verifySignature()
	{
		// Trys to verify a signature
		try
		{
			// Gets the name of the file to use as the signature message
			Scanner reader = new Scanner(System.in);
			System.out.println("\nEnter the name of the file you wish to verify, including the file extension:");
			String fileName = reader.nextLine();

			// Reads in the data from the signature file
			Scanner fileReader = new Scanner(new File(fileName));
			String rawData = "";
			while (fileReader.hasNext())
			{
				rawData += fileReader.next();
			}

			// Converts the data to bytes
			byte [] data = new byte [rawData.length()];
			for (int index = 0; index < rawData.length(); index ++)
			{
				data[index] = Byte.parseByte(rawData.substring(index, index + 1));
			}

			// Creates an object to generate the keys
			KeyPair keyGenerator = generateKeyPair(999);

			// Generates the signature
			byte[] signature = signData(data, keyGenerator.getPrivate());

			boolean verified;

			// Verifies the signature
			verified = verifySignature(data, keyGenerator.getPublic(), signature);

			if (verified == true)
			{
				System.out.println("\nSuccess!  This signature is verified!");
			}
			else
			{
				System.out.println("\nError!  This signature is not valid!");
			}
		}
		// Catches any errors that are thrown
		catch (Exception exception)
		{
			System.err.println("\nError!  Error exception:\t" + exception.toString());
		}
	}

	/**
	* Creates and initializes a key generation object that can be used to generate the private and public key.
	*
	* @param 		seed 			The value used to initialize the key generator
	*
	* @return 		KeyPair 		The key generator
	*
	* @throws 		Exception 		
	*/
	public KeyPair generateKeyPair(long seed) throws Exception
	{
		// Creates a key generation object
		KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("DSA");

		// Creates an object that can generate random numbers
		SecureRandom random = SecureRandom.getInstance("SHA1PRNG", "SUN");

		// Initializes the random generator
		random.setSeed(seed);

		// Initializes the key generation object
		keyGenerator.initialize(1024, random);

		// Returns the key generation object
		return keyGenerator.generateKeyPair();
	}

	/**
	* Signs the given data using the given private keys.
	*
	* @param 		data 			The data to sign
	* @param 		privateKey 		The private key to use
	*
	* @return 		byte [] 		The signed data
	*
	* @throws 		Exception
	*/
	public byte [] signData(byte [] data, PrivateKey privateKey) throws Exception
	{
		// Signs the data using the private key
		Signature signature = Signature.getInstance("SHA1withDSA");
		signature.initSign(privateKey);
		signature.update(data);
		return signature.sign();
	}

	/**
	* Verifies the given signature.
	*
	* @param 		data 			The data to use
	* @param 		publicKey 		The public key
	* @param 		signature 		The signature
	*
	* @return 		boolean 		The result of the signature comparison
	*
	* @throws 		Exception
	*/
	public boolean verifySignature(byte [] data, PublicKey publicKey, byte [] userSignature) throws Exception
	{
		// Verifies the signature
		Signature signature = Signature.getInstance("SHA1withDSA");
		signature.initVerify(publicKey);
		signature.update(data);
		return signature.verify(userSignature);
	}
}