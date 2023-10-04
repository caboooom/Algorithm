class Solution {
    public int solution(int[] nums) {

        boolean[] primeNumbers = new boolean[3001];
        primeNumbers[0] = false;
        primeNumbers[1] = false;
        for(int i=2; i<3001; i++){
            primeNumbers[i] = true;
        }
        for(int i=2; i*i<3001; i++){
            if (primeNumbers[i]){
                for(int j=i*2; j<3001; j+=i){
                    primeNumbers[j] = false;
                }
            }
        }
        
        int answer = 0;
        for(int i=0; i<nums.length; i++){
            for(int j=i+1; j<nums.length; j++){
                for(int k=j+1; k<nums.length;k++){
                    int sum = nums[i] + nums[j] + nums[k];
                    if(primeNumbers[sum]) answer++;
                }
            }
        }
        return answer;
    }
}