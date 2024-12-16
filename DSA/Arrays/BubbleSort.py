def BubbleSort_1(arrays):
    for i in range(len(arrays)-1):
        for j in range(len(arrays)-i-1):
            if arrays[j]>arrays[j+1]:
                arrays[j],arrays[j+1] = arrays[j+1],arrays[j]
    return arrays

arr=[12,32,54,78,45,98,22,55,95,33]
print(BubbleSort_1(arr))
print('\n')

#Bubble Sort Improvement
def BubbleSort_2(arrays):
    for i in range(len(arrays)-1):
        swapped=False   #It's assumed that the values weren't swapped
        for j in range(len(arrays)-i-1):
            if arrays[j]>arrays[j+1]:
                arrays[j],arrays[j+1] = arrays[j+1],arrays[j]
                swapped=True    #To identify the values were swapped, even only one
#If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, and we can stop the algorithm
        if not swapped:
            break
    return arrays

arr=[5,1,6,34,55,45,54,84,76,101,99]
print(BubbleSort_2(arr))
print('\n')