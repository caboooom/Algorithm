class Solution {
    public String[] solution(String[] strArr) {
        int n = 0;
        for (int i=0; i<strArr.length; i++){
            if (strArr[i].indexOf("ad") == -1) {
                n++;
            }
        }
        String[] answer = new String[n];
        for (int i=0,j=0; i<strArr.length; i++){
            if (strArr[i].indexOf("ad") == -1){
                answer[j] = strArr[i];
                j++;
            }
        }
        return answer;
    }
}