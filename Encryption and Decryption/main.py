alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def Encode(text):
    ind = 0
    charind = 0
    new_string = ""
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if(text[i] == alphabet[j]):
                charind = j
                break
        if (shift + charind) < len(alphabet):
            new_string += alphabet[shift + charind]
        else:
            new_string += alphabet[ind]
            ind += 1
    return new_string
  
def Decode(text):
    ind = len(alphabet) - 1
    charind = 0
    new_string = ""
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if(text[i] == alphabet[j]):
                charind = j
                break
        if(charind - shift) >= 0:
            new_string += alphabet[charind - shift]
        else:
            new_string += alphabet[ind]
            ind -= 1
    return new_string
  
  if direction == "encode":
    str1 = Encode(text)
    print(str1)
elif direction == "decode":
    str2 = Decode(str1)
    print(str2)
