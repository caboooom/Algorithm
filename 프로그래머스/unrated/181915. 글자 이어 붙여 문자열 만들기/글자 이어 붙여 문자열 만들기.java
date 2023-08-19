class Solution {
    public String solution(String my_string, int[] index_list) {
        
        char[] result = new char[index_list.length];
        for(int i=0; i<index_list.length; i++){
            result[i] = my_string.charAt(index_list[i]);
        }
        
        return new String(result);
    }
}