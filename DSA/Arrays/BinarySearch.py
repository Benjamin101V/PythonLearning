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

if __name__ == '__main__':
    arr = [1,5,12,34,55,66,67,85,87,101]
    n = 101
    if binarySearch(arr, n) != -1:
        print(f'Found {n} at index - {binarySearch(arr ,n)} -')
    else:
        print('Not Found')