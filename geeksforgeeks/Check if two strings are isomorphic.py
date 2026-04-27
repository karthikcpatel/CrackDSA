def are_isomorphic(str1, str2):
    # Check length mismatch
    if len(str1) != len(str2):
        return False

    # Check one-to-one mapping in both directions
    return (
        len(set(zip(str1, str2))) == len(set(str1)) ==
        len(set(str2))
    )


# Example usage
if __name__ == "__main__":
    s1 = "aab"
    s2 = "xxy"

    if are_isomorphic(s1, s2):
        print("Isomorphic")
    else:
        print("Not isomorphic")