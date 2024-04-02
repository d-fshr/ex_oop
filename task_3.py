class NotSleeping:
    '''
    class of people trying to sleep.
    '''

    def __init__(self):
        '''
        Initializing amounts of sheep.
        '''

        self.__sheep = 0

    def add_sheep(self):
        '''
        Counting sheep.
        '''

        self.__sheep += 1

    def lost(self):
        '''
        Lost of sheep.
        '''

        self.__sheep = 0
    
    def get_count_sheeps(self):
        '''
        Returns the number of sheep.
        '''

        return self.__sheep


dima = NotSleeping()

dima.add_sheep()
dima.add_sheep()
print(dima.get_count_sheeps())

dima.lost()
dima.add_sheep()
print(dima.get_count_sheeps())
