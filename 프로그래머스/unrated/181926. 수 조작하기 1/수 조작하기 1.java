import java.util.*;

class Solution {
    public int solution(int n, String control) {
        
        Map<Character, Integer> m = new HashMap<>();
        m.put('w',1);
        m.put('s',-1);
        m.put('d',10);
        m.put('a',-10);
        
        for(int i=0; i<control.length(); i++){
            n += m.get(control.charAt(i));
        }
        
        return n;
    }
}