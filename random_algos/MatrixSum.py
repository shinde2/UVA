# print sum between matrix (1, 1) and (x, y)


def init_dp(M):

    m = len(M)
    n = len(M[0])

    dp = [[0 for _ in range(0, n)] for _ in range(0, m)]

    dp[0][0] = M[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + M[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + M[i][0]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + M[i][j]

    return dp


def main():

    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    dp = init_dp(M)

    print(dp[2][2])
    print(dp[1][2])


if __name__ == '__main__':
    main()
