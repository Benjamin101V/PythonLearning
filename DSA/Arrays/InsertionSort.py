def InsertionSort_1(arrays):
    for i in range(1,len(arrays)):
        # An outer loop that picks a value to be sorted
        insert_index=i
        current_value=arrays.pop(i) #Cut the value who will be sorted
        for j in range(i-1,-1,-1):
            # An inner loop that goes through the sorted part of the array
            # To find where to insert the value
            if arrays[j] > current_value:
                insert_index=j
        arrays.insert(insert_index,current_value)
    return arrays

#Improvement by only shifting the value necessary
def InsertionSort_2(arrays):
    for i in range(len(arrays)):
        insert_index=i
        current_value=arrays[i]
        for j in range(i-1,-1,-1):
            if arrays[j] > current_value:
                arrays[j+1]=arrays[j]
                insert_index=j
            else:
                #There is no need to continue comparing values when we have already found the correct place for the current value
                break
        arrays[insert_index]=current_value
    return arrays

arr=[12,43,55,86,90,23,21,4,56,77]
print(InsertionSort_1(arr))
print(InsertionSort_1(arr))