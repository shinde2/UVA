from collections import deque

# num: 48 to 57
# char: 65 to 122


def compare(inputs, outputs, run):

    input_num = list()
    output_num = list()
    input_char = list()
    output_char = list()
    A = f"Run #{run}: Accepted"
    WA = f"Run #{run}: Wrong Answer"
    PE = f"Run #{run}: Presentation Error"

    if len(inputs) != len(outputs):
        print(WA)
        return
    pe = False

    for index, i in enumerate(inputs):
        input = i
        output = outputs[index]

        if input == output:
            continue
        else:
            for c in input:
                if 65 <= ord(c) <= 122:
                    input_char.append(c)
                elif 48 <= ord(c) <= 57:
                    input_num.append(c)
            for c in output:
                if 65 <= ord(c) <= 122:
                    output_char.append(c)
                elif 48 <= ord(c) <= 57:
                    output_num.append(c)
            if input_char != output_char:
                print(WA)
                return
            elif input_num != output_num:
                print(WA)
                return
            else:
                pe = True
    else:
        if pe:
            print(PE)
        else:
            print(A)


def main():

    run = 1

    with open("tests.txt") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines)-1:
        num = int(lines[i].rstrip())
        ins = lines[i+1:i+num+1]
        i = i + num + 1
        num = int(lines[i].rstrip())
        outs = lines[i+1:i+num+1]
        compare(ins, outs, run)
        i = i + num + 1
        run += 1


if __name__ == '__main__':
    main()
