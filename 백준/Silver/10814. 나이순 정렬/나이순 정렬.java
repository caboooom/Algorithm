import java.util.stream.Collectors;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        StringBuilder builder = new StringBuilder();

        List<Member> members = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            members.add(new Member(Integer.parseInt(tokenizer.nextToken()), tokenizer.nextToken()));
        }

        List<Member> sortedList = members.stream()
                .sorted(Comparator.comparing(m -> m.age))
                .collect(Collectors.toList());
        for (Member member : sortedList) {
            builder.append(member.age).append(" ").append(member.name).append("\n");
        }
        System.out.println(builder);

    }
}

class Member {
    int age;
    String name;
    Member(int age, String name) {
        this.age = age;
        this.name = name;
    }
}