import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());
        for(int i=1; i<=N; i++) {
            System.out.print("Case #" + i + ": ");
            String[] words = reader.readLine().split(" ");
            int length = words.length;
            for(int j=length-1; j>=0; j--) {
                System.out.print(words[j] + " ");
            }
            System.out.println();
        }
    }
}