class User:
    '''
    Site users.
    '''

    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        '''
        Initializing user's characteristics.
        '''

        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self):
        '''
        Attribute update.
        '''

        tp = input('What do you want to change? 1 - first name, 2 - last_name, 3 - gender: ')
        if tp == '1':
            self.first_name = input('Enter: ')
        elif tp == '2':
            self.last_name = input('Enter: ')
        elif tp == '3':
            self.gender = input('Enter: ')

user_1 = User('0000001', 'Dub', 'Sasha')
print(user_1.gender)
print(user_1.first_name)
user_1.update()
print(user_1.gender)
print(user_1.first_name)
