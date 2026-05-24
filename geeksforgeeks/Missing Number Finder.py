#Adobe #Aamzon #Cisco #Intuit #Microsoft #Morgan Stanley #Ola Cabs #PayU #Qualcomm #Visa #Flipkart

class MissingNumberFinder:

    def find_missing_number(self, arr):

        # Total numbers should be len(arr) + 1
        n = len(arr) + 1

        # Expected sum from 1 to n
        total = n * (n + 1) // 2

        # Actual array sum
        actual_sum = sum(arr)

        # Missing number
        missing = total - actual_sum

        return missing


arr = [5, 2, 4, 3, 6, 7, 8, 9]

obj = MissingNumberFinder()

result = obj.find_missing_number(arr)
print("The missing number is:", result)