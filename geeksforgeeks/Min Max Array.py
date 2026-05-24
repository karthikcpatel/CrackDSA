class MinMaxArray:

    def get_min_max(self, array):

        minimum = array[0]
        maximum = array[0]

        for i in range(len(array)):

            if array[i] < minimum:
                minimum = array[i]

            if array[i] > maximum:
                maximum = array[i]

        return minimum, maximum


array = [55, 22, 11, 66, 33, 99]

obj = MinMaxArray()
output = obj.get_min_max(array)
print("Minimum and maximum element of array:", output)