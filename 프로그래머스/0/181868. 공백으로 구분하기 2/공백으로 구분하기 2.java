import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        String[] arr = my_string.split(" ");
        List<String> temp = new ArrayList<>();
        for(String str : arr) {
            str = str.strip();
            if(!str.isBlank()) {
                temp.add(str);
            }
        }
        return temp.toArray(new String[0]);
    }
}