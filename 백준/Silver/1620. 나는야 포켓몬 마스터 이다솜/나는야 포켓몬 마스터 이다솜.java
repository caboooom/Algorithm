import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] line = reader.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);

        Map<Integer, String> numToName = new HashMap<>();
        Map<String, Integer> nameToNum = new HashMap<>();

        for(int i=0; i<N; i++) {
            String poketmon = reader.readLine();
            numToName.put(i+1, poketmon);
            nameToNum.put(poketmon, i+1);
        }

        for(int i=0; i<M; i++) {
            String question = reader.readLine();
            try {
                System.out.println(numToName.get(Integer.parseInt(question)));
            } catch (NumberFormatException ignore) {
                System.out.println(nameToNum.get(question));
            }
        }

    }
}