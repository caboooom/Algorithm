import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        
        HashMap<String, Integer> rank = new HashMap<String, Integer>();
        HashMap<Integer, String> name = new HashMap<Integer, String>();
        
        for(int i=0; i<players.length; i++){
            rank.put(players[i], i);
            name.put(i, players[i]);
        }
        
        for(int i=0; i<callings.length; i++){
            Integer newRank = rank.get(callings[i]) - 1;
            String next = name.get(newRank);
            rank.put(callings[i], newRank);
            rank.put(next, newRank+1);
            name.put(newRank, callings[i]);
            name.put(newRank+1, next);
        }
        
        for(String str:rank.keySet()){
            answer[rank.get(str)] = str;
        }
        
        return answer;
    }
}