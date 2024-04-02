class Point:
    '''
    Class of points on a plane.
    '''

    def __init__(self, cord=(0, 0)):
        '''
        Initializing point's coordinates.
        '''

        self.x, self.y = cord
    
    def get_x(self):
        '''
        Get coorginate x
        '''

        return self.x

    def get_y(self):
        '''
        Get coorginate y
        '''

        return self.y

    def distance(self, other):
        '''
        Distance between points.
        '''
        
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    def sum(self, other):
        '''
        Coordinate of the new point as the sum of another 2.
        '''

        return Point((self.x + other.x, self.y + other.y))
    
    def __str__(self):
        '''
        Conver result to string.
        '''

        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        '''
        Conver result to consol.
        '''
        return self.__str__()

point_1 = Point()
point_2 = Point((3, 4))
print(f'расстояние между {point_1} и {point_2} равно {point_1.distance(point_2)}')

point_3 = point_1.sum(point_2)
point_4 = point_3.sum(point_2)
print(f'новые точки: {point_3}, {point_4}')
print(f'расстояние между {point_1} и {point_2} равно {point_1.distance(point_4)}')
