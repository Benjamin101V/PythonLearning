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

#Radix Sort Using Other Sorting Algorithms
from BubbleSort import BubbleSort_2
#Radix Sort can actually be implemented together with any other sorting algorithm as long as it is stable
def radixSort_bubbleSort(arrays):
    max_value = max(arrays)
    exp = 1
    while max_value // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        for num in arrays:
            radix_index = (num // exp) % 10
            radixArray[radix_index].append(num)
        for container in radixArray:
            BubbleSort_2(container)
        i = 0
        for container in radixArray:
            for num in container:
                arrays[i] = num
                i += 1
        exp *= 10
    return arrays
#Attention: The sort in radixArray must be stable sort , or will cause wrong results
#Stable Sort:The sort which the positions of elements of the same size do not change during tne sorting process
if __name__ == '__main__':
    arr = [12, 101, 323, 543, 5, 78, 212, 78, 666, 767]
    print(radixSort(arr))
    print(radixSort_bubbleSort(arr))