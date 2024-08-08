import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static int[] table;
    static int[] zeros;
    static int[] ones;

    static int fibonacci(int n) {
        if (n == 0 || n == 1) {
            return table[n];
        }
        if(table[n] != 0) {
            return table[n];
        }
        table[n] = fibonacci(n-1) + fibonacci(n-2);
        zeros[n] = zeros[n-1] + zeros[n-2];
        ones[n] = ones[n-1] + ones[n-2];
        return table[n];
    }
        
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());
        for(int i = 0; i < t; i++) {
            int n = Integer.parseInt(reader.readLine());
            if(n == 0) {
                System.out.println("1 0");
                continue;
            }
            initVariables(n);
            fibonacci(n);
            System.out.printf("%d %d\n", zeros[n], ones[n]);
        }
    }

    static void initVariables(int n) {
        table = new int[n + 1];
        zeros = new int[n + 1];
        ones = new int[n + 1];
        
        zeros[0] = 1; ones[1] = 1;
        table[0] = 0; table[1] = 1;
    }
}
