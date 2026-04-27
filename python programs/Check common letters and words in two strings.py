def common_letters_and_words(str1, str2):
    # Convert to lowercase for case-insensitive comparison
    str1 = str1.lower()
    str2 = str2.lower()

    # --- Common Letters ---
    letters1 = set(str1.replace(" ", ""))
    letters2 = set(str2.replace(" ", ""))
    common_letters = letters1.intersection(letters2)

    # --- Common Words ---
    words1 = set(str1.split())
    words2 = set(str2.split())
    common_words = words1.intersection(words2)

    return common_letters, common_words


# Example usage
s1 = "I love Python programming"
s2 = "Python is love and fun"

letters, words = common_letters_and_words(s1, s2)

print("Common Letters:", letters)
print("Common Words:", words)