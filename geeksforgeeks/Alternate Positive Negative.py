#Amazon #Paytm #VMWare #Microsoft #Intuit

class AlternatePositiveNegative:

    def rearrange(self, arr):

        n = len(arr)

        negative = []
        positive = []

        # Separate positive and negative numbers
        for i in range(n):

            if arr[i] < 0:
                negative.append(arr[i])

            else:
                positive.append(arr[i])

        i = 0
        j = 0
        k = 0

        # Arrange alternatively
        while i < len(negative) and j < len(positive):

            if k % 2 == 0:
                arr[k] = positive[j]
                j += 1

            else:
                arr[k] = negative[i]
                i += 1

            k += 1

        # Add remaining positive elements
        while j < len(positive):
            arr[k] = positive[j]
            j += 1
            k += 1

        # Add remaining negative elements
        while i < len(negative):
            arr[k] = negative[i]
            i += 1
            k += 1

        return arr

arr = [-5, -2, 5]

obj = AlternatePositiveNegative()
output = obj.rearrange(arr)
print(output)