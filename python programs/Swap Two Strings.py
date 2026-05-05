class SwapStrings:

    def swap_string(self, string1, string2):

        len1 = len(string1)  # Save original length = 6
        len2 = len(string2)  # Save original length = 5

        string1 = string1 + string2        # "KartikPatel"
        string2 = string1[0:len1]          # "Kartik" ✅
        string1 = string1[len1:]           # "Patel"  ✅

        return string1, string2

obj = SwapStrings()
print(obj.swap_string("Kartik", "Patel"))  # ('Patel', 'Kartik')