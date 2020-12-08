class numeric:
    def __init__(self,valueX,valueY):
        self.valueX=valueX
        self.valueY=valueY
    
    def __sb__(self,valueX,valueY):
        x1=self.valueX + self.valueX
        y1=self.valueY + self.valueY
        sum = numeric(x1,y1)
        return sum
      
    def __gt__(self , other):
        return self.valueX > other.valueX
    
if __name__ == '__main__':
    sum1 = numeric(290, 100)
    sum2 = numeric(100, 80)
    if(sum1 > sum2):
        print('sum1 is greater than sum2')
    else:
        print('sum2 is greater than sum1')