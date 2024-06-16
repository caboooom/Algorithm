import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] numbers = reader.readLine().split(" ");

        int idx = 0;
        List<Integer> line = new ArrayList<>();
        for(String number : numbers) {
            line.add(idx - Integer.parseInt(number), ++idx);
        }

        for(int student : line) {
            System.out.print(student + " ");
        }
    }
}
