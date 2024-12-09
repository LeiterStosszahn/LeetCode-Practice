char* convert(char* s, int numRows) {
        int length = strlen(s);

        if(numRows == 1 || numRows >= length) {
            return s;
        }
        else if(numRows == 2) {
            char *out = (char *)malloc(sizeof(char) * (length + 1));
            int index = 0;
            for (int i = 0; i < length; i += 2) {
                out[index++] = s[i];
            }
            for (int i = 1; i < length; i += 2) {
                out[index++] = s[i];
            }
            out[length] = '\0';
            return out;
        }
        
        int period[numRows - 1];
        int n = numRows, i = 0;
        while(n > 1) {
            period[i] = (n << 1) - 2;
            n--;
            i++;
        }
        
        char *out = (char *)malloc(sizeof(char) * (length + 1));

        // row 1
        int id = 0;
        i = 0;
        while(id < length) {
            out[i] = s[id];
            i++;
            id += period[0];
        }

        // row 2 to n-1
        for(int row = 1; row < numRows - 1; row++) {
            id = row;
            while(id < length) {
                out[i] = s[id];
                i++;
                if((id + period[row]) < length) {
                    out[i] = s[id + period[row]];
                    i++;
                } else {
                    break;
                }
                id += period[0];
            }
        }

        //row n
        id = numRows - 1;
        while(id < length) {
            out[i] = s[id];
            i++;
            id += period[0];
        }

        out[i] = '\0';
            
        return out;
}