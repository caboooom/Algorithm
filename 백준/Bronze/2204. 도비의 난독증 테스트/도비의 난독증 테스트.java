import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int n = Integer.parseInt(reader.readLine());
            if (n == 0) break;

            String firstWord = reader.readLine();

            for (int i = 1; i < n; i++) {
                String word = reader.readLine();
                if(word.compareToIgnoreCase(firstWord) < 0) {
                    firstWord = word;
                }
            }

            System.out.println(firstWord);
        }
    }
}
