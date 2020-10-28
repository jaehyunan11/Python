#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#  Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(arr):
    for num in range(len(arr)):
        if arr[num] > 0:
            arr[num] = "big"
    return arr

print(biggie_size([-1, 3, 5, -5]))

#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#  Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#  Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(arr):
    positive_num_count = 0
    for num in arr:
        if num > 0:
            positive_num_count += 1
    arr[len(arr)-1] = positive_num_count
    return arr

print(count_positives([1,6,-4,-2,-7,-2]))
print(count_positives([-1,1,1,1]))

#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#  Example: sum_total([1,2,3,4]) should return 10
#  Example: sum_total([6,3,-2]) should return 7

def sum_total(arr):
    sum = 0
    for num in range(len(arr)):
        sum = sum + arr[num]
    return sum

print(sum_total([1,2,3,4]))


#4 Average - Create a function that takes a list and returns the average of all the values.
#  Example: average([1,2,3,4]) should return 2.5

def average(arr):
    average = 0
    total = 0
    for num in range(len(arr)):
        total = total + arr[num]
    average = float(total) / float(len(arr))
    return average

print(average([1,2,3,4])) 


#5 Length - Create a function that takes a list and returns the length of the list.
#  Example: length([37,2,1,-9]) should return 4
#  Example: length([]) should return 0

def length(arr):
    count = 0
    for num in arr:
        count += 1
    return count

print(length([37,2,1,-9]))
print(length([]))

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#  Example: minimum([37,2,1,-9]) should return -9
#  Example: minimum([]) should return False

def minimum(arr):
    if len(arr) == 0:
        return False
    else:
        min_num = arr[0]
        for num in arr:
            if num < min_num:
                min_num = num
    return min_num

print(minimum([37,2,1,-9]))
print(minimum([]))

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#  Example: maximum([37,2,1,-9]) should return 37
#  Example: maximum([]) should return False

def maximum(arr):
    if len(arr) == 0:
        return False
    else:
        max_num = arr[0]
        for num in arr:
            if num > max_num:
                max_num = num
    return max_num

print(maximum([37,2,1,-9]))
print(maximum([]))


#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#  Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(arr):
    sum = sum_total(arr)
    avg = average(arr)
    min = minimum(arr)
    max = maximum(arr)
    len = length(arr)
    analysis = {
        'sumTotal': sum,
        'average' : avg,
        'minumum' : min,
        'maixmum' : max,
        'length' : len
    }
    return analysis

print(ultimate_analysis([37,2,1,-9]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#  Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(nums_list):
    list_len = len(nums_list)
    for num in range(int(list_len/2)):
        temp = nums_list[list_len-1-num]
        nums_list[list_len-1-num] = nums_list[num]
        nums_list[num] = temp
    return nums_list

print(reverse_list([37,1,2,-9]))