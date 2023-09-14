import java.util.*;

class Solution {
    public int solution(int n) {
        List<Boolean> numbers = new ArrayList<>(n+1);
        numbers.add(false); // 0은 소수가 아님
        numbers.add(false); // 1은 소수가 아님
        for(int i=2; i<=n; i++){
            numbers.add(true);
        }
        
        for(int i=2; i*i<=n; i++){
            if (numbers.get(i)){
                for(int j=i*2; j<=n; j+=i) numbers.set(j,false);
            }
        }
        
        int answer = 0;
        for(int i=2; i<=n; i++){
            if (numbers.get(i)) answer++;
        }
        return answer;
    }
    

}