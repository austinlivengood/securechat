#Knapsack Algorithm


#CALCULATE PUBLIC KEY
def calcPubKey(privKey, mult, mod):

    pubKey = [ ] #init array

    #go through private key
    for i in privKey: 
        j = i * mult % mod #privkey[] * n % m
        pubKey.append(j) #add to array

    full_str = ' '.join([str(elem) for elem in pubKey]) #converts to string with space inbetween

    return full_str #return public key as a string





#CALCULATE INVERSE MOD
def modinv(n, m):
    
    n = n % m

    #go from 1 to m, x is n^-1
    for x in range(1, m): 
        if ((n * x) % m == 1):  #check if n(n^-1) mod m == 1
            return x 
        
    return x #return multiplicative inverse (n^-1)        





#ENCRYPT     
def encrypt(plaintext, publicKey):

    pubKey = publicKey.split(" ") #splits up public key by space

    pubKey = list(map(int, pubKey)) #converts public key to list

    binarytext = "" #init binarytext

    #goes through plaintext and converts to binary
    for letter in plaintext:
        asciivalue = ord(letter) #returns ascii int
        binaryvalue = format(asciivalue, '08b') #returns binary
        binarytext = binarytext + binaryvalue #adds to binary string

    blocks =([binarytext[i:i+16] for i in range(0, len(binarytext), 16)]) #splits up binary into blocks of 16

    cipherTotal = "" #init cipherTotal

    #goes through each block of 16
    for block in blocks:
        x = 0
        ciphertext = 0
        #in each block, multiplies each bit by the each value in public key
        for b in block:
            c = int(b) * pubKey[x]
            x = x + 1
            ciphertext = ciphertext + c
        cipherTotal = cipherTotal + str(ciphertext) + " " #extra space at the end is padding if odd number string
    

    cipherList = cipherTotal.split(" ") #splits into list
    cipherList.remove("") #remove space

    cipherStr = ' '.join([str(elem) for elem in cipherList]) #joins by space
    return cipherStr






#DECRYPT
def decrypt(ciphertext, privKey, n, m):

    ciphertext = ciphertext.split(" ") #splits up ciphertext by space

    ciphertext = list(map(int, ciphertext)) #converts to list of integers

    n1 = modinv(n,m) #calculate inv mod
    
    z = 0 #iterator to go through each ciphertext
    x = 15 #iterator to go through private key start at end
    message = [] #init message array
    msg='' #init message string

    #goes through ciphertext
    for each in range(len(ciphertext)):
        
        c = (ciphertext[z] * n1) % m #convert ciphertext ( c -> c')
        
        for i in privKey: #GREEDY algorithm used to decrypt
            if privKey[x] <= c: #if priv key value is less than or equal to c'
                c = c - privKey[x] #c' - priv key
                msg = msg + '1' #add a 1
                x = x - 1 #go backwards in priv key
            else:
                msg = msg + '0' #else add 0
                x = x - 1 #go backwards in priv key
        x = 15 #set priv key back to start at the end
        z = z + 1 #go to next ciphertext


    reverse = msg[::-1] #reverse binary


    blocks =([reverse[i:i+8] for i in range(0, len(reverse), 8)]) #divide binary string into 8 bit blocks

    plaintext="" #init plaintext
    b = 0 #init interator
    
    #goes through each block
    for b in range(len(blocks)):
        character = int(blocks[b],2) #converts each bit into a ascii int
        plaintext = plaintext + chr(character) #string of plaintext
        b = b + 1

    #switch things around ( y!wdHo -> Howdy!)
    end = len(plaintext)
    start = end - 2
    finalPlaintext=""

    #goes backwards through plaintext
    while (start >= 0):
        finalPlaintext = finalPlaintext + (plaintext[start:end]) #takes groups of 2 characters and adds them to final
        end = end -2 #back 2
        start = start -2 #back 2

    return finalPlaintext #returns final decrypted message
