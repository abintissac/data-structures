class DuplicateRemover:

    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i + 1
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
duplicate_remover = DuplicateRemover()
result = duplicate_remover.removeDuplicates(nums)
print(result)
