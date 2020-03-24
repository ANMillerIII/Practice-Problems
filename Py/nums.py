class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        for num in nums:
            if val in nums:
                nums.remove(val)
        if val in nums:
            nums.remove(val)
        print(nums)
        return len(nums)
Solution.removeElement(None,[3,3],3)