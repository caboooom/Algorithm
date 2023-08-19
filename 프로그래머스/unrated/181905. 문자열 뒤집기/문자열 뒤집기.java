class Solution {
    public String solution(String my_string, int s, int e) {
        
        char[] result = new char[my_string.length()];
        
        for (int i=0; i<my_string.length(); i++){
            if (i<s || i>e){
                result[i] = my_string.charAt(i);
            }else if (i<=s+(e-s)/2){
                result[i] = my_string.charAt(e-i+s);
                result[e-i+s] = my_string.charAt(i);
            }
        }
        
        return new String(result);
    }
}