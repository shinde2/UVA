# tests passed

from copy import deepcopy


def solution_found(output, k, n):

    if k == n-1:
        i = 0
        while i < n-2:
            if output[i]+output[i+1] == output[i+2]+output[i+3]:
                i += 2
            else:
                return False
        return True
    else:
        return False


def get_possibilities(files, output, k):

    posiible_files = deepcopy(files)

    for file in output[0:k]:
        posiible_files.remove(file)

    return posiible_files


def check_files(files, output, k, n):

    if solution_found(output, k, n):
        return output
    else:
        k += 1
        possibilities = get_possibilities(files, output, k)
        for possibility in possibilities:
            try:
                output[k] = possibility
            except:
                output.append(possibility)
            solun = check_files(files, output, k, n)
            if solun:
                return solun


def main():

    #files = [
    #    "011",
    #    "0111",
    #    "01110",
    #    "111",
    #    "0111",
    #    "10111"
    #]

    k = -1
    files = list()

    with open("tests.txt") as f:
        lines = f.readlines()
    lines.append("\n")

    for line in lines[2:]:
        if not line.strip():
            solutn = check_files(files, [], k, len(files))
            print("".join(solutn[0:2]))
            files = []
        else:
            files.append(line.rstrip())


if __name__ == '__main__':
    main()
