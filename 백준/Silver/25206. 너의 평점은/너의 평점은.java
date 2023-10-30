import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    
        Map<String,Double> grade = new HashMap<>();
        grade.put("A+", 4.5);
        grade.put("A0", 4.0);
        grade.put("B+", 3.5);
        grade.put("B0", 3.0);
        grade.put("C+", 2.5);
        grade.put("C0", 2.0);
        grade.put("D+", 1.5);
        grade.put("D0", 1.0);
        grade.put("F", 0.0);
        grade.put("P", 0.0);

        double score = 0;
        double totalScore = 0;
        for(int  i=0; i<20; i++){
            String[] input = reader.readLine().split(" ");
            if (input[2].equals("P")){
                continue;
            }
            score += Double.parseDouble(input[1]) * grade.get(input[2]);
            totalScore += Double.parseDouble(input[1]);
        }
        
        if (totalScore == 0){
            System.out.println(0.0);
        }else{
            System.out.println(score/totalScore);
        }
    }

}
