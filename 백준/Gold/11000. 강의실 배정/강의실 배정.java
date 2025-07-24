import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());

        PriorityQueue<Integer> rooms = new PriorityQueue<>();

        List<Lecture> lectures = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int start = Integer.parseInt(tokenizer.nextToken());
            int end = Integer.parseInt(tokenizer.nextToken());
            lectures.add(new Lecture(start, end));
        }
        lectures = lectures.stream()
                .sorted((l1, l2) -> {
                    if (l1.start == l2.start) {
                        return Integer.compare(l1.end, l2.end);
                    }
                    return Integer.compare(l1.start, l2.start);
                })
                .collect(Collectors.toList());

        for (Lecture lecture : lectures) {
            if (rooms.isEmpty()) {
                rooms.add(lecture.end);
            } else {
                if (rooms.peek() <= lecture.start) {
                    rooms.poll();
                }
                rooms.add(lecture.end);
            }
        }
        System.out.println(rooms.size());
    }
}

class Lecture {
    int start;
    int end;
    Lecture(int start, int end) {
        this.start = start;
        this.end = end;
    }
}