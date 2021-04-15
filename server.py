#SERVER

#import socket programming module
import socket

#import functions
from knapsack import calcPubKey
from knapsack import encrypt
from knapsack import decrypt
from knapsack import modinv

#set up to add color
import sys

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

#socket setup
sSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create socket object
clientAddr = "localhost" # Get local machine address                       
port = 9999 # Set port number for this server                                          
sSocket.bind((clientAddr, port)) # Bind to the port                                  

#variables
privKey = [ 3, 7, 11, 22, 45, 89, 179, 357, 714, 1429, 2857, 5717, 11431, 22862, 45724, 91448]
mod = 182899
mult = 378

counter = 1

#RECEIVE CLIENT PUB KEY
print("Waiting to receive message on port " + str(port) + '\n')
   
clientPubKey, addr = sSocket.recvfrom(1024) #Receive the data of 1024 bytes maximum
clientPubKey = clientPubKey.decode()
print("client public key received: " + clientPubKey +'\n')

#CALC SERVER PUB KEY AND SEND TO CLIENT
serverPubKey = calcPubKey(privKey, mult, mod)
sSocket.sendto(serverPubKey.encode(), addr) #send pubkey
print("server public key sent: " + serverPubKey +'\n')

#INV MOD
n1= modinv(mult,mod)
print('inv mod: ' + str(n1) + '\n')

#LOOP
while True:
   color.write('##### Message ' + str(counter) + ' Received' + '\n','ERROR') #shows message number

   #RECEIVE ENCRYPTED MESSAGE
   encryptedMessage, addr = sSocket.recvfrom(1024) #Receive no more than 1024 bytes
   encryptedMessage = encryptedMessage.decode() #decode
   print("ENCRYPTED MSG: " + encryptedMessage + '\n') #print encrypted message

   #DECRYPT MESSAGE
   decryptedMessage = decrypt(encryptedMessage, privKey, mult, mod) #decrypt message
   print("DECRYPTED MSG: " + decryptedMessage + '\n') #print decrypted message
   
   counter = counter + 1 #new message counter
   color.write('##### Message ' + str(counter) + ' Sent' + '\n','ERROR') #shows message number

   #ENCRYPT & SEND
   message = input("MSG: ") #message input
   print(" ")
    
   encryptedMessage = encrypt(message, clientPubKey) #encrypt message
   sSocket.sendto(encryptedMessage.encode(), addr) #send encrypted message
   print("ENCRYPTED MSG: " + encryptedMessage + '\n') #print encrypted message

   counter = counter + 1 #new message counter

