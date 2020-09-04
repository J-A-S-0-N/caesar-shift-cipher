word1 = ["A", "B", "C", "D" ,"E" ,"F", "G", "H", "I", "J", "K", "L" ,"M" ,"N" ,"O", "P", "Q", "R", "S" ,"T", "U", "V", "W" ,"X" ,"Y" ,"Z"]
original = ["A", "B", "C", "D" ,"E" ,"F", "G", "H", "I", "J", "K", "L" ,"M" ,"N" ,"O", "P", "Q", "R", "S" ,"T", "U", "V", "W" ,"X" ,"Y" ,"Z"] 

def answer():
    result = []
    print("enter the shift number")
    shift = input(">> ")
    print("enter the word to encript")
    enc = input(">> ")


    for i in range(0, int(shift)):
        letter = word1[i]
        word1.pop(i)
        word1.append(letter)

    enc = list(enc)
    for i in range(0, len(enc)):
        enc_letter = enc[i]
        enc_index = original.index(enc_letter)
        result.append(word1[enc_index])

    result = "".join(result)

    return result

print(answer())