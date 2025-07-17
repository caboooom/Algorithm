class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;
        int numX = (num-1) / w;
        int numY = (num-1) % w;
        if (numX % 2 == 1) {
            numY = w - numY - 1;
        }
        
        int lastX = (n-1) / w;
        int lastY = (n-1) % w;
        if (lastX % 2 == 1) {
            lastY = w - lastY - 1;
        }
        
        answer = lastX - numX;
        if (lastX % 2 == 0) {
            if (numY <= lastY) {
                answer++;
            }
        } else {
            if (numY >= lastY) {
                answer++;
            }
        }
        return answer;
    }
}