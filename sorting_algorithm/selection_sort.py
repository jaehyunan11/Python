def selection_sort(list):
    for i in range(0, len(list)-1):
        smallest = i
        print(f"smallest for i: {smallest}")
        for j in range(i+1, len(list)):
            if list[j] < list[smallest]:
                smallest = j
                print(f"smallest for j: {smallest}")
        list[i], list[smallest] = list[smallest], list[i]

    return list

list = [29, 72, 98, 13, 87, 66, 52, 51, 36]
print(selection_sort(list))
