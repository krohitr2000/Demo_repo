#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SCS
#
# Created:     08-09-2023
# Copyright:   (c) SCS 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
aplhabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(plain_text,shift_key):
    cipher_text=''
    for char in plain_text:
        position=aplhabets.index(char)
        new_position=(position+shift_key)%26
        cipher_text+=aplhabets[new_position]
    print(f"Your output is : {cipher_text}")

def decrypt(cipher_text,shift_key):
    cesar_text=''
    for char in cipher_text:
        position=aplhabets.index(char)
        new_position=(position-shift_key)%26
        cesar_text+=aplhabets[new_position]
    print(f"Your output is : {cesar_text}")

print('Welcome !')
user_choice=input('Enter E for encryption and D for decryption : ').upper()
message=input('what is your message ? : ')
shift_key=int(input('Enter shift key :'))
if user_choice=='E':
    encrypt(message,shift_key)
else:
    decrypt(message,shift_key)