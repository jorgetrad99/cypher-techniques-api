import sys
import json


def encryption(text, depth):
    fence = [[None] * len(text) for n in range(depth)]
    rails = range(depth - 1) + range(depth - 1, 0, -1)
    for n, x in enumerate(text):
        fence[rails[n % len(rails)]][n] = x

    if 0:  # debug
        for rail in fence:
            print(''.join('.' if c is None else str(c) for c in rail))

    return [c for rail in fence for c in rail if c is not None]


def decryption(text, n):
    rng = range(len(text))
    pos = encryption(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


message = sys.argv[1]
depth = int(sys.argv[2])

encryptedMessage = ''.join(encryption(message, depth))
decryptedMessage = decryption(encryptedMessage, depth)


rail_fence = {
    "message": message,
    "depth": depth,
    "encryptedMessage": encryptedMessage,
    "decryptedMessage": decryptedMessage
}

print(json.dumps(rail_fence))
