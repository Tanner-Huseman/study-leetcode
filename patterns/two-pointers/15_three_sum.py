class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            # skip duplicate values for the fixed element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                jval = nums[j]
                kval = nums[k]
                jkval = nums[j] + nums[k]

                if jkval == target:
                    output.append([nums[i], nums[j], nums[k]])
                    # advance past duplicates on both sides
                    while jval == nums[j] and j < k:
                        j += 1
                    while kval == nums[k] and j < k:
                        k -= 1
                elif jkval < target:
                    while jval == nums[j] and j < k:
                        j += 1
                else:
                    while kval == nums[k] and j < k:
                        k -= 1

        return output
