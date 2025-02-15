import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine()," ");
        
        int A = Integer.parseInt(tokenizer.nextToken());
        int B = Integer.parseInt(tokenizer.nextToken());
        int C = Integer.parseInt(tokenizer.nextToken());
        
        StringBuilder builder = new StringBuilder();
        builder.append((A + B) % C).append("\n");
        builder.append(((A % C) + (B % C)) % C).append("\n");
        builder.append((A * B) % C).append("\n");
        builder.append(((A % C) * (B % C)) % C);
        System.out.println(builder);
    }
}