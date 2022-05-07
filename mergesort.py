def merge_sort(nums, l, r):
    if l == r:
        return [nums[l]]

    mid = (l + r) // 2
    left = merge_sort(nums, l, mid)
    right = merge_sort(nums, mid+1, r)

    i = 0
    j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    
    while i < len(left):
        res.append(left[i])
        i += 1
    
    while j < len(right):
        res.append(right[j])
        j += 1

    return res

if __name__ == '__main__':
    nums = [1, 4, 5, 2, 1, 2, 10, 100, 2, 5, 8, 0, 33]
    res = merge_sort(nums, 0, len(nums) - 1)
    print(res)
