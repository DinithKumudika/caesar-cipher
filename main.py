from art import logo
from sys import exit

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


ALPHABET_LENGTH = 26

def in_alphabet(letter):
     if letter not in alphabet:
          return False
     else:
          return True
          

def encrypt_message(message,shift,final_str):
     for letter in message:
          if(not in_alphabet(letter)):
               final_str += letter
          else:
               pos = alphabet.index(letter)
               final_str += alphabet[pos+shift]    
     return final_str

def decrypt_message(message,shift,final_str):
     for letter in message:
          if(not in_alphabet(letter)):
               final_str += letter
          else:
               pos = alphabet.index(letter)
               final_str += alphabet[pos-shift]
     return final_str 

# code can be reduced by implementing both encryption and decryption in to ceaser_cipher function 
# depending on the user input without creating separate functions for them

def ceaser_cipher():
     choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
     message = input("Type your message:\n").lower()
     shift_amount = int(input("Enter offset:\n"))
     
     final_text = ""
   
     shift_amount = shift_amount % ALPHABET_LENGTH
     
     if(choice == "encode"):
          encoded_result = encrypt_message(message,shift_amount,final_text)
          print(f"Encoded message: {encoded_result}")
     elif(choice == "decode"):
          decoded_result = decrypt_message(message,shift_amount,final_text)
          print(f"Decoded message: {decoded_result}")
     else:
          print("wrong input! try again")
          
     repeat = input("type 'Y' if you want to try again, otherwise type 'N'\n").lower()
     if(repeat == "y"):
          ceaser_cipher()
     else:
          print("Thank you for using caesar cipher!")
          exit()
          

print(logo)

ceaser_cipher()
