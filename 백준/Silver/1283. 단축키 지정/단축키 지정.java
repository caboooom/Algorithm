import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        Set<Character> dict = new HashSet<>();
        for(int i = 0; i < n; i++) {
            String input = reader.readLine();
            String[] line = input.split(" ");
            String[] output = new String[line.length];
            boolean flag = false;
            for(int j = 0; j < line.length; j++) {
                String word = line[j];
                if (!dict.contains(Character.toUpperCase(word.charAt(0))) && !flag) {
                    dict.add(Character.toUpperCase(word.charAt(0)));
                    flag = true;
                    output[j] = "[" + word.substring(0,1) + "]" + word.substring(1, word.length());
                } else {
                    output[j] = word;
                }
            }
            
            StringBuilder builder = new StringBuilder();
            for(String str : output) {
                builder.append(str).append(" ");
            }

            if(builder.toString().contains("[")) {
                System.out.println(builder);
            } else {
                StringBuilder builder2 = new StringBuilder();
                for(int j = 0; j < input.length(); j++) {
                    if(input.charAt(j) == ' ') {
                        builder2.append(" ");
                        continue;
                    }
                    if (!dict.contains(Character.toUpperCase(input.charAt(j)))) {
                        builder2.append("[").append(input.charAt(j)).append("]");
                        builder2.append(input.substring(j+1, input.length()));
                        dict.add(Character.toUpperCase(input.charAt(j)));
                        break;
                    } else {
                        builder2.append(input.charAt(j));
                    }
                }
                System.out.println(builder2);
            }

            

        }
    }
}
