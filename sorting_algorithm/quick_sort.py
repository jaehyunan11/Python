# Partitioning : Choose a pivot
# Pivot : The value within the partitioning space that I want to find a position for
# 
# j : job to scan from L to R -1 
# [1,5,2,6,8]

def quicksort(listToSort, lowIndex, highIndex):
    if ((highIndex - lowIndex) > 0):
        p = partition(listToSort, lowIndex, highIndex)
        quicksort(listToSort,lowIndex,highIndex-1)