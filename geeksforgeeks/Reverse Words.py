#Accolite #Adobe #Amazon #Cisco #Goldman Sachs #MakeMyTrip # Microsoft #Paytm
# paytm #Samsung #SAP Labs

class ReverseWords:

    def reverse_words(self, s):

        # Split sentence into words
        list_of_words = s.split(".")

        # Reverse word list
        rev_list = list_of_words[::-1]

        # Join reversed words
        rev_sentence = ".".join(rev_list)

        return rev_sentence


obj = ReverseWords()

output = obj.reverse_words("i.like.this.program.very.much")
print(output)