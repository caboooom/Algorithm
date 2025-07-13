import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        long left = diffs[0];
        long right = 100000;
        
        long answer = Long.MAX_VALUE;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long time = 0;
            for (int i = 0; i < diffs.length; i++) {
                time += times[i];
                if (diffs[i] > mid && i > 0) {
                    time += (times[i] + times[i-1]) * (diffs[i] - mid);
                }
            }
            if (time <= limit) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
                
            }
        }
        return (int)answer;
    }
}