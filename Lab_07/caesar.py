import cipher

class Caesar(cipher.Cipher):
    """Caesar Cipher – this is another substitution cipher where the encrypted
    message is found by looking up each letter and finding the corresponding letter in a shifted
    alphabet (ex. letter to encode = ‘B’, location = 1, shift value = 3, location + shift value = 1 + 3 =
    4, encoded letter location = 4, which is an ‘E’). If the shift value causes the encoded letter to be
    past the end of the alphabet, then it should wrap around to the beginning (ex. letter to encode =
    ‘X’, location = 23, shift value = 3, location + shift value = 23 + 3 = 26, encoded letter location =
    26, which is larger than 25, subtract the total number of letters in the alphabet to get the updated
    location, 26 – 26 = 0, which is an ‘A’)"""

    # non-alpha characters should be left alone

    
    def __init__(self, shift):
        """passes in caesar cipher’s shift value. Call super to initialize
        the alphabet, then set the shift value"""
        self._shift  = shift
        pass

    def _encrypt_letter(self, letter):
        """overridden method – passes in one character,
        letter. Look up the letter in the alphabet to find its location. Use that location to calculate
        the position of the encrypted letter in the manner described above, then return the
        encrypted letter"""
        
        # encrypt function caesar = (letter_index + shift value) mod 26
        pass


    def _decrypt_letter(self, letter):
        """overridden method – passes in one character,
        letter. Look up the letter in the alphabet to find its location. Use that location to calculate
        the position of the decrypted letter in the manner described above, then return the
        decrypted letter"""

        # decrypt function caesar = (letter_index - shift value) mod 26
        #for each character in the message:
            #take index of each letter and subtract from it the shift value
            #save the letter in decrypted message string
        #