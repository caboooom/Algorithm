import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    static BufferedWriter writer;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input[] = reader.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        arr = new int[n+1];
        writer = new BufferedWriter(new OutputStreamWriter(System.out));

        permutation(0);
        writer.flush();
    }

    public static void permutation(int k) throws IOException {
        if (k == m){
            for (int i=0; i<m; i++){
                writer.write(arr[i]+" ");
            }
            writer.newLine();
            return;
        }
        for(int i=1; i<=n; i++){
                arr[k] = i;
                permutation(k+1);
            }
        }

}
