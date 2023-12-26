import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main { 

    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        int n = Integer.parseInt(line.split(" ")[0]);
        int target = Integer.parseInt(line.split(" ")[1]);

        line = reader.readLine();
        String[] strArr = line.split(" ");
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(strArr[i]);
        }

        int i = 0;
        int j = 0;
        int sum = 0;
        int count = 0;
        while (i < arr.length) {
            if (i == j) {
                sum = arr[i];
            }

            if (sum < target && j < arr.length - 1) {
                sum += arr[++j];
            } else {
                if (sum == target){
                    count++;
                }
                sum -= arr[i++];
                j=i;
            }
        }
        
        System.out.println(count);
    }
}
