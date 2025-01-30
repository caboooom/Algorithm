import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] cables;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int k = Integer.parseInt(tokenizer.nextToken());
        int n = Integer.parseInt(tokenizer.nextToken());
        long maxLength = Long.MIN_VALUE;
        cables = new long[k];
        for (int i = 0; i < k; i++) {
            long input = Long.parseLong(reader.readLine());
            maxLength = Math.max(maxLength, input);
            cables[i] = input;
        }

        long start = 1;
        long mid = 0;
        long end = maxLength;
        long answer = 0;
        while (start <= end) {
            mid = (start + end) / 2;
            long totalNumber = calculateTotalNumber(mid);
            if (totalNumber >= n) { // 더 크게 잘라야함
                answer = mid;
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        System.out.println(answer);
    }

    static long calculateTotalNumber(long mid) {
        int totalNumber = 0;
        for (long c : cables) {
            totalNumber += (c / mid);
        }
        return totalNumber;
    }
}
