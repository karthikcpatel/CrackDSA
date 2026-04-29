def getMinMax(array, n):
    min = array[0]
    max = array[0]
    for i in range(0, n):

        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]

    return min, max

array = [55,22,11,66,33,99]
n = len(array)
print("Minimum element of array:", getMinMax(array,n))