from math import floor

arr = [1, 1, 2, 4, 4, 6, 7, 8, 8, 8, 9, 10, 11, 11]


def lower_bound(low, high, k):

    if low > high:
        return low

    mid = floor((low + high) / 2)

    if k > arr[mid]:
        return lower_bound(mid+1, high, k)
    else:
        return lower_bound(low, mid-1, k)


def upper_bound(low, high, k):

    if low > high:
        return low

    mid = floor((low + high) / 2)

    if k < arr[mid]:
        return upper_bound(low, mid-1, k)
    else:
        return upper_bound(mid+1, high, k)


def main():

    k = 5

    print(lower_bound(0, len(arr)-1, k))
    print(upper_bound(0, len(arr)-1, k))


if __name__ == '__main__':
    main()
