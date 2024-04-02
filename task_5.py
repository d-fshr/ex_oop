import random

class Game:
    '''
    Class of playing basketball
    '''

    def __init__(self, teams):
        '''
        Initializing team's characteristics.
        '''

        self.teams = teams
        self.score = {teams['command1']: 0, teams['command2']: 0}

    def ball_thrown(self, command, points):
        '''
        Scoring points.
        '''

        self.score[self.teams[command]] += points

    def get_score(self):
        '''
        Returns the score of game.
        '''

        return tuple(self.score.items())
    
    def get_winner(self):
        '''
        Revealing the winner.
        '''

        if self.score[self.teams['command1']] > self.score[self.teams['command2']]:
            return self.teams['command1']
        elif self.score[self.teams['command1']] < self.score[self.teams['command2']]:
            return self.teams['command2']
        else:
            return 'Ничья'

com = {'command1': 'НГУ', 'command2': 'НГТУ'}
scores = Game(com)
for _ in range(10):
    n_team = str(random.randint(1, 2))
    am_points = random.randint(1, 3)
    scores.ball_thrown('command' + n_team, am_points)

print(scores.get_score())
print(scores.get_winner())
