# Diffie-Hellman Key Exchange 

## **Introduction**
The **Diffie-Hellman Key Exchange** is a fundamental cryptographic protocol used for securely exchanging cryptographic keys over a public channel. It enables two parties to establish a shared secret key without transmitting it directly, ensuring secure communication.

This program demonstrates the **key exchange process** of the Diffie-Hellman algorithm and serves as an introductory concept in cryptography for **network security applications**.

---

## **Features**
- Securely exchanges cryptographic keys between two parties  
- Uses **prime numbers** and **primitive roots** for key generation  
- Establishes a **shared secret key** without transmitting it directly  
- Simple and efficient implementation in **Python**  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
- **Prime Number Selection**: A large prime number (**q**) and a **primitive root (a)** are chosen.  
- **Private Key Selection**: Each party selects a private key (**Xa** for A, **Xb** for B).  
- **Public Key Computation**: Public keys (**Ya** and **Yb**) are computed using modular exponentiation.  
- **Shared Secret Key Computation**: Each party computes a **shared key** using the other party's public key and their own private key.  

---

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/DiffieHellman.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:  
[Diffie-Hellman Key Exchange on Google Colab](https://colab.research.google.com/drive/1Us_FSySsv67-zCqibkeByxLq33z6cfHN?usp=sharing)

