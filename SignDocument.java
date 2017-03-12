/**
* Project: Final Project - Digital Signature Standard
* Created By: Alex Cadigan, Jacob Scott, Skyler Norgaard
* Date Created: 3/11/2017
*/

// Imports:

import java.util.Scanner;

import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.io.PrintWriter;

import java.nio.ByteBuffer;

import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.KeyPair;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.Signature;

/**
* This class contains code to sign a document using the Digital Signature Standard algorithm.
*/
public class SignDocument
{
	// Methods:

	/**
	* Runs the Digital Signature Standard algorithm to sign a document.
	*/
	public void signDocument()
	{
		// Trys to generate a signature
		try
		{
			// Creates an object that can help generate the public and private key
			KeyPairGenerator keyGeneratorGenerator = KeyPairGenerator.getInstance("DSA", "SUN");

			// Creates an object that can generate random numbers
			SecureRandom random = SecureRandom.getInstance("SHA1PRNG", "SUN");

			// Initializes the key generator
			keyGeneratorGenerator.initialize(1024, random);

			// Creates an object that can generate the public and private key
			KeyPair keyGenerator = keyGeneratorGenerator.generateKeyPair();

			// Generates the private key
			PrivateKey privateKey = keyGenerator.getPrivate();

			// Generates the public key
			PublicKey publicKey = keyGenerator.getPublic();

			// Generates the signature
			Signature signature = Signature.getInstance("SHA1withDSA", "SUN");
			signature.initSign(privateKey);

			// Creates an object that can read using input
			Scanner reader = new Scanner(System.in);

			// Gets the name of the file that the user wants to use as data to sign
			System.out.println("\nEnter the name of the file you wish to sign, including the file extension:");
			String filename = reader.nextLine();

			// Creates objects to read in data from a file
			FileInputStream fileInput = new FileInputStream(filename);
			BufferedInputStream bufferedReader = new BufferedInputStream(fileInput);

			// Creates an array to hold the message to sign
			byte [] data = new byte [1024];

			// Stores the raw data to sign
			int rawData;

			// Runs through the file and stores the data
			while (bufferedReader.available() != 0)
			{
				rawData = bufferedReader.read(data);

				// Passes the data to the signature object
				signature.update(data, 0, rawData);
			}

			bufferedReader.close();

			// Gets the signed data
			byte[] rawSignedData = signature.sign();

			// Create a byte buffer and wrap the array
			ByteBuffer byteBuffer = ByteBuffer.wrap(rawSignedData);

			// Writes the data to a text file
			PrintWriter writer = new PrintWriter("TestResults.txt", "UTF-8");
			writer.println(byteBuffer.getInt());
    		writer.close();
		}
		// Catches any errors that are thrown
		catch (Exception exception)
		{
			System.err.println("\nError!  Error exception:\t" + exception.toString());
		}
	}
}