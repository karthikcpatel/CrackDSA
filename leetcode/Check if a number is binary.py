def is_binary(num):
    """
    Check if a number contains only binary digits (0 and 1)
    """
    while num > 0:
        digit = num % 10
        if digit != 0 and digit != 1:
            print("num is not binary")
            return False
        num = num // 10

    print("num is binary")
    return True


# Usage example:
number = int(input("Enter the number: "))
is_binary(number)