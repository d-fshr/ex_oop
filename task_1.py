class Dog:
    '''
    Class of Dogs
    '''

    def __init__(self, name):
        '''
        Initializing dog.
        '''
        
        self.name = name
    
    def say(self):
        '''
        Output on display 'Гав'
        '''

        print('Гав!')

dog = Dog('ПЁС')
dog.say()
