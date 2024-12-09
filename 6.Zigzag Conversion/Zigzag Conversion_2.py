class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)

        if numRows == 1 or numRows > length:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]
        
        period = [(2*n-2) for n in range(numRows,1,-1)]
        out = ''
        
        # row 1
        id = 0
        while id < length:
            out += s[id]
            id += period[0]

        # row 2 to n-1
        for row in range(1, numRows-1):
            id = row
            while id < length:
                out += s[id]
                if (id + period[row]) < length:
                    out += s[id + period[row]]
                else:
                    break
                id += period[0]

        # row n
        id = numRows - 1
        while id < length:
            out += s[id]
            id += period[0]
            
        return out