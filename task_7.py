class TrafficLight:
    '''
    Class of traffic light.
    '''

    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self, current_signal, previous_signal=None):
        '''
        Initializing traffic light's color.
        '''

        self.curren_signal = current_signal
        self.previous_signal = previous_signal
    
    def next_signal(self):
        '''
        Сhanges traffic light signal.
        '''

        if self.curren_signal == TrafficLight.permissible_values[0]:
            self.previous_signal = self.curren_signal
            self.curren_signal = TrafficLight.permissible_values[1]
            
        elif self.curren_signal == TrafficLight.permissible_values[2]:
            self.previous_signal = self.curren_signal
            self.curren_signal = TrafficLight.permissible_values[1]
        
        else:
            if self.previous_signal == TrafficLight.permissible_values[0]:
                self.previous_signal = self.curren_signal
                self.curren_signal = TrafficLight.permissible_values[2]
            else:
                self.previous_signal = self.curren_signal
                self.curren_signal = TrafficLight.permissible_values[0]
    
tr_lght = TrafficLight('зеленый')
for _ in range(10):
    print(tr_lght.curren_signal)
    tr_lght.next_signal()
