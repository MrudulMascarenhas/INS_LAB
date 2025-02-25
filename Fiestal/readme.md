#  Feistel-Based Binary Encryption Algorithm

## **Introduction**
This program implements a **Feistel-based binary encryption algorithm** using bitwise operations and modular arithmetic. It converts a string into its binary representation, splits it into two halves, applies a key for encryption using **addition and XOR operations**, and then swaps parts to generate the cipher text.

This serves as a fundamental introduction to encryption techniques used in **network security applications**.

---

## **Features**
- Supports **encryption** and **decryption**  
- Works with **any string input**  
- Implements **Feistel-like structure** for encryption  
- Uses **binary conversion and bitwise operations**  
- Preserves **character encoding** for accurate decryption  
- Simple and efficient implementation in **Python**  

---

## **Technologies Used**
- **Python 3.x**  

---

## **How It Works**
1. **Binary Conversion**: Converts each character in the input string to an 8-bit binary format.  
2. **Splitting**: Divides the binary string into two equal halves.  
3. **Key Addition**: Adds a binary-encoded key to one half.  
4. **XOR Operation**: Performs a bitwise XOR operation between the modified half and the other half.  
5. **Swapping**: Swaps the resulting binary halves for additional security.  
6. **Final Encryption**: Repeats steps 3-5 for additional rounds, producing the cipher text.  
7. **Decryption**: Reverses the encryption steps to retrieve the original message.  

---

## **Setup and Execution**
### **1. Clone the Repository**
git clone https://github.com/MrudulMascarenhas/Fiestal.git
cd Fiestal


### **2. Run the Code in Google Colab**
You can also execute the code using Google Colab:
[Fiestal on goole colab](https://colab.research.google.com/drive/1xN6v7IsKeoxJwaKzDykXopsgR3XeKqSI?usp=sharing))
