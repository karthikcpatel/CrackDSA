def median_sorted_array(array1, array2):
    merge_arrays = sorted(array1 + array2)  # ensure sorted
    n = len(merge_arrays)

    # Odd length
    if n % 2 == 1:
        return merge_arrays[n // 2]

    # Even length
    else:
        mid1 = merge_arrays[n // 2 - 1]
        mid2 = merge_arrays[n // 2]
        return (mid1 + mid2) / 2


# Example
output = median_sorted_array([1, 2, 3], [4])
print(output)