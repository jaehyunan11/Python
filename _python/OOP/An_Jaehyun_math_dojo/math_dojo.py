class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for num2 in nums:
            self.result += num2
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for num2 in nums:
            self.result -= num2
        return self

# create an instance:
md = MathDojo()
# to test
x = md.add(7).add(2,5,1).add(3,5,7,9).subtract(2).subtract(3,2,1).subtract(5,4,3,2,1).result
print(x)