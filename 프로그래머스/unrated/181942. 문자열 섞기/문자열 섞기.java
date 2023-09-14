import java.util.*;

class Solution {
    public String solution(String str1, String str2) {
        StringBuffer sb = new StringBuffer();
        for(int i=0, j=0 ; i<str1.length(); i++,j++){
            sb.append(str1.charAt(i));
            sb.append(str2.charAt(j));
        }
        return sb.toString();
    }
}