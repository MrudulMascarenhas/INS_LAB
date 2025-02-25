# Caesar Cipher 

## **Introduction**
The **Caesar Cipher** is a fundamental encryption technique used in classical cryptography. It is a type of **substitution cipher** where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. 

This program demonstrates the **encryption** and **decryption** processes of the Caesar Cipher and serves as an introductory concept in cryptography for **network security applications**.

---

## **Features**
 - Supports both **encryption** and **decryption**  
 - Works with **uppercase and lowercase** letters  
 - Preserves **non-alphabetic characters** (spaces, numbers, punctuation)  
 - Shift key wraps around using **modulo 26** for proper letter rotation  
 - Simple and efficient implementation in **Python**  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
- **Encryption**: Each letter in the plaintext is shifted forward by a given number (key).  
- **Decryption**: The encrypted text is shifted backward by the same key to retrieve the original message.  
- **Modular Arithmetic**: If shifting exceeds the alphabet's range, it wraps around using modulo 26.

---

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/Caser_Cipher.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:
[Caesar Cipher on Google Colab](https://colab.research.google.com/drive/1Ip42Ma0JSBhhAlAaoqzOxsmHkpR83dCB?usp=sharing)

