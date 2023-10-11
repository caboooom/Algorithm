class Solution {
    public int[][] solution(int[][] arr) {
        int len = Math.max(arr.length, arr[0].length);
        int[][] answer = new int[len][len];
        
        for(int i=0; i<len; i++){
            for(int j=0; j<len; j++){
                if (i >= arr.length || j >= arr[0].length) answer[i][j] = 0;
                else answer[i][j] = arr[i][j];
            }
        }
        return answer;
    }
}