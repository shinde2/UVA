
def solution_found(output, n):

    if len(output) == n:
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

    return [file for file in files if file not in output[0:k]]


def check_files(files, output, k, n):

    if solution_found(output, n):
        print(output)
    else:
        k += 1
        possibilities = get_possibilities(files, output, k)
        for possibility in possibilities:
            try:
                output[k] = possibility
            except:
                output.append(possibility)
            check_files(files, output, k, n)


def main():

    files = [
        "011",
        #"0111",
        "01110",
        "111",
        #"0111",
        "10111"
    ]

    output = list()
    k = -1

    check_files(files, output, k, len(files))


if __name__ == '__main__':
    main()
