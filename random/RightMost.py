import math


def SetBit(n):

   return math.log2(n & -n)


def UnsetBit(n):

    return SetBit(~n)


def RightMostUnset(n, N):

    lst = []

    if n == 0:
        return [i for i in range(N)]
    else:
        pos = 0
        while N:
            if not (n & 1):
                lst.append(pos)
            pos += 1
            n = n >> 1
            N -= 1

        return lst


if __name__ == '__main__':

    print(RightMostUnset(4, 3))
