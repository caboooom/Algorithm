class Solution {
    public String solution(String code) {
        String answer = "";
        StringBuilder result = new StringBuilder();
        int mode = 0;
        char[] arr = code.toCharArray();
        for(int i=0; i<arr.length; i++){
            if (mode == 0){
                if(arr[i] == '1'){
                    mode = 1;
                }else if (i%2==0){
                    result.append(arr[i]);
                }
            }else{
                if(arr[i] == '1'){
                    mode = 0;
                }else if (i%2==1){
                    result.append(arr[i]);
                }
            }
        }
        
        answer = result.toString();
        
        if (answer.equals("")) return "EMPTY";
        return answer;
    }
}