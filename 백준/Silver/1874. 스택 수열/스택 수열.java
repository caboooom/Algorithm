import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(reader.readLine());
        }
        Deque<Integer> stack = new ArrayDeque<>();
        int pointer = 1;
        StringBuilder builder = new StringBuilder();
        int index = 0;
        while (index < n) {
            if (!stack.isEmpty() && arr[index] == stack.peekLast()) {
                stack.removeLast();
                builder.append("-\n");
                ++index;
            } else {
                if (pointer > n) {
                    break;
                }
                stack.addLast(pointer);
                builder.append("+\n");
                ++pointer;
            }
        }
        if (!stack.isEmpty()) {
            System.out.println("NO");
        } else {
            System.out.println(builder);
        }
    }
}
