class ShortestWordDistance:

    def shortest_distance(self, s, word1, word2):

        pos1 = -1
        pos2 = -1

        minimum = float('inf')

        for i in range(len(s)):

            if s[i] == word1:
                pos1 = i

            if s[i] == word2:
                pos2 = i

            if pos1 != -1 and pos2 != -1:
                minimum = min(minimum, abs(pos1 - pos2))

        return minimum


s = ["the", "quick", "brown", "fox", "quick"]

word1 = "the"
word2 = "fox"

obj = ShortestWordDistance()
output = obj.shortest_distance(s, word1, word2)
print(output)