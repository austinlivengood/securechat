# Secure Chat Application

Austin Livengood 


CLIENT & SERVER

*Run the server first, then the client

Initially the client and server public keys are calculated and sent to each other. 
Then the client sends the first message that is decrypted by the server. Next the server 
sends the second message that is decrypted by the client. 
This continues back and forth until the program is closed.

Each message is numbered and the program keeps a count which is displayed in the window. 
Each message number statement is in red in order to clearly differentiate between messages.


KNAPSACK

This file contains functions for calculating the public key, inverse modulo, encryption, and 
decryption. 

The comments added in the file explain most of the code. One part I feel requires additional 
explanation is a section in my decryption function with a comment header of 
“switch things around”. I ran into a weird problem where my ciphertext was decrypted 
properly but the order of characters was inaccurate, it was backwards in groups of two. For 
example, instead of decrypting “Howdy!” it came out to “y!wdHo”. This was likely caused 
by the way I appended the decrypted blocks of ciphertext to the plaintext string 
(I went backwards through the private key to decrypt). 

That additional code added in the decryption function was the easiest way I found for 
me to fix the problem.
