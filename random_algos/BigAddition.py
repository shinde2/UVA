

class BigNum:

    def __init__(self, digits=0, maxdigits=5):
        self.MAXDIGITS = maxdigits
        self.digits = [0] * self.MAXDIGITS
        self.sign = "-" if digits < 0 else "+"
        self.lastdigit = len(list(map(int, str(digits)))) - 1
        for i, num in enumerate(list(map(int, str(digits)))[::-1]):
            self.digits[self.MAXDIGITS-1-i] = num

    def __repr__(self):
        for i, n in enumerate(self.digits):
            if n != 0:
                break
        else:
            num = 0
        if n != 0:
            num = "".join(map(str, self.digits[i:]))
            return f"{self.sign}{num}"
        else:
            return f"{num}"


def BidAdd(a, b):

    c = BigNum()
    c.lastdigit = max(a.lastdigit, b.lastdigit)
    carry = 0

    i = c.MAXDIGITS - 1
    while i >= c.lastdigit:
        c.digits[i] = int(carry + a.digits[i] + b.digits[i]) % 10
        carry = int(carry + a.digits[i] + b.digits[i]) / 10
        i -= 1

    return c


def main():

    nums = [
        (323, 434),
        (100, 23),
        (12, 215),
        (2, 5),
        (0, 0)
    ]

    for a, b in nums:
        c = BidAdd(BigNum(a), BigNum(b))
        print(c)


if __name__ == '__main__':
    main()
