import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String S = reader.readLine();
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        for(char c : alphabet) {
            System.out.print(S.indexOf(c) + " ");
        }
    }
}