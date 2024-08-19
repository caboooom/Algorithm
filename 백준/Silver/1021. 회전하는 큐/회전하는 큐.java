import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] line = reader.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int count = 0;

        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < n; i++) {
            queue.add(i+1);
        }

        line = reader.readLine().split(" ");
        for(int i = 0; i < line.length; i++) {
            int target = Integer.parseInt(line[i]);
            int index = 0;
            Iterator<Integer> iter = queue.iterator();
            while(true) {
                if(iter.next() == target) {
                    break;
                }
                index++;
            }
            if(index < queue.size() / 2 + 1) {
                while(true) {
                    int head = queue.removeFirst();
                    if(head == target) {
                        break;
                    }
                    queue.addLast(head);
                    count++;
                }
            } else {
                while(true) {
                    int tail = queue.removeLast();
                    count++;
                    queue.addFirst(tail);
                    if(tail == target) {
                        break;
                    }
                }
                queue.removeFirst();
            }
        }
        System.out.println(count);

    }

}
