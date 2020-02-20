class MovingAverage:
    def __init__(self,size):
        self.size = size
        self._sum = 0
        self.array = []
        
    def calculate_average(self,val):
        self._sum += val
        self.array.append(val)
        if len(self.array) > self.size:
            self._sum = self._sum - self.array[0]
            self.array.pop(0)
            
        self.get_average()
        
    def get_average(self):
        print(self._sum / len(self.array))
    
MovingAverage_obj = MovingAverage(3)
p1 = MovingAverage_obj.calculate_average(1)
p2 = MovingAverage_obj.calculate_average(5)
p3 = MovingAverage_obj.calculate_average(12)
p4 = MovingAverage_obj.calculate_average(4)
p5 = MovingAverage_obj.calculate_average(-1)


