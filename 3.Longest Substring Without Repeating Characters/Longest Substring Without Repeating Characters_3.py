#Using list as a substituition compared to Longest Substring Without Repeating Characters_2.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = [-1]*127
        
        for i in range(len(s)):
            index=ord(s[i])
            if usedChar[index] !=-1 and start <= usedChar[index]:
                start = usedChar[index] + 1
            else:
                maxLength = max(maxLength,i - start + 1)
            usedChar[index] = i
        return maxLength