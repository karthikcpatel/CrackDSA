#Google #Microsoft #Amazon #Accolite

class KAnagramChecker:

    def are_k_anagrams(self, str1, str2, k):

        # Length mismatch check
        if len(str1) != len(str2):
            return False

        count = 0

        # Count matching characters
        for i in range(len(str1)):

            if str1[i] in str2:

                count += 1

                # Remove matched character
                str2 = str2.replace(str1[i], '', 1)

        # Check if remaining unmatched chars <= k
        if len(str1) - count <= k:
            return True

        return False


str1 = "anagram"
str2 = "grammar"

k = 2

obj = KAnagramChecker()

if obj.are_k_anagrams(str1, str2, k):
    print("Yes")
else:
    print("No")