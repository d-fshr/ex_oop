class StandsDNA:
    '''
    Сlass that stores DNA chains.
    '''

    def __init__(self, all_strands):
        '''
        Initializing list of DNA chains.
        '''

        self.all_strands = all_strands

    def add_strands(self, strands):
        '''
        Add new DNA chains.
        '''

        self.all_strands += strands.split()
    
    def get_max_stands(self):
        '''
        Create string of DNA chains with maximum len
        '''

        res = []
        result = ''
        mx = 0

        for chain in self.all_strands:
            if len(chain) > mx:
                res = [chain]
                mx = len(chain) 
            elif len(chain) == mx:
                if chain not in res:
                    res.append(chain)
            
        res.sort()
        
        for item in res:
            result += item + ' '
        
        return result[:-1]


strnds = ['ГТЦ', 'АЦА', 'ТЦАА', 'ГЦГ', 'ТЦАА', 'ГГТ', 'АЦАТ']
dna = StandsDNA(strnds)

print(dna.get_max_stands())

new_strnds = 'ГЦТАТ ЦТ'
dna.add_strands(new_strnds)

print(dna.get_max_stands())
