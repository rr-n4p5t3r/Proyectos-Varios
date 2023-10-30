def caesar_cipher(text,desp):
   cipher = ""
   for i in range(len(text)): #Para cada letra del texto
      char = text[i]
      if (char.islower()):
          cipher += chr((ord(char) + desp - 97) % 26 + 97) #97 letra minuscula (a)
      else:
          cipher += chr((ord(char) + desp-65) % 26 + 65) # Prima letra mayuscula (A) 
    return cipher