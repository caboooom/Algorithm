import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static StringBuilder builder = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        System.out.println((int) (Math.pow(2, n) - 1));
        hanoi(n, 1, 2, 3);
        System.out.println(builder);
    }
    public static void hanoi(int n, int origin, int temp, int dest) {
        if(n == 1) {
            builder.append(origin + " " + dest + "\n");
            return;
        }
        hanoi(n-1, origin, dest, temp);
        builder.append(origin + " " + dest + "\n");
        hanoi(n-1, temp, origin, dest);
    }
}
