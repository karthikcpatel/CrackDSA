def average_word_length(sentence):
    words = sentence.split()
    total_length = 0

    for word in words:
        word_length = len(word)
        total_length = total_length + word_length

    if len(words) == 0:
        return 0

    return total_length / len(words)

# Example usage
text = "I love Python programming"
avg_length = average_word_length(text)

print("Average word length:", avg_length)
