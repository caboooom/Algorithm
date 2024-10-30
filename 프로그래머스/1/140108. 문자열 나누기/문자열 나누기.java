class Solution {
    public int solution(String s) {
        int answer = 0;
        
        int cursor = 0;
        while (cursor < s.length()) {
            char x = s.charAt(cursor);
            int isX = 0;
            int notX = 0;
            for(int i = cursor; i < s.length(); i++) {
                ++cursor;
                if (x == s.charAt(i)) {
                    ++isX;
                } else {
                    ++notX;
                }
                if (isX == notX) {
                    break;
                }
            }
            ++answer;
        }
        return answer;
    }
}