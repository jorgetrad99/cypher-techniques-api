import sys
import json


def encrypt(clearText, key):

    result = ""

    matrix = [["" for x in range(len(clearText))] for y in range(key)]

    increment = 1
    row = 0
    col = 0

    for c in clearText:
        if row + increment < 0 or row + increment >= len(matrix):
            increment = increment * -1

        matrix[row][col] = c

        row += increment
        col += 1

    for list in matrix:
        result += "".join(list)

    return result


def decrypt(cipherText, key):

    result = ""

    matrix = [["" for x in range(len(cipherText))] for y in range(key)]

    idx = 0
    increment = 1

    for selectedRow in range(0, len(matrix)):
        row = 0

        for col in range(0, len(matrix[row])):
            if row + increment < 0 or row + increment >= len(matrix):
                increment = increment * -1

            if row == selectedRow:
                matrix[row][col] += cipherText[idx]
                idx += 1

            row += increment

    matrix = transpose(matrix)
    for list in matrix:
        result += "".join(list)

    return result


def transpose(m):

    result = [[0 for y in range(len(m))] for x in range(len(m[0]))]

    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]

    return result


message = sys.argv[1]
depth = int(sys.argv[2])

encryptedMessage = encrypt(message, depth)
decryptedMessage = decrypt(encryptedMessage, depth)


rail_fence = {
    "message": message,
    "depth": depth,
    "encryptedMessage": ''.join(encryptedMessage),
    "decryptedMessage": decryptedMessage
}

print(json.dumps(rail_fence))
