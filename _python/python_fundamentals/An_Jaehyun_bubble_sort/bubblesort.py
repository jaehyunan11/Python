def bubble_sort(my_list):
    for i in range(len(my_list)): # 1st, 2dn .. nth iteration
        print(my_list)
        for j in range(0,len(my_list)-1-i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                print(my_list)
    return my_list

print(bubble_sort([23,73,17,86,34,8]))