import sys
import json


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return("" . join(encrypt_text))


def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


message = sys.argv[1]
keyword = sys.argv[2]
key = generateKey(message, keyword)
encryptedMessage = encryption(message, key)
decryptedMessage = decryption(encryptedMessage, key)


vigenere = {
    "message": message,
    "keyword": keyword,
    "generatedKey": key,
    "encryptedMessage": encryptedMessage,
    "decryptedMessage": decryptedMessage
}

print(json.dumps(vigenere))
