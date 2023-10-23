import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] input = reader.readLine().split(" ");
        long x = Integer.parseInt(input[0]);
        long y = Integer.parseInt(input[1]);
        long w = Integer.parseInt(input[2]);
        long s = Integer.parseInt(input[3]);

        long dist1 = (x+y) * w; // 직선 이동 거리
        long dist2; // 대각선 이동 거리
        if ( (x+y)%2 == 1){
            dist2 = (Math.max(x,y)-1) * s + w;
        }else {
            dist2 = Math.max(x,y) * s;
        }
        long dist3 = Math.min(x,y) * s + Math.abs(x-y) * w; // 직선, 대각선 조합 이동 거리

        System.out.println(Math.min(Math.min(dist1, dist2), dist3));
    }
}
