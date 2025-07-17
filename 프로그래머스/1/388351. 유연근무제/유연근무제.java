class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = schedules.length;
        int sat = (6 - startday + 7) % 7;
        int sun = (7 - startday + 7) % 7;
        
        for (int i = 0; i < schedules.length; i++) {
            int time = (schedules[i] / 100) * 60 + (schedules[i] % 100) + 10;
            schedules[i] = time;
        }
        
        
        for (int i = 0; i < timelogs.length; i++) {
            for (int j = 0; j < timelogs[0].length; j++) {
                if (j % 7 == sat || j % 7 == sun) {
                    continue;
                }
                int time = (timelogs[i][j] / 100) * 60 + (timelogs[i][j] % 100);
                if (time > schedules[i]) {
                    --answer;
                    break;
                }
            }
        }
        return answer;
    }
}