def merge(left, right):
    #Merge and sort the sub-arrays
    Sorted = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            Sorted.append(left[i])
            i += 1
        else:
            Sorted.append(right[j])
            j += 1
    Sorted.extend(left[i:]) #Add the remainder element into result
    Sorted.extend(right[j:])
    return Sorted

#Use recursion
def mergeSort_1(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    sortedLeft = mergeSort_1(leftHalf)
    sortedRight = mergeSort_1(rightHalf)
    return merge(sortedLeft, sortedRight)

#Without recursion
def mergeSort_2(arr):
    step = 1  #Starting with sub-arrays of length 1
    length = len(arr)
    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)
            #Place the merged array back into the original array
            for j, val in enumerate(merged):
                arr[i + j] = val
        step *= 2  #Double the sub-array length for the next iteration
    return arr

if __name__ == '__main__':
    arr=[101,23,22,54,44,55,5,5,34,65]
    print(mergeSort_1(arr))
    print(mergeSort_2(arr))