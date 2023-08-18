class Solution {
    public String solution(String[] arr) {
        StringBuffer result = new StringBuffer();
        for (int i=0; i<arr.length; i++) {
            result.append(arr[i]);
        }
        return result.toString();
    }
}