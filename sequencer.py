#201902934 컴전 이호영
#Made Sequencer
Touched by user2
class Sequencer:
    def __init__(self, maxValue):
        self.maxValue = maxValue
    def __len__(self):
        return self.maxValue
    def __getitem__(self, index): #메서드 재정의/인덱스로 아이템 값접근
        if 0 < index <= self.maxValue:
            return index * 10 # element index * 10
        else:
            raise IndexError('index out of range')
    def __contains__(self, item):
        return 0 < item <= self.maxValue
  
num = int(input()) #숫자입력받기
s = Sequencer(num)
print([s[i] for i in range(1, num+1)]) #s객체를 통해 얻을수 있는 값
t = Sequencer(1)
print(t[0])
