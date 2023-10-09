class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        
        int direction = 0;
        int[] dx = new int[]{0,1,0,-1};
        int[] dy = new int[]{1,0,-1,0};
        
        int curNum = 1;
        int row=0; int col=0;
        
        while (true){
            
            answer[row][col] = curNum++;
            if(curNum > n*n) break;
            
            int nextRow = row + dx[direction%4];
            int nextCol = col + dy[direction%4];
            
            if(nextRow < 0 || nextRow >= n || nextCol<0 || nextCol >= n
              || answer[nextRow][nextCol] > 0){
                // change direction
                direction++;
                curNum--;
            }else{
                row = nextRow;
                col = nextCol;
            }  
        }
        return answer;
    }
}