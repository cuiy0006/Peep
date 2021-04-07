
def quick_sort(nums, l, r):
    if l >= r:
        return
    pivot = nums[l]
    left = l + 1
    right = r
    while left < right:
        while left < right and nums[left] <= pivot:
            left += 1
        while left < right and nums[right] >= pivot:
            right -= 1

        nums[left], nums[right] = nums[right], nums[left]

    if nums[left] > pivot:
        left -= 1
    nums[left], nums[l] = nums[l], nums[left]

    quick_sort(nums, l, left - 1)
    quick_sort(nums, left + 1, r)


if __name__ == '__main__':
    nums = [1, 4, 5, 2, 1, 2, 10, 100, 2, 5, 8, 0, 33]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)