## Playfair Cipher  

### Description  
This Python program implements the **Playfair Cipher**, a digraph substitution cipher that encrypts pairs of letters in the plaintext. The cipher uses a **5x5 matrix** of letters, constructed from a keyword (**key**), and encrypts the plaintext based on specific rules.

### Key Features  
- Encrypts messages using the **Playfair Cipher**  
- Replaces the letter **'J'** with **'I'** (as the Playfair Cipher uses only 25 letters in the matrix)  
- Handles repeated letters by inserting an **'X'** between them  
- Works with **alphabetic characters** only (special characters and numbers are ignored)

---

### Technologies Used  
- Python 3.x  

---

### How to Run  

1. **Download** the script file.  
2. **Navigate** to the project directory:  
   ```bash
   cd playfair-cipher
## How It Works

The program will ask for two inputs:

- **Key:** A string used to create the Playfair Cipher matrix.  
- **Message:** The plaintext message to encrypt.

### 1. Creating the Matrix
- The key (provided by the user) is used to create the first part of the 5x5 matrix.  
- The matrix is then completed with the remaining letters of the alphabet (skipping 'J').

### 2. Preparing the Message
- The message is converted to uppercase, and 'J' is replaced with 'I'.  
- The message is split into pairs of letters.  
- If there is a repeated letter (e.g., "LL"), an 'X' is inserted between them (e.g., "LX").

### 3. Encryption
Each pair of letters is encrypted using these rules:

- **Same Row:** Letters are replaced by the letters immediately to their right.  
- **Same Column:** Letters are replaced by the letters immediately below them.  
- **Different Rows & Columns:** The letters form a rectangle, and the opposite corners of the rectangle are used.

### Note:
- Only alphabetic characters (A-Z) are considered.
