class Solution:
    def revStr(self, s: str) -> str:
        return s[::-1]


# Input
text = "Jenkins"

print("Running Reverse String Program")
print("Input String:", text)

obj = Solution()

result = obj.revStr(text)

print("Reversed String:", result)
