def insertionSort(arr):
    # Traverse through 1 to len(arr)

    for i in range(1, len(arr)):
        print(f"Current Array: {arr}")
        key = arr[i]
        print(f"First key: {key}")
        # move elements of arr[0.. i-1] that greater than key
        # to one position of their curent position
        j = i-1
        print(f"First j: {j}, arr[j]: {arr[j]}")
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(f"Updated j: {j}")
        arr[j+1] = key
        print(f"Updated key: {key}")
        print(f"Updated Array: {arr}")
# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is")
for i in range(len(arr)):
    print("%d"% arr[i])