#Accolite #Adobe #Amazon #Cisco #Goldman Sachs #MakeMyTrip # Microsoft #Paytm
# paytm #Samsung #SAP Labs

def reverseWords(s):
    list_of_words = s.split(".")
    rev_list = list_of_words[::-1]
    rev_sentence = " ".join(rev_list)
    return rev_sentence

# Fix: Print the result
print(reverseWords("i.like.this.program.very.much"))