class ReverseWordsClass:

    def reverse_words(self, string):

        # Step 1: Split the string into words using '.'
        words = string.split(".")
        # Example:
        # "i.like.this.program.very.much"
        # becomes:
        # ['i', 'like', 'this', 'program', 'very', 'much']

        # Step 2: Reverse the order of words
        reversed_words = words[::-1]
        # becomes:
        # ['much', 'very', 'program', 'this', 'like', 'i']

        # Step 3: Reverse each word individually
        reversed_each_word = []

        for word in reversed_words:
            reversed_word = word[::-1]
            reversed_each_word.append(reversed_word)

        # becomes:
        # ['hcum', 'yrev', 'margorp', 'siht', 'ekil', 'i']

        # Step 4: Join the reversed words using '.'
        final_string = ".".join(reversed_each_word)

        # Final output:
        # "hcum.yrev.margorp.siht.ekil.i"

        return final_string


# Input string
string = "i.like.this.program.very.much"

# Create object
obj = ReverseWordsClass()

# Call method
output = obj.reverse_words(string)

# Print output
print(output)