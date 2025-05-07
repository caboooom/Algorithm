import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(reader.readLine());

        List<Integer> aSum = new ArrayList<>();

        int n = Integer.parseInt(reader.readLine());
        int[] aArr = new int[n];
        StringTokenizer tokenizer = new StringTokenizer(reader.readLine(), " ");
        for (int i = 0; i < n; i++) {
            aArr[i] = Integer.parseInt(tokenizer.nextToken());
        }
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += aArr[j];
                aSum.add(sum);
            }
        }

        int m = Integer.parseInt(reader.readLine());
        int[] bArr = new int[m];
        tokenizer = new StringTokenizer(reader.readLine(), " ");
        for (int i = 0; i < m; i++) {
            bArr[i] = Integer.parseInt(tokenizer.nextToken());
        }

        Map<Integer, Integer> bMap = new HashMap<>();
        for (int i = 0; i < m; i++) {
            int sum = 0;
            for (int j = i; j < m; j++) {
                sum += bArr[j];
                bMap.put(sum, bMap.getOrDefault(sum, 0) + 1);
            }
        }

        Arrays.sort(aArr);

        long answer = 0;
        for (int a : aSum) {
            answer += bMap.getOrDefault(t - a, 0);
        }
        System.out.println(answer);

    }
}
