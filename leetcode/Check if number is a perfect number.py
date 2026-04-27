def is_perfect_number(num):
    """
    Check if a number is a perfect number.
    A perfect number equals the sum of its proper divisors.
    """
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print("The given no is perfect number")
        return True
    else:
        print("The given no is not a perfect number")
        return False


# Usage example:
number = int(input("please give first number a: "))
is_perfect_number(number)