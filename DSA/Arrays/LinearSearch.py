def linearSearch(arrays,n):
    for i in range(len(arrays)):
        if n == arrays[i]:
            return i
    return -1

if __name__ == '__main__':
    arr=[1,34,3,5,77,45,23,7]
    n=5
    if linearSearch(arr,n) != -1:
        print(f'Found {n} at index {linearSearch(arr,n)}')
    else:
        print('Not Found')