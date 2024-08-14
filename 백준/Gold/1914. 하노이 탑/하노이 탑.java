import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BigInteger n = new BigInteger(reader.readLine());
        System.out.println((new BigInteger("2").pow(n.intValue()))
                .subtract(new BigInteger("1")));
        if(n.intValue() <= 20) {
            hanoiTower(n.intValue(), 1, 2, 3);
        }
    }

    public static void hanoiTower(int n, int origin, int temp, int dest) {
        if(n == 1) {
            System.out.println(origin + " " + dest);
            return;
        }
        hanoiTower(n-1, origin, dest, temp);
        hanoiTower(1, origin, temp, dest);
        hanoiTower(n-1, temp, origin, dest);
    }
}
