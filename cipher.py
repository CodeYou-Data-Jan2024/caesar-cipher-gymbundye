# add your code here
#create dictionary for our cypher
caesar_cipher = {
    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j',
    'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
    'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't',
    'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
    'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd',
    'z': 'e'
}

#get the user input
normal_sentence = input("Enter your message:  ")
#convert sentence to deal with capitals
normal_sentence = normal_sentence.lower()
#do the conversion
cipher_sentence = ''
for char in normal_sentence:
    if char.isalpha():
        cipher_sentence += caesar_cipher[char]
    else:
        cipher_sentence += char
#print results
print("Normal sentence: ", normal_sentence)
print()
print("Ciphered sentence: ", cipher_sentence)
