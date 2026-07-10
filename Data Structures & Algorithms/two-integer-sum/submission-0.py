class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}

        for i in range(len(nums)):
            j = target - nums[i] 
            k = two_sum.get(j, -1)
            if k > -1:
                if k > i:
                    return [i, k]
                else:
                    return [k, i]

            else:
                two_sum[nums[i]] = i