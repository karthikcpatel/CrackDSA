def count_vowels_consonants(string):
    vowels_set = set("aeiouAEIOU")
    vowels = 0
    consonants = 0

    for ch in string:
        if ch in vowels_set:
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    return vowels, consonants


# Driver Code
string = input("Enter string: ")
v, c = count_vowels_consonants(string)
print("Number of vowels are:", v)
print("Number of consonants are:", c)
