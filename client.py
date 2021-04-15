#CLIENT

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
cSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create a socket object
port = 9999 # Set destination port
serverAddr = ('localhost', port) # Include the server Address 

#variables
privKey = [ 2, 3, 6, 13, 27, 52, 105, 209, 418, 837, 1673, 3347, 6693, 13389, 26775, 53550]
mod = 107101
mult = 519

counter = 1

#CALC CLIENT PUB KEY AND SEND TO SERVER
clientPubKey = calcPubKey(privKey, mult, mod)
cSocket.sendto(clientPubKey.encode(), serverAddr) #send pubkey
print("client public key sent: " + clientPubKey +'\n')

#RECEIVE SERVER PUB KEY
serverPubKey, addr = cSocket.recvfrom(1024) #Receive no more than 1024 bytes
serverPubKey = serverPubKey.decode() #decode message
print("server public key received: " + serverPubKey +'\n')

#INV MOD
n1= modinv(mult,mod)
print('inv mod: ' + str(n1) + '\n')

#LOOP
while True:
    color.write('##### Message ' + str(counter) + ' Sent' + '\n','ERROR') #shows message number

    #ENCRYPT & SEND
    message = input("MSG: ") #message input
    print(" ")
    
    encryptedMessage = encrypt(message, serverPubKey) #encrypt message
    cSocket.sendto(encryptedMessage.encode(), serverAddr) #send pubkey
    print("ENCRYPTED MSG: " + encryptedMessage +'\n') #print encrypted message

    counter = counter + 1 #new message counter
    color.write('##### Message ' + str(counter) + ' Received' + '\n','ERROR') #shows message number

    #RECEIVE ENCRYPTED MESSAGE
    encryptedMessage, addr = cSocket.recvfrom(1024) #Receive no more than 1024 bytes
    encryptedMessage = encryptedMessage.decode() #decode
    print("ENCRYPTED MSG: " + encryptedMessage + '\n') #print encrypted message

    #DECRYPT MESSAGE
    decryptedMessage = decrypt(encryptedMessage, privKey, mult, mod) #decrypt message
    print("DECRYPTED MSG: " + decryptedMessage + '\n') #print decrypted message

    counter = counter + 1 #new message counter


