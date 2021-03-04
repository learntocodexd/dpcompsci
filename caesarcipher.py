def caesar(plainText, shift): 
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift 
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
        else:
            stayInAlphabet = ord(ch) + shift
        finalLetter = chr(stayInAlphabet)
        cipherText += finalLetter
    print("Your ciphertext is: ", cipherText)


inputText = input("Enter the text you want to caesar cipher: ")
inputShift = int(input("Enter the shift value in for your cipher: "))

caesar(inputText, inputShift)
