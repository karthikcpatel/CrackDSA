def get_most_frequent_words(text):
    """
    Identifies the word(s) with the highest occurrence in a string.
    Returns a list of winners and their count.
    """
    # 1. Normalize and split
    word_list = text.lower().split()
    word_counts = {}

    # 2. Count occurrences
    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] = word_counts[word] + 1

    # 3. Find the highest number of repetitions
    max_value = max(word_counts.values())

    # 4. Extract ALL words that have that max value
    winners = []
    for word, count in word_counts.items():
        if count == max_value:
            winners.append(word)

    return winners, max_value


# --- Execution ---
input_string = "My name is Kartik and my hometown is Navsari"
most_frequent, count = get_most_frequent_words(input_string)

print(f"The most occurring words are: {', '.join(most_frequent)}")
print(f"They are repeated {count} times each.")