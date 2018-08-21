''' Problem 2 - PlaintextMessage '''
# For this problem, the graders will use our implementation of the Message class,
# so don't worry if you did not get the previous parts correct.

# PlaintextMessage is a subclass of Message and has methods to encode a string
# using a specified shift value. Our class will always create an encoded version
# of the message, and will have methods for changing the encoding.

# Implement the methods in the class PlaintextMessage according to the specifications in ps6.py.
# The methods you should fill in are:
# __init__(self, text, shift): Use the parent class constructor to make your code more concise.
# The getter method get_shift(self)
# The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict.
# The getter method get_message_text_encrypted(self)
# change_shift(self, shift): Think about what other methods you can use to make this easier.

### Helper code

def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list

WORDLIST_FILENAME = 'words.txt'

### Paste your implementation of the `PlaintextMessage` class here
class Message(object):
    '''### DO NOT MODIFY THIS METHOD ###'''
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        shift_dict = {}

        for i in range(97, 123, 1):
            shift_dict[chr(i)] = chr(97+(i-97+shift)%26)
        for i in range(65, 91, 1):
            shift_dict[chr(i)] = chr(65+(i-65+shift)%26)

        return shift_dict
        # pass #delete this line and replace with your code here

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # pass #delete this line and replace with your code here
        message = ""
        shift_dict = self.build_shift_dict(shift)
        for i in self.message_text:
            if i in shift_dict:
                message += shift_dict[i]
            else:
                message += i
        return message


### Helper code End
class PlaintextMessage(object):
    '''PlaintextMessage'''
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        # pass #delete this line and replace with your code here
        self.msg_txt = Message(text)
        self.message_text = text
        self.shift = shift
        self.valid_words = self.msg_txt.get_valid_words()
        self.encrypting_dict = self.msg_txt.build_shift_dict(self.shift)
        self.message_text_encrypted = self.msg_txt.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        # pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        # pass #delete this line and replace with your code here
        return self.msg_txt.build_shift_dict(self.shift)

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        # pass #delete this line and replace with your code here
        return self.msg_txt.apply_shift(self.shift)

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # pass #delete this line and replace with your code here
        # return
        self.shift = shift

def main():
    ''' Function to handle testcases '''
    inp = input()
    data = PlaintextMessage(inp, int(input()))
    print(data.get_shift())
    print(data.get_encrypting_dict())
    print(data.get_message_text_encrypted())
    data.change_shift(int(input()))
    print(data.get_shift())
    print(data.get_encrypting_dict())
    print(data.get_message_text_encrypted())

if __name__ == "__main__":
    main()
