# Python program to print first half in 
# ascending order and the second half
# in descending order


# function to print half of the array in 
# ascending order and the other half in 
# descending order
class ArrayOrder:

    def print_order(self, arr):

        arr.sort()

        n = len(arr)

        mid = n // 2

        # First half ascending
        for i in range(mid):
            print(arr[i], end=" ")

        # Second half descending
        for j in range(n - 1, mid - 1, -1):
            print(arr[j], end=" ")


arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
obj = ArrayOrder()
obj.print_order(arr)
