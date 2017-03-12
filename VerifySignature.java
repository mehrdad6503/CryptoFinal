/**
* Project: Final Project - Digital Signature Standard
* Created By: Alex Cadigan, Jacob Scott, Skyler Norgaard
* Date Created: 3/11/2017
*/

// Imports:

import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.Security;
import java.security.Signature;

/**
* This class contains code to verify a signature using the Digital Signature Standard algorithm.
*/
public class VerifySignature
{

	/**
	* Runs the Digital Signature Standard algorithm to verify a signature.
	*/
	public void verifySignature()
	{
		Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
	}
	

// 	import java.security.KeyPair;
// import java.security.KeyPairGenerator;
// import java.security.PrivateKey;
// import java.security.PublicKey;
// import java.security.SecureRandom;
// import java.security.Security;
// import java.security.Signature;

// public class MainClass {
//   public static void main(String args[]) throws Exception {
//     Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());

//     KeyPair keyPair = generateKeyPair(999);

//     byte[] data = { 65, 66, 67, 68, 69, 70, 71, 72, 73, 74 };
//     byte[] digitalSignature = signData(data, keyPair.getPrivate());

//     boolean verified;

//     verified = verifySig(data, keyPair.getPublic(), digitalSignature);
//     System.out.println(verified) ;

//     keyPair = generateKeyPair(888);
//     verified = verifySig(data, keyPair.getPublic(), digitalSignature);
//     System.out.println(verified);

//   }

//   public static byte[] signData(byte[] data, PrivateKey key) throws Exception {
//     Signature signer = Signature.getInstance("SHA1withDSA");
//     signer.initSign(key);
//     signer.update(data);
//     return (signer.sign());
//   }

//   public static boolean verifySig(byte[] data, PublicKey key, byte[] sig) throws Exception {
//     Signature signer = Signature.getInstance("SHA1withDSA");
//     signer.initVerify(key);
//     signer.update(data);
//     return (signer.verify(sig));

//   }

//   public static KeyPair generateKeyPair(long seed) throws Exception {
//     Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
//     KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("DSA");
//     SecureRandom rng = SecureRandom.getInstance("SHA1PRNG", "SUN");
//     rng.setSeed(seed);
//     keyGenerator.initialize(1024, rng);

//     return (keyGenerator.generateKeyPair());
//   }
	//}
}