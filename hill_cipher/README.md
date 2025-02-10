# Hill Cipher Encryption Program

## Description
This project implements a simple Hill Cipher encryption algorithm in Python. The Hill Cipher is a polygraphic substitution cipher based on linear algebra. It encrypts a plaintext message by treating it as a vector and multiplying it by a key matrix.

## How It Works
The program will ask for the following inputs:

- **Plaintext:** The message that needs to be encrypted.
- **Key Matrix:** A square matrix used for encryption.

### 1. User Input

- **Plaintext:** Input message that will be converted to uppercase and padded if needed.
- **Key Matrix:** A user-defined square matrix that will be used for the encryption process.

### 2. Encryption Process

- The program uses the Hill Cipher algorithm to encrypt the plaintext.
- After the encryption, the program displays the encrypted text.

### 3. Padding

- If the length of the plaintext is not divisible by the size of the key matrix, it will be padded with the letter "X".

## Features

- Encrypts a given plaintext using a user-defined key matrix.
- Pads the plaintext with the letter "X" if its length is not divisible by the size of the key matrix.
- Simple and efficient implementation using NumPy for matrix operations.

## Requirements

- Python 3.x
- **Libraries**:
  - `numpy` (install via `pip install numpy`)

