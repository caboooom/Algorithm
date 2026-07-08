import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        int oldValue = -1;
        
        for (int num : arr) {
            if (num != oldValue) {
                answer.add(num);
                oldValue = num;
            }
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}