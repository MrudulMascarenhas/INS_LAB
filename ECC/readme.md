# Elliptic Curve Cryptography (ECC) Key Exchange 

## **Introduction**
The **Elliptic Curve Cryptography (ECC) Key Exchange** is a cryptographic protocol that enables two parties to securely exchange cryptographic keys using elliptic curve cryptography (ECC). It provides stronger security with shorter key lengths compared to traditional Diffie-Hellman.

This program demonstrates the **key exchange process** of the ECC algorithm and serves as an advanced concept in cryptography for **network security applications**.

---

## **Features**
- Securely exchanges cryptographic keys between two parties using **elliptic curves**  
- Uses **private and public keys** for secure key generation  
- Establishes a **shared secret key** without direct transmission  
- Simple and efficient implementation in **Python** using the **tinyec** library  

---

## **Technologies Used**
- **Python 3.x**  
- **tinyec library** for elliptic curve operations  

---

## **How It Works**
- **Elliptic Curve Selection**: A specific elliptic curve (e.g., "brainpoolP256r1") is used.  
- **Private Key Generation**: Each party selects a **random private key**.  
- **Public Key Computation**: Public keys are derived from the private keys using elliptic curve multiplication.  
- **Shared Secret Key Computation**: Each party computes a **shared key** using the other party's public key and their own private key.  

---

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/ECC_Key_Exchange.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:  
[Elliptic Curve Cryptography Key Exchange on Google Colab](https://colab.research.google.com/drive/1Ip42Ma0JSBhhAlAaoqzOxsmHkpR83dCB?usp=sharing)
