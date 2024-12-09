class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring=""
        i=0
        strlen=len(s)
        while i<strlen:
            sublen=len(substring)
            substring1=""
            for j in range(i,strlen):
                if s[j] not in substring1:
                    substring1+=s[j]
                else:
                    break
            substring=substring1 if j-i+1>sublen else substring
            i+=1
            if i+len(substring)>strlen:
                break
        return len(substring)