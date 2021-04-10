

def levenshtein(s1, s2):

    m = len(s1)
    n = len(s2)

    dp = [[0 for _ in range(0, n+1)] for _ in range(0, m+1)]

    # empty source string to destination string
    for j in range(1, n+1):
        dp[0][j] = j

    # source string to empty destination
    for i in range(1, m+1):
        dp[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )

    return dp[m][n]


def main():

    s1 = "sitting"
    s2 = "kitten"

    distance = levenshtein(list(s1), list(s2))

    print(distance)


if __name__ == '__main__':
    main()
