import java.io.*;

public class Main {

    static int[][] board = new int[3][3];

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int firstPlayer = Integer.parseInt(reader.readLine());
        int nextPlayer = 0;
        if (firstPlayer == 1) {
            nextPlayer = 2;
        } else {
            nextPlayer = 1;
        }

        for(int i = 0; i < 9; i++) {
            String line = reader.readLine();
            int row = Integer.parseInt(line.split(" ")[0]);
            int col = Integer.parseInt(line.split(" ")[1]);

            if (i % 2 == 0) {
                board[row-1][col-1] = firstPlayer;
            } else {
                board[row-1][col-1] = nextPlayer;
            }
            
            checkGameOver();
        }
        System.out.println(0);
        
    }

    public static void checkGameOver() {
        
        for(int i = 0; i < 3; i++) {
            if(board[i][0] != 0 && 
            board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
                System.out.println(board[i][0]); 
                System.exit(0);
            }
        }
        for(int i = 0; i < 3; i++) {
            if(board[0][i] != 0 &&
            board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
                System.out.println(board[0][i]);
                System.exit(0);
            }
        }
        if(board[0][0] != 0 &&
        board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
            System.out.println(board[0][0]);
            System.exit(0);
        }
        if(board[0][2] != 0 &&
        board[0][2] == board[1][1] &&  board[1][1] == board[2][0]) {
            System.out.println(board[0][2]);
            System.exit(0);
        }
    }

}
