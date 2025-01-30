import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long[] heights;
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
        int n = Integer.parseInt(tokenizer.nextToken());
        long m = Long.parseLong(tokenizer.nextToken());
        heights = new long[n];
        tokenizer = new StringTokenizer(reader.readLine());
        long maxHeight = 0;
        for (int i = 0; i < n; i++) {
            heights[i] = Long.parseLong(tokenizer.nextToken());
            maxHeight = Math.max(maxHeight, heights[i]);
        }

        long low = 0;
        long high = maxHeight;
        long mid = 0;
        long answer = 0;
        while (low <= high) {
            mid = (low + high) / 2;
            if (cutTree(mid) < m) { // 부족하면, 더 낮은 높이로 이동해야함
                high = mid - 1;
            } else { // 같거나 남으면, 더 높은 높이로 이동 해봐야함
                answer = mid;
                low = mid + 1;
            }
        }
        System.out.println(answer);
    }

    static long cutTree(long mid) {
        long total = 0;
        for (long h : heights) {
            if (h - mid > 0) {
                total += (h - mid);
            }
        }
        return total;
    }

}
