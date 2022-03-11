#Made Sequencer
class Sequencer:
    def __init__(self, maxValue):
        self.maxValue = maxValue
    def __len__(self):
        return self.maxValue
    def __getitem__(self, index):
        if 0 < index <= self.maxValue:
            return index * 10 # element index * 10
        else:
            raise IndexError('index out of range')
    def __contains__(self, item):
        return 0 < item <= self.maxValue

s = Sequencer(5) #i.g) 1~5 sequencer
