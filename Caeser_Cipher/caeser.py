def encrypt(textname,c):
 result = ""
 for i in range(len(textname)):
   char = textname[i]
   if (char.isupper()):
     result += chr((ord(char)+ c-65)% 26+65)
   else:
     result += chr((ord(char)+ c-97)% 26+97)
 return result
def decrypt(textname,c):
 result = ""
 for i in range(len(textname)):
  char = textname[i]
  if (char.isupper()):
   result += chr((ord(char)-c-65)% 26+65)
  else:
   result += chr((ord(char)- c-97)% 26+97)
 return result
textname=input("Enter the text:")
c=int(input("Enter the shift:"))
print("text:" + textname)
print(f"shift: {c}")
print(f"encrypted message: {encrypt(textname,c)}")
textname=encrypt(textname,c)
print(f"decrypted message: {decrypt(textname,c)}")