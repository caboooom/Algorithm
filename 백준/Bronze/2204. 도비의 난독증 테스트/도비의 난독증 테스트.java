import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int n = Integer.parseInt(reader.readLine());
            if (n == 0) break;

            List<String> words = new ArrayList<>();

            int firstWordIdx = 0;
            words.add(reader.readLine());
            for (int i = 1; i < n; i++) {
                String word = reader.readLine();
                if(word.compareToIgnoreCase(words.get(firstWordIdx)) < 0) {
                    firstWordIdx = i;
                }
                words.add(word);
            }

            System.out.println(words.get(firstWordIdx));
        }
    }
}
