import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        Player first = new Player(players[0], null, null);
        Player prev = first;
        Map<String, Player> map = new HashMap<>();
        map.put(first.name, first);
        
        for (int i = 1; i < players.length; i++) {
            Player player = new Player(players[i], prev, null);
            map.put(player.name, player);
            prev.next = player;
            prev = player;
        }
        
        for (String player : callings) {
            Player target = map.get(player);
            prev = target.prev;
            target.prev = prev.prev;
            if (prev.prev != null) {
                prev.prev.next = target;
            }
            if (target.next != null) {
                target.next.prev = prev;
            }
            prev.next = target.next;
            target.next = prev;
            prev.prev = target;
            if (target.prev == null) {
                first = target;
            }
        }
        String[] answer = new String[players.length];
        for (int i = 0; i < players.length; i++) {
            answer[i] = first.name;
            first = first.next;
        }
        return answer;
    }
}

class Player {
    String name;
    Player prev;
    Player next;
    Player(String name, Player prev, Player next) {
        this.name = name;
        this.prev = prev;
        this.next = next;
    }
}