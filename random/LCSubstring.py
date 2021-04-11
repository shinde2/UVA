

def LCSubstring(s1, s2):

    index = 0
    lenght = 0
    m = len(s1)
    n = len(s2)

    dp = [[0 for _ in range(0, n+1)] for _ in range(0, m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            k = dp[i - 1][j - 1]
            if s1[i-1] == s2[j-1]:
                if i-2 >= 0 and j-2 >= 0:
                    if s1[i-2] == s2[j-2]:
                        k += 1
                else:
                    k = 1
            dp[i][j] = max(
                k,
                dp[i-1][j],
                dp[i][j-1]
            )
            if dp[i][j] > dp[i][index]:
                index = j

    lenght = dp[m][n]

    return "".join(s2[index-lenght:index])


def main():

    #s1 = "ashish"
    #s2 = "mash"

    #s1 = "abpx"
    #s2 = "abqx"

    #s1 = "abcd"
    #s2 = "xyzw"

    s1 = "abcd"
    s2 = "abcd"

    lcs = LCSubstring(list(s1), list(s2))

    print(f"Longest Common Substring: {lcs}")


if __name__ == '__main__':
    main()
