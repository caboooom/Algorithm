import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] lectures;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        long m = Long.parseLong(tokenizer.nextToken());
        lectures = new long[n];
        tokenizer = new StringTokenizer(reader.readLine());
        long totalLength = 0;
        long maxValue = 0;
        for (int i = 0; i < n; i++) {
            lectures[i] = Long.parseLong(tokenizer.nextToken());
            totalLength += lectures[i];
            maxValue = Math.max(maxValue, lectures[i]);
        }

        long low = maxValue;
        long high = totalLength;
        long mid = 0;
        long answer = 0;
        while (low <= high) {
            mid = (low + high) / 2;
            if (record(mid) <= m) { // 같거나 부족하면, 더 작게 잘라야함
                high = mid - 1;
                answer = mid;
            } else { // 남으면, 더 크게 잘라야함
                low = mid + 1;
            }
        }
        System.out.println(answer);
    }

    static long record(long mid) {
        long total = 1;
        long temp = 0;
        for (long l : lectures) {
            if (temp + l <= mid) {
                temp += l;
            } else {
                ++total;
                temp = l;
            }
        }
        return total;
    }

}
