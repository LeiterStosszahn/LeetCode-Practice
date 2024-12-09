class Solution:
    def longestPalindrome(self, s: str) -> str:
        StrLen=len(s)
        if StrLen<=1:
            return s
        
        MaxLen=1
        MaxStr=s[0]
        for i in range(0,StrLen):
            for j in range(i+1,StrLen):
                strNow=s[i:j+1]
                if j-i+1>MaxLen and strNow==strNow[::-1] :
                    MaxLen=j-i+1
                    MaxStr=strNow
        
        return MaxStr