#Abode #Amazon #Hike #MakeMyTrip #Microsoft #Morgan Stanley #Ola Cabs
#Snapdeal #Qualcomm #Yatra #Paytm #SAP Labs #Walmart #Flipkart #OYO Rooms

class DutchNationalFlag:

    def sort_012(self, arr):

        lo = 0
        mid = 0
        hi = len(arr) - 1

        while mid <= hi:

            # If element is 0
            if arr[mid] == 0:

                arr[lo], arr[mid] = arr[mid], arr[lo]

                lo += 1
                mid += 1

            # If element is 1
            elif arr[mid] == 1:

                mid += 1

            # If element is 2
            else:

                arr[mid], arr[hi] = arr[hi], arr[mid]

                hi -= 1

        return arr


arr = [0, 1, 1, 2, 2]

obj = DutchNationalFlag()
output = obj.sort_012(arr)
print("Array after sorting:", output)
