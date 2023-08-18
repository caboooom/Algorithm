
import java.io.*;
import java.util.*;


class Students implements Comparable<Students>{
    private String name;
    private int korean;
    private int english;
    private int math;

    public Students(String name, int korean, int english, int math){
        this.name = name;
        this.korean = korean;
        this.english = english;
        this.math = math;
    }

    @Override
    public String toString(){
        return this.name;
    }

    @Override
    public int compareTo(Students o){
        if (this.korean != o.korean){
            return o.korean - this.korean;
        }
        if (this.english != o.english){
            return this.english - o.english;
        }
        if (this.math != o.math){
            return o.math - this.math;
        }
        return this.name.compareTo(o.name);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        ArrayList<Students> arr = new ArrayList<>();

        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int korean = Integer.parseInt(st.nextToken());
            int english = Integer.parseInt(st.nextToken());
            int math = Integer.parseInt(st.nextToken());
            arr.add(new Students(name, korean, english, math));
        }

        Collections.sort(arr);

        for(int i=0; i<n; i++){
            System.out.println(arr.get(i));
        }
    }
}
