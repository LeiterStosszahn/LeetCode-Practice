class Solution {
    public String convert(String s, int numRows) {
        int length = s.length();
        if(numRows == 1 || numRows >= length) {
            return s;
        }
        else if(numRows == 2) {
            StringBuilder out = new StringBuilder();
            for(int i = 0; i < length; i += 2) {
                out.append(s.charAt(i));
            }
            for(int i = 1; i < length; i += 2) {
                out.append(s.charAt(i));
            }
            return out.toString();
        }

        int[] period = new int[numRows - 1];
        int n = numRows, i = 0;
        while(n > 1) {
            period[i] = (n << 1) - 2;
            n--;
            i++;
        }
        
        StringBuilder out = new StringBuilder();

        // row 1
        int id = 0;
        while(id < length) {
            out.append(s.charAt(id));
            id += period[0];
        }

        // row 2
        for(int row = 1; row < numRows - 1; row++) {
            id = row;
            while(id < length) {
                out.append(s.charAt(id));
                if((id + period[row]) < length) {
                    out.append(s.charAt(id + period[row]));
                } else {
                    break;
                }
                id += period[0];
            }
        }

        // row n
        id = numRows - 1;
        while(id < length) {
            out.append(s.charAt(id));
            id += period[0];
        }

        return out.toString();
    }
}