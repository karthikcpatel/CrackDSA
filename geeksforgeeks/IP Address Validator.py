class IPv4Validator:

    def is_valid(self, s):

        # Check invalid dot patterns
        if '..' in s or s.count('.') != 3:
            return False

        # Split using dot
        parts = s.split('.')

        # Must contain exactly 4 parts
        if len(parts) != 4:
            return False

        for part in parts:

            # Check alphabetic characters
            if part.isalpha():
                return False

            # Prevent leading zeros
            if part != str(int(part)):
                return False

            # Range check
            if int(part) not in range(0, 256):
                return False

        return True


s = "192.168.1.1"

obj = IPv4Validator()

if obj.is_valid(s):
    print("Valid IP")
else:
    print("Invalid IP")