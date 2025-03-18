# DES Encryption 

## **Introduction**
The **Data Encryption Standard (DES)** is a fundamental encryption technique used in classical cryptography. It is a type of **block cipher** where plaintext is encrypted in fixed-size blocks using a symmetric key. 

This program demonstrates the **encryption** and **decryption** processes of the DES algorithm and serves as an introductory concept in cryptography for **network security applications**. 

---

## **Features**
 - Supports both **encryption** and **decryption**  
 - Works with **8-byte blocks** of plaintext  
 - Uses a **56-bit key** for encryption  
 - Implements **ECB (Electronic Codebook) mode**  
 - Produces **hexadecimal ciphertext** for encrypted messages  
 - Simple and efficient implementation in **Python**  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
- **Encryption**: Each 8-byte block of plaintext is encrypted using a **56-bit key**, resulting in ciphertext.  
- **Decryption**: The ciphertext is decrypted using the same **key**, and padding is removed to retrieve the original message.  
- **Key Generation**: A secure **random key** is generated to ensure encryption security.  
- **Block Cipher**: DES encrypts data in **64-bit (8-byte) blocks** rather than individual characters.  

---

## **Setup and Execution**

### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/DES.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:  
[DES Encryption on Google Colab](https://colab.research.google.com/drive/1V7xMJdfXhlqhATBzauTi4tG6A5Rpps0L?usp=sharing)

