def remove_duplicates(input_list):
    """
    Takes a list and returns a new list with 
    duplicate elements removed, preserving order.
    """
    temp_list = []

    for item in input_list:
        if item not in temp_list:
            temp_list.append(item)

    return temp_list


# Example usage:
kp_list = [1, 2, 3, 1, 2, 4, 5, 4, 6, 2]
print("Original List:", kp_list)

# Call the function and store the result
cleaned_list = remove_duplicates(kp_list)

print("List after removing duplicates:", cleaned_list)
# Output: [1, 2, 3, 4, 5, 6]