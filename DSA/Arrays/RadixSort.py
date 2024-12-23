def radixSort(arrays):
    radixArray = [[],[],[],[],[],[],[],[],[],[]] #An 2D-array to hold values with the current radix in focus
    max_value = max(arrays)
    exp = 1
    while max_value // exp > 0:
        #The outer loop ensure that all digit can be run, by the max value of the unsorted arrays
        while len(arrays) > 0:
            #The operation(in loop) move the value from unsorted arrays into the position with their different radix in radix array
            temp = arrays.pop()
            radix_index = (temp // exp) % 10
            radixArray[radix_index].append(temp)
        for container in radixArray:
            #Move the element back to the arrays
            while len(container) > 0:
                temp = container.pop()
                arrays.append(temp)
        exp *= 10
    return arrays

arr=[12,101,323,543,5,78,212,78,666,767]
print(radixSort(arr))