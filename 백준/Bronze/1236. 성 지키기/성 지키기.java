import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = reader.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        char[][] castle = new char[N][M];
        for(int i=0; i<N; i++) {
            castle[i] = reader.readLine().toCharArray();
        }

        int row = 0;
        for(int i=0; i<N; i++) {
            boolean isEmpty = true;
            for(int j=0;j<M;j++){
                if(castle[i][j] == 'X') {
                    isEmpty = false;
                    break;
                }
            }
            if(isEmpty) {
                row++;
            }
        }

        int col = 0;
        for(int i=0; i<M; i++) {
            boolean isEmpty = true;
            for(int j=0;j<N;j++){
                if(castle[j][i] == 'X') {
                    isEmpty = false;
                    break;
                }
            }
            if(isEmpty) {
                col++;
            }
        }

        System.out.println(Math.max(row, col));
    }
}
