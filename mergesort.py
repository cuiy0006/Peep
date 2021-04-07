
def merge_sort(nums, l, r):
    if l >= r:
        return nums
    left = []
    right = []
    pivot = nums[l]
    i = l + 1
    while i <= r:
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
        i += 1

    return merge_sort(left, 0, len(left) - 1) + [pivot] + merge_sort(right, 0, len(right) - 1)

if __name__ == '__main__':
    nums = [1, 4, 5, 2, 1, 2, 10, 100, 2, 5, 8, 0, 33]
    res = merge_sort(nums, 0, len(nums) - 1)
    print(res)