# tests passed

def crypt(input, plain, possible_plain):

    mapped = dict()
    plain = "".join(plain)
    possible_plain = "".join(possible_plain)

    for i in range(0, len(plain)):
        mapped.setdefault(possible_plain[i], plain[i])
    po = []
    for i in input:
        o = ""
        i = " ".join(i)
        for c in i:
            if c != " ":
                if c not in mapped.keys():
                    break
                o += mapped[c]
            else:
                o += " "
        else:
            po.append(o)
        if not po:
            return None
    else:
        return po


def main():

    plain = "the quick brown fox jumps over the lazy dog"
    plain = plain.split(" ")

    with open("tests.txt") as f:
        lines = f.readlines()

    all_inputs = []
    input = []
    for line in lines[2:]:
        if not line.strip():
            all_inputs.append(input)
            input = []
        else:
            input.append(line.rstrip().split(" "))
    all_inputs.append(input)

    for input in all_inputs:
        possible_plain = list()
        for i in input:
            if len(i) == len(plain):
                for j in range(0, len(plain)):
                    if len(plain[j]) != len(i[j]):
                        break
                else:
                    if i not in possible_plain:
                        possible_plain.append(i)
        if not possible_plain:
            print("No solution")
        else:
            for poss in possible_plain:
                po = crypt(input, plain, poss)
                if po:
                    for p in po: print(p)
                    break
            else:
                print("No solution")
        print("\n")


if __name__ == '__main__':
    main()
