# Hill Cipher Encryption Program

## Description
This project implements a simple Hill Cipher encryption algorithm in Python. The Hill Cipher is a polygraphic substitution cipher based on linear algebra. It encrypts a plaintext message by treating it as a vector and multiplying it by a key matrix.

## How It Works
- **Plaintext:** The message that needs to be encrypted.
- **Key Matrix:** A square matrix used for encryption. 
- **Plaintext:** Input message that will be converted to uppercase and padded if needed.
- **Key Matrix:** A user-defined square matrix that will be used for the encryption process.
- The program uses the Hill Cipher algorithm to encrypt the plaintext.
- After the encryption, the program displays the encrypted text.
- If the length of the plaintext is not divisible by the size of the key matrix, it will be padded with the letter "X".

## Features

- Encrypts a given plaintext using a user-defined key matrix.
- Pads the plaintext with the letter "X" if its length is not divisible by the size of the key matrix.
- Simple and efficient implementation using NumPy for matrix operations.

## Requirements

- Python 3.x
- **Libraries**:
  - `numpy` (install via `pip install numpy`)

## **Setup and Execution**
### **1. Clone the Repository**
```sh
git clone https://github.com/MrudulMascarenhas/hill_cipher.git
```

### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:
[Hill Cipher on Google Colab](https://colab.research.google.com/drive/1-TJ3JQVXgg6hfGEEbBOe7pVaZLZ-shXL?usp=sharing)
