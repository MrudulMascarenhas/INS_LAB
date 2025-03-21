## Monoalphabetic Substitution Cipher

This repository contains implementations of various cryptographic techniques and algorithms as part of the Information and Network Security (INS) Lab. The programs demonstrate encryption, decryption, key exchange, and secure communication methods.  


## Introduction

The Monoalphabetic Substitution Cipher is a type of substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a predefined mapping. Unlike the Caesar Cipher, which shifts letters by a fixed number, this cipher uses a fixed but random substitution for each letter.

This program demonstrates the encryption and decryption processes of the Monoalphabetic Cipher, making it a fundamental concept in network security and cryptography.

#### Features  
 - Supports both encryption and decryption
 - Works with uppercase and lowercase letters
 - Preserves non-alphabetic characters (spaces, numbers, punctuation)
 - Uses a predefined substitution mapping for stronger encryption than Caesar Cipher

### How It Works
 
- Encryption: Each letter in the plaintext is substituted with its corresponding letter from the predefined mapping.
- Decryption: The encrypted text is mapped back to the original letters using the inverse of the predefined substitution.
- Fixed Key Mapping: The encryption and decryption mappings are static and predefined, making the cipher stronger than simple shift-based ciphers. 

---

## **Setup and Execution** 
### **1. Clone the Repository** 
```sh 
git clone https://github.com/MrudulMascarenhas/Monoalphabetic_Cipher.git 
```
### **2. Run the Code in Google Colab** 
You can also execute the code using Google Colab: 
[Monoalphabetic Cipher on Google Colab](https://colab.research.google.com/drive/1sMjr-0RvIBzsiE4o2QMTgJ8wxTUE3LbQ?usp=sharing)



