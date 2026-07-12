class TextNormalization:
    def __init__(self,data):
        self.data = data
        self.start()
    def start(self):
        print('''
            1)Converting  strings to lower case
            2)Removing Punctuations
            3)Removing Spl char
            4)Handling Emoji's
            5)Removing Extra Spaces
            6)Contractions
            7)Correcting the words
             ''')
        print('1)Converting strings to lower case....')
        self.strings_lowercase()
        option_punctuation = input('Enter Yes/No').lower()
        if option_punctuation=='yes':
            pass
        else:
            pass

        
    def strings_lowercase(self,data):
        # return updated_text
        self.data = self.data.lower()
    def removing_punctuations(self):
        data = self.data
        import string
        punctuations = string.punctuation
        for char in punctuations:
            chars = chars.replace(char,'')
        self.data = chars
    def removing_spl_char(self):
        chars = self.data
        for char in chars:
            if not char.isalnum() and not ord(char)==32:
                chars = chars.replace(char,'')
        self.data=chars
    def handling_emoji(self):
        
obj = TextNormalization('corrting the wods for txt normalization')

        
