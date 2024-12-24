def binarySearch(arrays, targetVal):
    left = 0
    right = len(arrays) - 1
    while left <= right:
        mid = (left + right) // 2
        if arrays[mid] == targetVal:
            return mid
        if arrays[mid] < targetVal:
            left = mid + 1
        else:
            right = mid -1
    return -1
#For the Binary Search algorithm to work,the array must already be sorted, so we can use Sort Alogrithm first when we face some unsorted arrays
if __name__ == '__main__':
    from QuickSort import QuickSort

    arr1 = [1,5,12,34,55,66,67,85,87,101]
    arr2 = [12,1,5,34,66,55,85,87,101,67]
    arr = QuickSort(arr1)
    #arr = QuickSort(arr2)    #But this way can not find the elements' index in original arrays
    n = 101
    if binarySearch(arr, n) != -1:
        print(f'Found {n} at index - {binarySearch(arr ,n)} -')
    else:
        print('Not Found')