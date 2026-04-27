class SortArray:

    def sort_array(self,arr):

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        return arr


arr = [5, 2, 8, 4, 7, 9, 3, 6, 1]
# sorted_array = sort_array(arr)
# print(sorted_array)
obj = SortArray()
x = obj.sort_array(arr)
print(x)