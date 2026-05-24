#Google

class MinimumStringRepeats:

    def min_repeats(self, A, B):

        repeated = A

        count = 1

        while len(repeated) < len(B):

            repeated += A

            count += 1

        if B in repeated:
            return count

        repeated += A

        if B in repeated:
            return count + 1

        return -1


A = "abcd"
B = "cdabcdab"

obj = MinimumStringRepeats()
print(obj.min_repeats(A, B))