class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        print(sum(nums))
        # for num in nums:
        #     print(num)
        #     self.result += num
        #     print(self.result)
        # return self
    def subtract(self, num, *nums):
        pass

# create an instance:
md = MathDojo()
# to test
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)

x = md.add(2,5,1).result
print(x)