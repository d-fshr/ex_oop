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
    
class Segment:
    '''
    Class of line segment.
    '''

    def __init__(self, point_1, point_2):
        '''
        Initializing line's coordinates.
        '''

        self.point_1 = point_1
        self.point_2 = point_2
    
    def one_intersection(self):
        '''
        Determines whether one coordinate axis intersects.
        '''

        p_1 = self.point_1
        p_2 = self.point_2

        if p_1.get_x() == 0 and p_1.get_y() == 0 or p_2.get_x() == 0 and p_2.get_y() == 0:
            return False
        elif p_1.get_x() == 0 and p_1.get_y() != 0 and p_2.get_x() != 0 and p_2.get_y() == 0:
            return False
        elif p_1.get_x() != 0 and p_1.get_y() == 0 and p_2.get_x() == 0 and p_2.get_y() != 0:
            return False 

        elif p_1.get_x() == 0 and p_2.get_x() != 0 and p_1.get_y() * p_2.get_y() < 0 :
            return False
        elif p_2.get_x() == 0 and p_1.get_x() != 0 and p_1.get_y() * p_2.get_y() < 0 :
            return False
        
        elif p_1.get_y() == 0 and p_2.get_y() != 0 and p_1.get_x() * p_2.get_x() < 0 :
            return False
        elif p_2.get_y() == 0 and p_1.get_y() != 0 and p_1.get_x() * p_2.get_x() < 0 :
            return False
        
        elif p_1.get_x() >= 0 and p_1.get_y() >= 0 and p_2.get_x() >= 0 and p_2.get_y() <= 0:
            return True
        elif p_1.get_x() >= 0 and p_1.get_y() <= 0 and p_2.get_x() >= 0 and p_2.get_y() >= 0:
            return True
        
        elif p_1.get_x() >= 0 and p_1.get_y() >= 0 and p_2.get_x() <= 0 and p_2.get_y() >= 0:
            return True
        elif p_1.get_x() <= 0 and p_1.get_y() >= 0 and p_2.get_x() >= 0 and p_2.get_y() >= 0:
            return True  

        elif p_1.get_x() <= 0 and p_1.get_y() <= 0 and p_2.get_x() >= 0 and p_2.get_y() <= 0:
            return True
        elif p_1.get_x() >= 0 and p_1.get_y() <= 0 and p_2.get_x() <= 0 and p_2.get_y() <= 0:
            return True
        
        elif p_1.get_x() <= 0 and p_1.get_y() <= 0 and p_2.get_x() <= 0 and p_2.get_y() >= 0:
            return True
        elif p_1.get_x() <= 0 and p_1.get_y() >= 0 and p_2.get_x() <= 0 and p_2.get_y() <= 0:
            return True 
        
        return False

class CoordinateSystem:
    '''
    Class of coordinate system.
    '''

    segments = []

    def __init__(self):
        '''
        Initializing coordinate system.
        '''

        pass

    def add_segment(self, segment):
        '''
        Add line segment on coordinate system.
        '''

        CoordinateSystem.segments.append(segment)


    def axis_intersection(self, segment):
        '''
        Determines number of segments that intersect with coordinate axis.
        '''

        count = 0

        for segment in CoordinateSystem.segments:
            if segment.one_intersection():
                count += 1
    
        return count


pnt_1 = Point((1, 1))
pnt_2 = Point((-1, 2))
sgmnt = Segment(pnt_1, pnt_2)

plane = CoordinateSystem()
plane.add_segment(sgmnt)

pnt_1 = Point((0, -1))
pnt_2 = Point((2, 2))
sgmnt = Segment(pnt_1, pnt_2)
plane.add_segment(sgmnt)

print(plane.axis_intersection(sgmnt))
