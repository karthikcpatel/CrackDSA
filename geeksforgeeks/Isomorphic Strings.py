class IsomorphicStrings:

    def are_isomorphic(self, str1, str2):

        # Check length mismatch
        if len(str1) != len(str2):
            return False

        # Check one-to-one mapping
        return (
            len(set(zip(str1, str2))) ==
            len(set(str1)) ==
            len(set(str2))
        )


s1 = "aab"
s2 = "xxy"

obj = IsomorphicStrings()

if obj.are_isomorphic(s1, s2):
    print("Isomorphic")
else:
    print("Not Isomorphic")