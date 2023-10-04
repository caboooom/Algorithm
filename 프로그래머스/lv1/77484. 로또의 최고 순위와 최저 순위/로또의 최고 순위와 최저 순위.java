class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        int zeros = 0; // 0 개수
        int equals = 0; // 일치하는 숫자 갯수
        for(int i=0; i<lottos.length; i++){
            for(int j=0; j<win_nums.length; j++){
                if(lottos[i] == 0) {
                    zeros++;
                    break;
                }
                if(lottos[i] == win_nums[j]) {
                    equals++;
                    break;
                }
            }
        }
        
        int[] ranking = new int[] {6,6,5,4,3,2,1};
        answer[0] = ranking[equals+zeros];
        answer[1] = ranking[equals];
        
        return answer;
    }
}