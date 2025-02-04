keys = {
'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u', 'h': 'i','i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g', 'p': 'h','q': 'j', 'r':
'k', 's': 'l', 't': 'z', 'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b',
'y': 'n', 'z': 'm'
}
reverse_keys = {v: k for k, v in keys.items()}
def encrypt(text):
 text = text.lower()
 encrypttext = []
 for i in text:
  encrypttext.append(keys.get(i, i))
 return ''.join(encrypttext)
def decrypt(text):
 text = text.lower()
 decrypttext = []
 for i in text:
  decrypttext.append(reverse_keys.get(i, i))
 return ''.join(decrypttext)
x = input("Enter the plain text: ")
encrypted_text = encrypt(x)
decrypted_text = decrypt(encrypted_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)