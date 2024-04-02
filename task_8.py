class MorseMsg:
    '''
    Morse code messages class.
    '''

    eng_alph = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z'
    }

    rus_alph = {
        '.-': 'А',
        '-...': 'Б',
        '.--': 'В',
        '--.': 'Г',
        '-..': 'Д',
        '.': 'Е',
        '...-': 'Ж',
        '--..': 'З',
        '..': 'И',
        '.---': 'Й',
        '-.-': 'К',
        '.-..': 'Л',
        '--': 'М',
        '-.': 'Н',
        '---': 'О',
        '.--.': 'П',
        '.-.': 'Р',
        '...': 'С',
        '-': 'Т',
        '..-': 'У',
        '..-.': 'Ф',
        '....': 'Х',
        '-.-.': 'Ц',
        '---.': 'Ч',
        '----': 'Ш',
        '--.-': 'Щ',
        '--.--': 'Ъ',
        '-.--': 'Ы',
        '-..-': 'Ь',
        '..-..': 'Э',
        '..--': 'Ю',
        '.-.-': 'Я'
    }

    vowels_eng = ['A', 'E', 'I', 'O', 'U']
    consonants_eng = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 
                      'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    
    vowels_rus = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Э', 'Ы', 'Я', 'Ю']
    consonants_rus = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 
                      'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ъ']

    def __init__(self, mess):
        '''
        Initializing message.
        '''

        self.mess = mess

    def eng_decode(self):
        '''
        Decode message to english
        '''

        res = ''
        lttr_lst = self.mess.split()

        for letter in lttr_lst:
            res += MorseMsg.eng_alph[letter]

        return res
    
    def ru_decode(self):
        '''
        Decode message to russian
        '''

        res = ''
        lttr_lst = self.mess.split()

        for letter in lttr_lst:
            res += MorseMsg.rus_alph[letter]

        return res

    def get_vowels(self, lang):
        '''
        Vowels in particular language.
        '''
        
        vowels = []

        if lang == 'ru':
            for letter in self.ru_decode():
                if letter in MorseMsg.vowels_rus:
                    vowels.append(letter)
        
        elif lang == 'eng':
            for letter in self.eng_decode():
                if letter in MorseMsg.vowels_eng:
                    vowels.append(letter)
        
        return vowels
    
    def get_consonants(self, lang):
        '''
        Consonants in particular language.
        '''
        
        consonants = []

        if lang == 'ru':
            for letter in self.ru_decode():
                if letter in MorseMsg.consonants_rus:
                    consonants.append(letter)
        
        elif lang == 'eng':
            for letter in self.eng_decode():
                if letter in MorseMsg.consonants_eng:
                    consonants.append(letter)
        
        return consonants

ptr = '-.. ..- -... --- -.-'
mess = MorseMsg(ptr)

print(mess.ru_decode())
print(mess.get_vowels('ru'))
print(mess.get_consonants('ru'))

print(mess.eng_decode())
print(mess.get_vowels('eng'))
print(mess.get_consonants('eng'))
