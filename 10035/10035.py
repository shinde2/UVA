
class BigNum:

    def __init__(self, digits=0, maxdigits=5):
        self.MAXDIGITS = maxdigits
        self.digits = [0] * self.MAXDIGITS
        self.sign = "-" if digits < 0 else "+"
        self.lastdigit = len(list(map(int, str(digits)))) - 1
        for i, num in enumerate(list(map(int, str(digits)))[::-1]):
            self.digits[i] = num

    def __repr__(self):
        for i, n in enumerate(self.digits):
            if n != 0:
                break
        else:
            num = 0
        if n != 0:
            num = "".join(map(str, self.digits[:self.lastdigit+1][::-1]))
            return f"{self.sign}{num}"
        else:
            return f"{num}"


def check_carry(a, b):

    if a == 0 and b == 0:
        return

    a = BigNum(a, 10)
    b = BigNum(b, 10)

    count = 0
    carry = 0

    for i in range(max(a.lastdigit, b.lastdigit)+1):
        if a.digits[i] + b.digits[i] + carry > 9:
            count += 1
            carry = 1
        else:
            carry = 0

    s = str(count) if count else "No"

    print(f"{s} carry operations.") if count > 1 else print(f"{s} carry operation.")


def main():

    with open("inputs.txt") as f:
        lines = f.readlines()

    for line in lines:
        check_carry(*list(map(int, line.strip().split())))


if __name__ == '__main__':
    main()
