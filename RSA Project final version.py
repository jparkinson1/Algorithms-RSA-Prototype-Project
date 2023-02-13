import random
import gc
import math

# Code by: Joshua Parkinson, Nicholas Colet, and Nate Geoghagan

#generate a random number
def generateNum():
    
    randNum = random.randint(2, 1000000000000000)
    return randNum

#tests if number is prime
def testIfPrime(prime):
    
   if prime <= 1:
       return False
   
   if prime == 2:
       return True
   
   if prime % 2 == 0:
       return False
   
   maximum = math.floor(math.sqrt(prime)) + 1
   
   for i in range(3, maximum, 2):
       if prime % i == 0:
           return False
       
   return True

#generates a prime number using testIfPrime to verify
def primeGenerator():
    
    num = generateNum()
    test = testIfPrime(num)
    
    if test == False:
        return primeGenerator()
    
    else:
        return num

#find GCD
def findGCD(a,b):
    
    result = math.gcd(a,b)
    return result

#find e
def findE(phi):
    
    e = random.randint(1, phi)
    
    if findGCD(e, phi) != 1:
        return findE(phi)
    
    return e

#find inverse of e and phi which will be d
def modinv(e,phi):
    
    return  pow(e,-1,phi)

#Convert to ASCII
def convASCII(message):
    
    Ascii = []
    
    for character in message:
        Ascii.append(ord(character))
        
    return Ascii

#Encrypt with public key
def publicEncrypt(m, e, n):
    
    m = pow(m, e, n)
    return m

#Decrypt with private key
def privateDecrypt(m, d, n):
    
    msg = pow(m, d, n)
    return msg

#encrypt message prompt and driver
def encryptMsg(msg, e, n):
    
    i = 0
    
    while i < len(msg):
        msg[i] = publicEncrypt(msg[i], e, n)
        i = i + 1
  
    return msg

#Decrypt message driver
def decryptMsg(msg, d, n):
    
    i = 0
    j = 0
    decipheredMsg = ""
    
    for i in range(len(msg)):
        msg[i] = privateDecrypt(msg[i], d, n)
        i = i + 1
    
    for j in msg:
        decipheredMsg = decipheredMsg + chr(j)
  
    return decipheredMsg

# prompt for message to be used
def promptMsg():
    msg = input("Please enter message for encryption: ")
    
    while bool(msg) == False:
        print("Invalid input. Message cannot be empty!")
        msg = input("Please enter your message:")
        
    msg = convASCII(msg)
    return msg

# public key holder
def publicUser(publicMsg, e, n):
    while True:
        print("As a public user, what would you like to do?")
        print("\t1. Send an encrypted message.")
        print("\t2. Authenticate a digital signature.")
        print("\t3. Log out to previous menu.")
        
        while True:
            choice = input("\nEnter your choice: ")
                
            try:
                choice = int(choice)
                break
                
            except ValueError:
                print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
                
        if 1 < choice > 3:
            print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
        
        if choice == 1:
            main.publicMsg = promptMsg()
            main.publicMsg = encryptMsg(main.publicMsg,e,n)
            publicLst.append(main.publicMsg)
            print("The message as ciphertext from encrypting with the public key:\n", main.publicMsg,"\n")
            
        if choice == 2:
            if bool(privateLst) == False:
                print("\nError: No signature to authenticate!\n")
                
            else:
                print("Messages that are available:")
                
                for i in range(len(privateLst)):
                    print(f'{i + 1}. length = {len(privateLst[i])}')
                    
                choose = int(input("Enter your choice: "))
                if not choose.isdigit():
                    print("Invalid choice!")
                    publicUser(publicMsg, e, n)
                
                main.privateMsg = decryptMsg(privateLst[choose - 1], e, n)
                print("\nThe message decrypted is: ", main.privateMsg)
                privateLst.pop(choose-1)
            
        if choice == 3:
            break    

# private key holder
def privateUser(publicMsg, d, n):
    while True:
        print("As the owner of the keys, what would you like to do?")
        print("\t1. Decrypt a received message.")
        print("\t2. Digitally sign a message.")
        print("\t3. Log out to previous menu.")
        while True:
           choice = input("\nEnter your choice: ")
               
           try:
               choice = int(choice)
               break
               
           except ValueError:
               print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
               
        if 1 < choice > 3:
                print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
        
        if choice == 1:
            
            if bool(publicLst) == False:
                print("\nError: No message to decrypt!\n")
                
            else:
                print("Messages that are available:")
                
                for i in range(len(publicLst)):
                    print(f'{i + 1}. length = {len(publicLst[i])}')
                    
                choose = int(input("Enter your choice: "))
                main.publicMsg = decryptMsg(publicLst[choose - 1], d, n)
                print("\nThe message decrypted is: ", main.publicMsg)
                publicLst.pop(choose-1)
                
        if choice == 2:
            main.privateMsg = promptMsg()
            main.privateMsg = encryptMsg(main.privateMsg, d, n)
            privateLst.append(main.privateMsg)
            print("The message as ciphertext from signing with the private key:\n", main.privateMsg,"\n")
            
        if choice == 3:
            break

# Two lists to hold the messages encrypted with the public key and another for messages encrypted with the private key
publicLst = []
privateLst = []

#main
def main():
    main.publicMsg = ""
    main.privateMsg = ""
    p = primeGenerator()
    q = primeGenerator()
    n = p * q
    pnot = p - 1
    qnot = q - 1
    phi = pnot * qnot
    e = findE(phi)
    d = modinv(e, phi)
    
    while True:
        print("Please select your user type: ")
        print("\t1.A public user")
        print("\t2.The owner of the keys")
        print("\t3.Exit program")
        
        while True:
           choice = input("\nEnter your choice: ")
               
           try:
               choice = int(choice)
               break
               
           except ValueError:
               print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
               
        if 1 < choice > 3:
                print("\nInvalid input! Please enter a valid choice, numbers 1 through 3: ")
        
        if choice == 1:
            publicUser(main.publicMsg, e, n)
            
        if choice == 2:
            privateUser(main.publicMsg, d, n)
            
        if choice == 3:
            print("Thank you for using this program! Exiting!")
            gc.collect()
            break
        
main()
