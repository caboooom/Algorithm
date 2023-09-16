import java.util.*;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> result = new ArrayList<>();        
        for(int i=2; i<=n; i++){
            if (n%i==0){
                result.add(i);
                n /= i;
            }
            while(n%i==0) {
                n /= i;
            }
        }
        
        int[] answer = new int[result.size()];
        for(int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
 
    


        return answer;
    }
}