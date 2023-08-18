import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int d[][] = new int[n+1][n+1];
        for (int i=0; i<n+1; i++){
            d[i][1] = i;
            d[i][0] = 1;
            d[i][i] = 1;
        }
        for(int i=2; i<n+1; i++){
            for(int j=1; j<i; j++){
                d[i][j] = d[i-1][j] + d[i-1][j-1];
                d[i][j] = d[i][j]%10007;
            }
        }
        System.out.println(d[n][k]%10007);
    }
}