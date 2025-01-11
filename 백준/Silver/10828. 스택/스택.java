import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            String cmd = tokenizer.nextToken();
            switch (cmd) {
                case "push" :
                    int x = Integer.parseInt(tokenizer.nextToken());
                    stack.push(x);
                    break;
                case "pop" :
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.pop());
                    }
                    break;
                case "size" :
                    System.out.println(stack.size());
                    break;
                case "empty" :
                    int empty = stack.isEmpty() ? 1 : 0;
                    System.out.println(empty);
                    break;
                case "top" :
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.peek());
                    }
            }
        }
    }
}
