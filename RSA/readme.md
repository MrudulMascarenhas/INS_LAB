# RSA Encryption 

## **Introduction**
The **RSA Algorithm** is a widely used encryption technique in modern cryptography. It is an **asymmetric cipher** where plaintext is encrypted using a public key and decrypted using a private key. 

This program demonstrates the **encryption** and **decryption** processes of the RSA algorithm and serves as an introductory concept in cryptography for **network security applications**.

---

## **Features**
- Supports both **encryption** and **decryption**  
- Uses **public and private key pairs**  
- Ensures **secure communication** through asymmetric encryption  
- Implements **modular exponentiation** for encryption and decryption  
- Simple and efficient implementation in **Python**  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
- **Key Generation**: Two large prime numbers are chosen to compute **n**, and the **public and private keys** are derived.  
- **Encryption**: The plaintext message is raised to the power of **e (public key exponent)** modulo **n**, resulting in ciphertext.  
- **Decryption**: The ciphertext is raised to the power of **d (private key exponent)** modulo **n** to retrieve the original message.  
- **Greatest Common Divisor (GCD)**: Ensures that **e** is coprime with **phi(n)** for secure key selection.  

---

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/RSA.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:  
[RSA Encryption on Google Colab](https://colab.research.google.com/drive/1ZUMTwdcEjY5YnTz09CQIkGJtrJMj33hS?usp=sharing)

