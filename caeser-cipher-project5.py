# caesar cipher
# a technique to send secret messages 
# it will be encrypted and it will be sent , hacker can't hack messages so easily

# to do both encryption and decryptino change only shift_key
# for encryption shift_key remains the same , for decryption shift_key=shift_key*-1

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabets[new_position]
        else:
            cipher_text+=char
        
    print("The encrypted message is",cipher_text)


def decryption(cipher_text,shift_key):
    decrypted_text=""
    for char in cipher_text:
        if char in alphabets:  
            position=alphabets.index(char)
            new_position=(position-shift_key)%26 
            decrypted_text+=alphabets[new_position]
        else:
            decrypted_text+=char
    print("The decrypted text is",decrypted_text)

wanna_end=False

while not wanna_end:
    what_to_do=input("Enter 'encrypt' to perform encryption or 'decrypt' to perform decryption:")
    text=input("Enter the text:").lower()
    shift=int(input("Enter the shift key number:"))

    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    
    want_to_continue=input("Do you want to perform this program once again?(Enter 'yes' or 'no')")
    if want_to_continue=="no":
        wanna_end=True
        print("Have a nice day!Bye...")