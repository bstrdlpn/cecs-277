class Cipher:
    """
    Atbash Cipher - is a substitution cipher where the encrypted message is 
    obtained by looking up each letter and finding the corresponding letter in a 
    reversed alphabet. The encoded letter can be found in one of two ways, 
    either a parallel list look up (ex. letter to encode = 'B', location = 1, 
    encoded letter location = 1, which is a 'Y'), or a calculated position in 
    the list (ex. letter to encode = 'B', location = 1, 25 - location = 24, 
    encoded letter location = 24, which is a 'Y')
    """
    
    def __init__(self):
        """Initialize the alphabet attribute - make string with letters A-Z."""
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def encrypt_message(self, message):
        """
        Encrypt the message string.
        
        :param message: string, message string to encrypt
        :returns: The encrypted string
        """
        # force upper for message string
        message = message.upper()
        
        encrypted_string = ''

        # loop through message string, if char is an alphabetic char, encrypt
        # using class function and append char to a list.
        for char in message:
            if char.isalpha():
                encrypted_string += self._encrypt_letter(char)
            else:
                encrypted_string += char

        return encrypted_string
                        

    def _decrypt_message(self, message):
        """
        Decrypt the message string.
        
        :param message: string, message string to decrypt
        :returns: decrypted message string
        """
        message = message.upper()
        decrypted_string = ''

        for char in message:
            if char.isalpha():
                decrypted_string += self._decrypt_letter(char)
            else:
                decrypted_string += char

        return decrypted_string


    def _encrypt_letter(self, letter):
        """
        Helper function, encrypt a letter.

        :param letter: char, letter to encrypt
        :returns: encrypted letter       
        """
        letter = letter.upper()

        # reverse the self._alphabet list
        reverse_alphabet = self._alphabet[::-1]

        # index method gets the index number in the alphabet string
        index = self._alphabet.index(letter)
        return reverse_alphabet[index]
    

    def _decrypt_letter(self, letter):
        """
        Helper function, decrypt a letter.

        :param letter: char, letter to decrypt
        :returns: decrypted letter
        """
        letter = letter.isalpha()
        reverse_alphabet = self._alphabet[::-1]
    
        index = reverse_alphabet.index(letter)
        return self._alphabet[index]