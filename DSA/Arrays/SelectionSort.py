def SelectionSort_1(arrays):
    for i in range(len(arrays)-1):
        min_index=i
        #This loop must loop through one less value each time it runs
        for j in range(i+1,len(arrays)):
            if arrays[i] > arrays[j]:
                min_index=j
        #Finds the lowest value, and moves it to the front of the array
        min_value=arrays.pop(min_index)
        arrays.insert(i,min_value)
    return arrays

#Here is an implementation of the improved Selection Sort, using swapping
def SelectionSort_2(arrays):
    for i in range(len(arrays)-1):
        for j in range(i+1,len(arrays)):
            if arrays[i] > arrays[j]:
                temp=arrays[i]
                arrays[i]=arrays[j]
                arrays[j]=temp
    return arrays

if __name__ == '__main__':
    arr = [12, 54, 13, 56, 32, 87, 95, 10, 5, 3]
    print(SelectionSort_1(arr))
    print(SelectionSort_2(arr))