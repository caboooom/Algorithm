import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] input = reader.readLine().split(" ");
        int[][] numbers = new int[n][2];
        for (int i = 0; i < n; i++) {
            numbers[i][0] = Integer.parseInt(input[i]);
        }
        numbers[0][1] = 1;

        if (n == 1) {
            System.out.println(1);
            return;
        }

        int answer = 1;
        if (numbers[0][0] < numbers[1][0]) {
            numbers[1][1] = 2;
        } else {
            numbers[1][1] = 1;
        }

        for (int i = 1; i < n; i++) {
            int k = 0;
            for (int j = 0; j <= i - 1; j++) {
                if (numbers[j][0] < numbers[i][0]) {
                    k = Math.max(k, numbers[j][1]);
                }
            }
            numbers[i][1] = k + 1;

            answer = Math.max(answer, numbers[i][1]);
        }
        System.out.println(answer);
    }
}
