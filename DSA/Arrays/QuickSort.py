def partition(arrays, low, high):
#The function to split the unsorted arrays into 2 parts
    pivot = arrays[high]  #Choosing the final element as the pivot element at first
    i = low - 1 #The pointer to record the right boundaries of smaller part than pivot element
    for j in range(low, high): #low ~ high, the "bigger part" than pivot element
        if arrays[j] <= pivot:
            i += 1
            arrays[i], arrays[j] = arrays[j], arrays[i]
    arrays[i+1], arrays[high] = arrays[high], arrays[i+1] #Switch the pivot value
    return i+1  #Returning the index where the next split in sub-arrays happens

def QuickSort(arrays, low=0, high=None):
    if high is None:
        high = len(arrays) - 1  #Default parameter of the final element
    if low < high: #Judging the number of element of sub-arrays
        pivot_index = partition(arrays, low, high) #Identifying the pivot element
        QuickSort(arrays, low, pivot_index-1)   #Sorting the smaller side than pivot
        QuickSort(arrays, pivot_index+1, high)  #Sorting the bigger side than pivot
    return arrays

#The core part of QuickSort is the func "partition" which identifies the pivot element of the sort
#The speed[O(nlog(n))] of the Sort depends on whether the pivot element is correctly identified or not

if __name__ == '__main__':
    arr=[12,43,65,32,67,14,78,98,44,55]
    print(QuickSort(arr))