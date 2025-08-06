import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder builder = new StringBuilder();

        while (true) {
            String line = reader.readLine();
            if (line.equals(".")) {
                break;
            }
            Deque<Character> stack = new ArrayDeque<>();
            boolean flag = false;
            for (char c : line.toCharArray()) {
                if (c == '(' || c == '[') {
                    stack.addLast(c);
                } else if (c == ')') {
                    if (stack.isEmpty() || stack.peekLast() != '(') {
                        builder.append("no\n");
                        flag = true;
                        break;
                    } else {
                        stack.removeLast();
                    }
                } else if (c == ']') {
                    if (stack.isEmpty() || stack.peekLast() != '[') {
                        builder.append("no\n");
                        flag = true;
                        break;
                    } else {
                        stack.removeLast();
                    }
                }
            }
            if (!flag) {
                if (stack.isEmpty()) {
                    builder.append("yes\n");
                } else {
                    builder.append("no\n");
                }
            }
        }
        System.out.println(builder);
    }
}
