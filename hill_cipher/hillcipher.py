import numpy as np
def hill_cipher(plaintext,key):
 n=len(key)
 plaintext = plaintext.upper().replace(" ", "")
 if len(plaintext) % n != 0:
  plaintext += "X" * (n - len(plaintext) % n)
  plaintext_vector = [ord(char) - ord('A') for char in plaintext]
  ciphertext=""
  for i in range(0,len(plaintext_vector),n):
   block=plaintext_vector[i:i+n]
   result=np.dot(key,block)%26
   ciphertext += "".join(chr(num + ord('A')) for num in result)
  return ciphertext
plaintext="HELLO"
key=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("encrypted_text:",hill_cipher(plaintext,key))
