class NotSleeping:
    '''
    class of people trying to sleep.
    '''

    def __init__(self):
        '''
        Initializing amounts of sheep.
        '''

        self.sheep = 0

    def add_sheep(self):
        '''
        Counting sheep.
        '''

        self.sheep += 1

dima = NotSleeping()

dima.add_sheep()
dima.add_sheep()
dima.add_sheep()

print(dima.sheep)
