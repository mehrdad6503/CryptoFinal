/**
* Project: Final Project - Digital Signature Standard
* Created By: Alex Cadigan, Jacob Scott, Skyler Norgaard
* Date Created: 3/11/2017
* 
* This code is based off of code from these links:
* http://www.java2s.com/Code/Java/Security/GenerateaDSAsignature.htm
* http://www.java2s.com/Code/Java/Security/SignatureSignAndVerify.htm
*/

// Imports:
import java.util.Scanner;

/**
* This class contains code to initiate a digital signature algorithm.  The user can choose to sign a document or verify an existing
* signature.
*/
public class DigitalSignatureStandard
{
	// Methods:

	/**
	* Contains the main method to run the program.
	*
	* @param 		args 		Not used in this program
	*/
	public static void main(String [] args)
	{
		System.out.println("\n--------------- Welcome to the Cadigan/Scott/Norgaard Digital Signature Program! ---------------\n");

		// Creates an object capable of reading in user data
		Scanner reader = new Scanner(System.in);

		// Determines if the user wants to sign a document or verify a signature
		System.out.println("\nEnter 'Sign' to sign a document, or 'Verify' to verify a signature:");
		String userPurpose = reader.nextLine();
		while (!userPurpose.equalsIgnoreCase("SIGN") && !userPurpose.equalsIgnoreCase("VERIFY"))
		{
			System.out.println("\nInvalid entry!  Enter 'Sign' to sign a document, or 'Verify' to verify a signature:");
			userPurpose = reader.nextLine();
		}

		// Checks to see if the user wants to sign a document or verify a signature
		if (userPurpose.equalsIgnoreCase("SIGN"))
		{
			// Signs a document
			SignDocument signature = new SignDocument();
			signature.signDocument();
		}
		else
		{
			// Verifies a signature
			VerifySignature verification = new VerifySignature();
			verification.verifySignature();
		}
	}
}