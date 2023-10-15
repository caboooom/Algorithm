import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        Map<Integer, Integer> m = new HashMap<>();
        
        for(int i=0; i<rank.length; i++){
            if (attendance[i]){
                if (m.size() < 3){
                    m.put(rank[i],i);
                }
                else if (rank[i] < Collections.max(m.keySet())){
                    m.remove(Collections.max(m.keySet()));
                    m.put(rank[i], i);
                } 
            }
        }
        
        List<Integer> keySet = new ArrayList<>(m.keySet());
        Collections.sort(keySet);
        answer += 10000 * (m.get(keySet.get(0)));
        answer += 100 * (m.get(keySet.get(1)));
        answer += 1 * (m.get(keySet.get(2)));
        
        
        return answer;
    }
}