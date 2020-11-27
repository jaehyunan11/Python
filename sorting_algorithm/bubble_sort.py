def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                # swap the elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
                # setthe flag to True to begin the new loop
                swapped = True

# Verify it works
random_list_of_nums = [5,2,1,8,4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

def bubble_sort_2nd(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)- i -1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1], lst[j]

if __name__ == '__main__':
    lst = [3,2,1,5,4]
    bubble_sort_2nd(lst)
    print("Sorted list is ". lst)