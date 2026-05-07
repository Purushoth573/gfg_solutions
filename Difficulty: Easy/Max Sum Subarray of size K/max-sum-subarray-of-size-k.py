class Solution:
    def maxSubarraySum(self, arr, k):
        l = 0
        res = 0
        cursum = 0

        for r in range(len(arr)):
            cursum += arr[r]
            res = max(res, cursum)

            while r - l + 1 >= k:
                cursum -= arr[l]
                l += 1

        return res


# Input
arr = [2, 1, 5, 1, 3, 2]
k = 3

print("Running Maximum Subarray Sum Program")
print("Input Array:", arr)
print("Window Size:", k)

obj = Solution()

result = obj.maxSubarraySum(arr, k)

print("Maximum Subarray Sum:", result)
