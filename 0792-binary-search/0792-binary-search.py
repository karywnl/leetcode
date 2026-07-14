class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_idx = 0
        high_idx = len(nums)-1

        while low_idx <= high_idx:

            mid_idx = low_idx + (high_idx - low_idx) // 2

            if target == nums[mid_idx]:
                return mid_idx

            elif target < nums[mid_idx]:
                high_idx = mid_idx - 1

            else:
                low_idx = mid_idx + 1

        return -1