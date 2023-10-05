import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int n;
    static int k;
    static int count = 0;
    static int[] temp;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String line = reader.readLine();
        n = Integer.parseInt(line.split(" ")[0]);
        k = Integer.parseInt(line.split(" ")[1]);
        temp = new int[n];

        line = reader.readLine();
        int[] array = new int[n];
        String[] input = line.split(" ");
        for(int i=0; i<n; i++){
            array[i] = Integer.parseInt(input[i]);
        }

        mergeSort(array, 0, n-1);

        System.out.println(-1);
        
        return;

    }

    public static int[] mergeSort(int[] inputArray, int start, int end) {

        if (start < end) {
            int mid = (start + end) / 2;
            mergeSort(inputArray, start, mid);
            mergeSort(inputArray, mid + 1, end);
            merge(inputArray, start, mid, end);
        }

        return inputArray;
    }

    public static int[] merge(int[] inputArray, int start, int mid, int end) {

        
        int i = start;
        int j = mid + 1;
        int t = 0;
        while (i <= mid && j <= end) {
            if (inputArray[i] < inputArray[j]) {
                temp[t++] = inputArray[i++];
                count++;
                if (count == k){ 
                    System.out.println(temp[t-1]);
                    System.exit(0);
                }
                
            } else {
                temp[t++] = inputArray[j++];
                count++;
                if (count == k){
                    System.out.println(temp[t-1]);
                    System.exit(0);
                }
            }
        }
        while (i <= mid) {
            temp[t++] = inputArray[i++];
            count++;
            if (count == k){
                System.out.println(temp[t-1]);
                System.exit(0);
            }
        }
        while (j <= end) {
            temp[t++] = inputArray[j++];
            count++;
            if (count == k){
                System.out.println(temp[t-1]);
                System.exit(0);
            }
        }
        i = start;
        t = 0;
        while (i <= end) {
            inputArray[i++] = temp[t++];
        }
        return inputArray;
    }

}

