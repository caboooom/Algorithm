import java.util.*;
class Solution {
    public int[] solution(int[] sequence, int k) {
        long[] sum = new long[sequence.length + 1];
        for (int i = 1; i <= sequence.length; i++) {
            sum[i] = sequence[i-1] + sum[i-1];
        }
        int[] answer = new int[2];
        answer[1] = Integer.MAX_VALUE;
        
        int x = 1;
        int y = 1;
        while (x < sum.length) {
            if (y >= sum.length) {
                ++x;
                continue;
            }
            long val = sum[y] - sum[x-1];
            if (val > k) {
                ++x;
            } else if (val == k) {
                if (y - x < answer[1] - answer[0]) {
                    answer[0] = x - 1;
                    answer[1] = y - 1;
                }
                ++x;
            } else {
                ++y;
            }
        }
        
        return answer;
    }
}