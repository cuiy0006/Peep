
def insertionsort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0:
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
            j -= 1


if __name__ == '__main__':
    nums = [1, 4, 5, 2, 1, 2, 10, 100, 2, 5, 8, 0, 33]
    insertionsort(nums)
    print(nums)