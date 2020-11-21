# If you want to implement Linear Search in python 
# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(f"x is here at index {i}")
            return i

    return -1

arr = [10, 20, 80, 30, 60, 50, 40, 110, 100, 130, 170]
x = 110

print(search(arr, x))