
def max_sum_index(nums):

    for num in nums:
        max_sum = float("-inf")
        cur_sum = float("-inf")
        cs = 0
        ce = 0
        bs = -1
        be = -1
        for i, n in enumerate(num):
            if n > cur_sum+n:
                cur_sum = n
                cs = i
                ce = i
            else:
                cur_sum = cur_sum+n
                ce = i
            if cur_sum > max_sum:
                max_sum = cur_sum
                bs = cs
                be = ce
        print(max_sum, bs, be)


# min sub array sum
def min_sum_subarray(nums):

    for num in nums:
        min_sum = float("inf")
        cur_sum = float("inf")
        for n in num:
            cur_sum = min(n, cur_sum+n)
            min_sum = min(cur_sum, min_sum)
        print(min_sum)


# max sub array sum
def max_sum_subarray(nums):

    for num in nums:
        max_sum = float("-inf")
        cur_sum = float("-inf")
        for n in num:
            cur_sum = max(n, cur_sum+n)
            max_sum = max(cur_sum, max_sum)
        print(max_sum)


if __name__ == '__main__':
    nums = [
        [-9, 10, -1, 2, -10, 8], #11 -10
        [1, 2, 3, 4], #10 1
        [-3, -2, -1, -4, -5], #-1 -15
        [-3, -2, -1, 0, -5], #0 -11
        [-4, 2, -6], #2 -8
    ]

    max_sum_subarray(nums)
    print("----")
    min_sum_subarray(nums)
    print("----")
    max_sum_index(nums)
