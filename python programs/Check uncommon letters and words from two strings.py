def uncommon_elements(list1, list2):
    """
    Returns elements that are present in one list but not the other.
    """
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    for i in list2:
        if i not in list1:
            result.append(i)
    # Optional: remove duplicates if needed
    return list(set(result))


# Driver Code
list1 = ["Kartik", "Chetan", "Patel"]
list2 = ["Kartik", "Chetankumar", "Patel"]

print(uncommon_elements(list1, list2))
