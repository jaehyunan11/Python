# Interative 
# It returns index of x in given array arr if present, 
# else returns -1 

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        print(f"Mid Num: {arr[mid]}")
        # if x is greater, ignor left half
        if arr[mid] < x:
            low = mid + 1
            print(f"low Num: {arr[low]}, index: {low}")
            print(f"x is not existed in left array from {arr[low]}")

        # if x is smaller, ignore right half 
        elif arr[mid] > x:
            high = mid - 1
            print(f"high Num: {arr[high]}, index: {high}")
            print(f"x is not existed in right array from {arr[high]}")

        # check if x is present at mid
        else:
            return mid
    
    # If we reach here, then element was not present
    return -1

# Test Array
arr = [2, 3, 4, 10, 40]
x = 40

result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")