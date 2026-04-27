def number_reverse(num):

    reverse_num = 0
    while(num !=0 ):
        digit = num % 10 #8
        reverse_num = reverse_num * 10 + digit
        num = num // 10

    print(reverse_num)

num = 150688
number_reverse(num)