import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        char[] result = new char[a.length()];
        
        for(int i=0; i<result.length; i++){
            if (Character.isUpperCase(a.charAt(i))) {
                result[i] = Character.toLowerCase(a.charAt(i));
            }else{
                result[i] = Character.toUpperCase(a.charAt(i));
            }
        }
        System.out.println(new String(result));
    }       
}