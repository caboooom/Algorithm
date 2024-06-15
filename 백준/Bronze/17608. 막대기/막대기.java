import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(reader.readLine());

        Stack<Integer> stack = new Stack<>();
        for(int i=0; i<N; i++) {
            stack.push(Integer.parseInt(reader.readLine()));
        }

        int answer = 1;
        int currentMax = stack.pop();
        while (!stack.isEmpty()) {
            int top = stack.pop();
            if(top > currentMax) {
                answer++;
                currentMax = top;
            }
        }

        System.out.println(answer);
    }
}
