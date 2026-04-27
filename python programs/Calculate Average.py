def calculate_average(numbers):
    # Check if the list is empty to avoid an error
    if len(numbers) == 0:
        return 0

    # Sum all numbers and divide by the count
    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return average


# Example usage:
my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)

print(f"The average is: {result}")
# Output: 30.0