class RightRotateArray:

    def rotate(self, arr):

        n = len(arr)

        # Store last element
        temp = arr[n - 1]

        i = n - 1

        # Shift elements to the right
        while i > 0:

            arr[i] = arr[i - 1]

            i = i - 1

        # Place last element at first position
        arr[0] = temp

        return arr


arr = [9, 8, 7, 6, 4, 2, 1, 3]

obj = RightRotateArray()
output = obj.rotate(arr)
print(output)