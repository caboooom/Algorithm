class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        
        int start = Integer.parseInt(op_start.split(":")[0]) * 60 +
            Integer.parseInt(op_start.split(":")[1]);
        int end = Integer.parseInt(op_end.split(":")[0]) * 60 +
            Integer.parseInt(op_end.split(":")[1]);
        int currPos = Integer.parseInt(pos.split(":")[0]) * 60 +
            Integer.parseInt(pos.split(":")[1]);
        int len = Integer.parseInt(video_len.split(":")[0]) * 60 +
            Integer.parseInt(video_len.split(":")[1]);
        
        
        if (currPos >= start && currPos <= end) {
                currPos = end;
        }
        
        for (String cmd : commands) {
            if (cmd.equals("prev")) {
                if (currPos <= 10) {
                    currPos = 0;
                } else {
                    currPos -= 10;
                }
            } else {
                if (currPos + 10 >= len) {
                    currPos = len;
                } else {
                    currPos += 10;
                }
            }
            if (currPos >= start && currPos <= end) {
                currPos = end;
            }
        }
        
        int m = currPos / 60;
        int s = currPos % 60;
        return String.format("%02d:%02d", m, s);
    }
}