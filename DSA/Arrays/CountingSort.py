def countingSort(arrays):
    max_value=max(arrays)   #Using the max value of unsorted arrays as the size of the count arrays
    count=[0] * (max_value + 1) #Using the size to initialize the count arrays
    while len(arrays) > 0:
        #Turn the values of the unsorted arrays into the index of count arrays
        num=arrays.pop(0)
        count[num] +=1
    for i in range(len(count)):
        #Sort and turn back
        while count[i] > 0:
            arrays.append(i)
            count[i] -= 1
    return arrays

#The number "k" of possible different values to be sorted is "len(count)"
#The number of values to be sorted "n" is "max_value"
#"k" must smaller than "n", or the Sort will be pointless

if __name__ == '__main__':
    arr=[1,2,2,7,7,8,8,4,4,3,3,9,9,1,1]
    print(countingSort(arr))