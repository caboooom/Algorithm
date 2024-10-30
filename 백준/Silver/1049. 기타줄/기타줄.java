import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] line = reader.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);

        int packageMinPrice = Integer.MAX_VALUE;
        int singleMinPrice = Integer.MAX_VALUE;

        for(int i = 0; i < m; i++) {
            line = reader.readLine().split(" ");
            int packagePrice = Integer.parseInt(line[0]);
            int singlePrice = Integer.parseInt(line[1]);
            
            packageMinPrice = Math.min(packageMinPrice, packagePrice);
            singleMinPrice = Math.min(singleMinPrice, singlePrice);
        }

        if (packageMinPrice * n / 6 > singleMinPrice * n) {
            System.out.println(singleMinPrice * n);
            System.exit(0);
        }
        
        int totalPrice = 0;
        while (n >= 6) {
            totalPrice += packageMinPrice;
            n -= 6;
        }
        while (n > 0) {
            if (packageMinPrice < singleMinPrice || packageMinPrice < singleMinPrice * n) {
                totalPrice += packageMinPrice;
                n -= 6;
            } else {
                totalPrice += singleMinPrice;
                n -= 1;
            }
        }

        System.out.println(totalPrice);
    }
}