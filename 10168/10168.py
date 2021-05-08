
N = 10000000
PRIMES = None


def get_primes():

    global PRIMES
    PRIMES = [True for _ in range(N+1)]

    i = 2
    while i ** 2 <= N:
        if PRIMES[i]:
            for j in range(i ** 2, N+1, i):
                PRIMES[j] = False
        i += 1


def backtrack(n, index, solution):

    global PRIMES

    if sum(solution) == n:
        return solution[:]
    else:
        index += 1
        if index < 4:
            for i in reversed(range(2, n)):
                if PRIMES[i]:
                    solution[index] = i
                    found = backtrack(n, index, solution)
                    if found:
                        return found


def SumofFour(n):

    index = -1
    solution = [-1, -1, -1, -1]

    sln = backtrack(n, index, solution)
    print(" ".join(map(str, sln)))


def main():

    get_primes()

    with open("inputs.txt") as infile:
        lines = infile.readlines()

    for line in lines:
        n = int(line.strip())
        if n < 8:
            print("Impossible.")
        else:
            SumofFour(n)


if __name__ == '__main__':
    main()
