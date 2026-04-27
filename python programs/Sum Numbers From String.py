def sum_numbers_in_string(input_string):
    """
    Finds all numbers within a string (even multi-digit ones) 
    and returns their total sum.
    """
    temp = "0"
    total_sum = 0

    for ch in input_string:
        if ch.isdigit():
            # Build the multi-digit number as a string
            temp = temp + ch
        else:
            # We hit a letter, so convert the built number and add to sum
            total_sum = total_sum + int(temp)
            temp = "0"

    # Add the last remaining 'temp' in case the string ends with a number
    return total_sum + int(temp)


# Example usage:
my_string = "12abc20yz68"
result = sum_numbers_in_string(my_string)

print(f"The sum of numbers in the string is: {result}")
# Calculation: 12 + 20 + 68 = 100