import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] line = reader.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int k = Integer.parseInt(line[1]);

        List<Integer> list = new LinkedList<>();
        for(int i = 1; i <= n; i++) {
            list.add(i);
        }

        int target = k - 1;
        StringBuilder builder = new StringBuilder("<");
        while(!list.isEmpty()) {
            target = target % list.size();
            int data = list.remove(target);
            builder.append(data + ", ");
            target += (k-1);
        }
        builder.delete(builder.length()-2, builder.length()).append(">");
        System.out.println(builder);
    }
}
