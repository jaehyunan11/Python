
# Big O(1)
def getFirst(arr):
    return arr[0]

# Big O(N)
def example(arr):
    for i in arr: # O(N)
        print(i)

# Big O(N^2)
def example(arr):
    for x in arr: # O(N)
        for y in arr: # O(N)
            print(x,y)

# Some rules to remember
"""
Ignore constants : When using Big O notation, you always drop the constants.
So, even if the runtime complexity is O(2N), we call it O(N)

"""