import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] numbers = {a,b,c,d};
        Arrays.sort(numbers);
        
        if (numbers[0] == numbers[3]){
            answer = numbers[0] * 1111;
        }else if(numbers[0] != numbers[1] && numbers[1]==numbers[3]){
            answer = (int)Math.pow(numbers[3]*10+numbers[0],2);
        }else if(numbers[3] != numbers[0] && numbers[0]==numbers[2]){
            answer = (int)Math.pow(numbers[0]*10+numbers[3],2);
        }else if(numbers[0]==numbers[1] && numbers[2]==numbers[3] 
                 && numbers[1]!=numbers[2]){
            answer = (numbers[0]+numbers[3]) * (int)Math.abs(numbers[0]-numbers[3]);
        }else if(numbers[0]!=numbers[1] && numbers[1]!=numbers[2]
                 && numbers[2]!=numbers[3]){
            answer = numbers[0];
        }else{
            if (numbers[0]==numbers[1]) answer = numbers[2]*numbers[3];
            else if (numbers[1]==numbers[2]) answer = numbers[0]*numbers[3];
            else if (numbers[2]==numbers[3]) answer = numbers[0]*numbers[1];
        }
        
        return answer;
    }
}