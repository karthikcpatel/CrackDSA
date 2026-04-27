def run_length_encoding(string):

    count = 1
    new_string = ""

    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            count = count + 1
            #new_string = new_string + string[i] + str(count)
        else:
            new_string = new_string + string[i] + str(count)
            count = 1

    new_string = new_string + string[i + 1] + str(count)
    return new_string

# Usage:
result = run_length_encoding("aabbccdaae")
print(result)