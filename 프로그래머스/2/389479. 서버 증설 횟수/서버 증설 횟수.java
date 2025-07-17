class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] servers = new int[players.length];
        
        for (int i = 0; i < players.length; i++) {
            int serverNum = players[i] / m;
            if (servers[i] < serverNum) {
                int needs = serverNum - servers[i];
                answer += needs;
                int j = i;
                while (j < players.length && j < i + k) {
                    servers[j] += needs;
                    j++;
                }
            }
        }
        return answer;
    }
}