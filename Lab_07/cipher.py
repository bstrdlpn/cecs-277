class Cipher:
    """
    Atbash Cipher - is a substitution cipher where the encrypted message is
    obtained by looking up each letter and finding the corresponding letter in a reversed alphabet.
    The encoded letter can be found in one of two ways, either a parallel list look up (ex. letter to
    encode = 'B', location = 1, encoded letter location = 1, which is a 'Y'), or a calculated position
    in the list (ex. letter to encode = 'B', location = 1, 25 - location = 24, encoded letter location =
    24, which is a 'Y')
    """
    
    def __init__(self):
        """
        initializes the alphabet attribute - make a list with the letters A-Z in it
        (alternatively, make a string with letters A-Z in it, since a string is a list of characters)
        """
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    def encrypt_message(self, message):
        """
        pass in the message string. Convert the message
        to upper case letters, then loop through the message string one character at a time, if it is
        a letter A-Z, then call the encrypt_letter method, otherwise ignore the character. Build
        the encryption string using the encrypted letters and ignored characters, and then return it
        (ie. leave all spaces, punctuation, and numbers the same, only letters in the string will be
        encrypted)
        """
        message = message.upper()
        
        encrypted_string = ''

        for char in message:
            if char.isalpha():
                encrypted_string += self.encrypt_message(char)

        return encrypted_string
                        

    def _decrypt_message(self, message):
        """
        pass in the message string. Convert the message
        to upper case letters, then loop through the message string one character at a time. Build
        the decryption string using the decrypted letters in a manner similar to the
        encrypt_message method above.
        """
        message = message.upper()
        decrypted_string = ''

        for char in message:
            if char.isalpha():
                decrypted_string += self._decrypt_letter(char)

        return decrypted_string


    def _encrypt_letter(self, letter):
        """
        passes in one character, letter. Look up the letter
        in the alphabet to find its location. Use that location to calculate the position of the
        encrypted letter in the manner described above, then return the encrypted letter.
        """
        letter = letter.isalpha()
        reverse_alphabet = self._alphabet.copy().reverse()
        encrypted_letter = ''

        for index, char in enumerate(self._alphabet):
            if char == letter:
                encrypted_letter = reverse_alphabet[index]
        return encrypted_letter
    

    def _decrypt_letter(self, letter):
        """
        passes in one character, letter. Look up the letter
        in the alphabet to find its location. Use that location to calculate the position of the
        decrypted letter in the manner described above, then return the decrypted letter.
        """
        letter = letter.isalpha()
        reverse_alphabet = self._alphabet.copy().reverse()
        decrypted_letter = ''

        for index, char in enumerate(reverse_alphabet):
            if char == letter:
                decrypted_letter = self._alphabet[index]
        return decrypted_letter