def remove_duplicate_characters(string):
    result = []
    for char in string:
        if char not in result:
            result.append(char)
    return ''.join(result)

# Example usage
input_string = "programming"
output = remove_duplicate_characters(input_string)
print("After removing duplicate characters:", output)
# Output: "progamin"
