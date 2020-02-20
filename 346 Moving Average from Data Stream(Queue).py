#Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Example:
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3

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


