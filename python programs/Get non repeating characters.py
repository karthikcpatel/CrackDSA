def get_unique_chars(string):
    new_string = ""
    for char in string:
        # If the character appears only once in the whole string, keep it
        if string.count(char) == 1:
            new_string = new_string + char
        else:
            # If it appears more than once (like 'k'), we skip it entirely
            pass

    return new_string


# To get 'arti', we use 'kartik'
# 'k' appears twice, so it is removed.
# 'a', 'r', 't', 'i' appear once, so they stay.
original_word = "KARtik".lower()
x = get_unique_chars(original_word)
print(x)