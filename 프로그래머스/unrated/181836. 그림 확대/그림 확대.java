class Solution {
    public String[] solution(String[] picture, int k) {
        
        String[] answer = new String[picture.length*k];
        int curRow = 0;
        for(int i=0; i < picture.length; i++){
            StringBuffer sb = new StringBuffer();
            char[] temp = picture[i].toCharArray();
            for(int j=0; j<temp.length; j++){
                for(int l=0; l<k; l++){
                    sb.append(temp[j]);
                }
            }
            for(int l=0; l<k; l++){
                answer[curRow++] = sb.toString();
            }
        }
        return answer;
    }
}