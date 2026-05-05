class StringFilter:

    @staticmethod
    def extract_alphabets(string):
        result = ""
        for ch in string:
            if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
                result += ch
        return result


print(StringFilter.extract_alphabets("$%$kar123*^%ik"))