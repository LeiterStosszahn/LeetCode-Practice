class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lens = len(s)
        if numRows == 1 or numRows >= lens:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]

        oneGroup = 2 * numRows - 2
        groups = lens / oneGroup
        groups = int(groups // 1 + (groups % 1 > 0))

        strStar = strEnd = strMid = ""
        for i in range(groups):
            start = i * oneGroup
            # First row
            strStar += s[start]

            #Last row
            index = start + numRows - 1
            if index < lens:
                strEnd += s[index]

        for j in range(numRows - 2):
            for i in range(groups):
                start = i * oneGroup
                index = start + j + 1
                if index < lens:
                    strMid += s[index]
                index2 = index + 2 * (numRows - 2 - j)
                if index2 < lens:
                    strMid += s[index2]
        
        return strStar + strMid + strEnd
# PAYPALISHIRING row=5

# P     H
# A   S I
# Y  I  R
# P L   I G
# A     N