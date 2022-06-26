class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, l, r, k):
            if l == k or l >= r:
                return

            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[l] = nums[l], nums[pivot_idx]
            
            i = l+1
            j = r
            
            while i < j:
                while i < j and nums[i] >= pivot:
                    i += 1
                while i < j and nums[j] <= pivot:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]

            if nums[i] < pivot:
                i -= 1
            nums[l], nums[i] = nums[i], nums[l]
            
            if i+1 <= k:
                quick_select(nums, i+1, r, k)
            else:
                quick_select(nums, l, i-1, k)
    
        quick_select(nums, 0, len(nums)-1, k)

        return nums[k-1]
