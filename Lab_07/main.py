import cipher
import caesar
import check_input

def main():
    """
    Have the user choose to encrypt or decrypt a message, then have them choose
    an encryption/decryption method (Atbash or Caesar cipher). If they choose to encrypt, then
    prompt them to enter a message to encrypt, then write the encrypted message to the file
    'message.txt'. If they choose to decrypt a message, read the message from the file 'message.txt'
    and then display the decrypted message to the console. If they choose to use a Caesar Cipher for
    either encryption or decryption, then prompt the user to enter a shift value (0-25)
    """

    print("-Secret Decoder Ring-")
    action = check_input.get_int_range("1. Encrypt Message\n2.Decrypt Message\n", 1, 2)
    if action == 1:
        print("Enter encryption type:")
        encrypt = check_input.get_int_range("1. Atbash\n2.Caesar Cipher\n", 1, 2)
        message_e = input("Enter message: ")
        if encrypt == 1:
            message_e = message_e.cipher.encrypt_message()
        else:
            #ask for shift number
            #encrypt message in caesar
        file = open("message.txt", "w")
        file.write(message_e)
        file.close()
        print("Encrypted message saved to 'message.txt'")
    else:
        print("Enter decryption type:")
        decrypt = check_input.get_int_range("1. Atbash\n2.Caesar Cipher\n", 1, 2)
        file = open("message.txt")
        
        if decrypt = 1:
            #decrypt message in atbash
        else:
            #ask for shift number
            #decrypt message in caesar
        #message_d = decrypted message from message.txt
        print("Reading encrypted message from 'message.txt'...")
        #print("Decrypted message: " + message_d)
main()