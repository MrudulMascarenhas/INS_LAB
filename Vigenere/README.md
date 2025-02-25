# Vigenère Cipher 

## **Introduction**
The **Vigenère Cipher** is a fundamental encryption technique used in classical cryptography. It is a type of **polyalphabetic substitution cipher** where each letter in the plaintext is shifted based on a repeating keyword.

This program demonstrates the **encryption** and **decryption** processes of the Vigenère Cipher and serves as an introductory concept in cryptography for **network security applications**.

---

## **Features**
 Supports both **encryption** and **decryption**  
 Works with **uppercase and lowercase** letters  
 Preserves **non-alphabetic characters** (spaces, numbers, punctuation)  
 Uses a **repeating key** for shifting letters  
 Simple and efficient implementation in Python  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
- **Encryption**: Each letter in the plaintext is shifted forward based on the corresponding letter in the repeating keyword.  
- **Decryption**: The encrypted text is shifted backward using the same keyword to retrieve the original message.  
- **Modular Arithmetic**: Ensures shifts wrap around within the alphabet's range.

---

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/Vigenere.git
cd vigenere-cipher
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:
[Vigenère Cipher on Google Colab](https://colab.research.google.com/github/MrudulMascarenhas/INS_LAB/blob/main/Vigenere.ipynb)
