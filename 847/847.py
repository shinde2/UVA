
def main():

    with open("inputs.txt") as inf:
        lines = inf.readlines()

    with open("outputs.txt", "w") as outf:
        for line in lines:
            n = int(line.strip())
            count = 1
            num = 9
            while n > num:
                if count % 2 == 1:
                    num *= 2
                else:
                    num *= 9
                count += 1

            if count % 2 == 1:
                outf.write("Stan wins.\n")
            else:
                outf.write("Ollie wins.\n")


if __name__ == '__main__':
    main()
