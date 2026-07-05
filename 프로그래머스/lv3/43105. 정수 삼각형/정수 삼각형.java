class Solution {
    public int solution(int[][] triangle) {
        int answer = triangle[0][0];
        int[][] dp = new int[triangle.length][triangle.length];
        
        dp[0][0] = triangle[0][0];
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 0; j < triangle[i].length; j++) {
                int temp = 0;
                if (j > 0) {
                    temp = dp[i-1][j-1];
                }
                if (j < triangle[i].length - 1) {
                    temp = Integer.max(temp, dp[i-1][j]);
                }
                dp[i][j] = temp + triangle[i][j];
                answer = Integer.max(answer, dp[i][j]);
            }
            
        }
        
        return answer;
    }
}
