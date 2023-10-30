import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n;
    static int m;
    static int[] arr;
    static boolean[] isUsed;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input[] = reader.readLine().split(" ");
        n = Integer.parseInt(input[0]);
        m = Integer.parseInt(input[1]);

        arr = new int[n+1];
        isUsed = new boolean[n+1];

        permutation(0);
    }

    public static void permutation(int k){
        if (k == m){
            for (int i=0; i<m; i++){
                System.out.print(arr[i]+" ");
            }
            System.out.println();
            return;
        }
        for(int i=1; i<=n; i++){
            if(!isUsed[i]){
                arr[k] = i;
                isUsed[i] = true;
                permutation(k+1);
                isUsed[i] = false;
            }
        }
    }

}
