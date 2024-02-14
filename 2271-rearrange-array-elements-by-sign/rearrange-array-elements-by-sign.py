class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        main_arr = []
        negative_value = []
        postitive_value = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_value.append(nums[i])

            else:
                postitive_value.append(nums[i])
        merged_array = [val for pair in zip(postitive_value, negative_value) for val in pair]

        return merged_array