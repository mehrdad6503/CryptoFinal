Project: Cryptography Final Project - Digital Signature Standard
Created By: Alex Cadigan, Jacob Scott, Skyler Norgaard
Date Created: 3/13/2017

Program Functionality:

While this program should theoretically work, we have found it does not produce correct answers when very large numbers are used.  However, this program has been confirmed to verify a signature properly when we used the information from question 5 of our take home final.  Here are the values used for that calculation:
Message: Pick me up at 7
P = 9337
Q = 389
G = 8854
Y = 7743
R = 113
S = 163
Hash Value = 22
We were unable to fully test the digital signature functionality of the program, because we could not find numbers small enough to use that also satisfied the necessary conditions for the algorithm to work.  Here are the values we got from an NSA website that we attempted to test the program with:
Message = 616263
P = 157754757658850164039820501368692494984638811981595753785726084071390339342949827166074468203116945260071420591948184266427919389750857419939387549499186051557325946160152109714671771886387784860670680481921786590260608186162263954672484772147274284399498187140357851764561666898851637006570752518678867635307
Q = 1331985975749110751467452671644594430583873510479
G = 147898545040606209330230055267646210530048641427472555641518780529319888952924449556772555570317947086022121909734653034292067334334687959961597799568568987279946842584777692484878672986933866319818683030808864041201327429509854041153169303558986971095604768418830701291626138041045041681927765991510706817653
The program produced a signature, however when we attempted to verify this signature, the program said the signature was not verified.  We have hypothesized that the numbers we used were too large, and that we lost some precision during our calculations, thus making the program unable to verify the signature.

User Instructions:

This program will run the digital signature standard algorithm.  This program is capable of digitally signing a message, and verifying that a given signed message is valid.  The user may use this program to safely transfer and read messages between two parties, as a digital signature ensures that no one else could have sent the message.  

When the program is run, the user will have the choice to generate their own public values, or input their public values.  These values include the 'p', 'q', and 'g' values that make up the public key.  Entering 'Authentic' enables the program to generate these values randomly, and entering 'Realistic' enables the program to ask the user to enter their own values. 
Next, the user will be able to choose to sign a message, or verify a signature.  Enter 'Sign' to sign a message, and 'Verify' to verify a message.  
The program will then ask for several more inputs, and then will generate a message signature, or will verify a message.  
When the program is finished running, the user will either be supplied with a signature for the given message, or will be informed whether or not the given signature is valid. 

Citations: 

We got sample values from this NSA pdf:
http://csrc.nist.gov/groups/ST/toolkit/documents/Examples/DSA2_All.pdf

We used this website to learn how to use the gmpy2 functions:
https://gmpy2.readthedocs.io/en/latest/mpz.html

We used this website to implement the Extended Euclidean Algorithm:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

We used this website to implement the modular multiplicative inverse algorithm:
Algorithm from: http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

We used this website to implement our SHA1 hash function:
https://docs.python.org/3.0/library/hashlib.html

We also used page 405 of Cryptography and Network Security, by William Stallings, to implement the Digital Signature Standard algorithm.