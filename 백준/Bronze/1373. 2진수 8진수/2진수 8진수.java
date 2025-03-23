import java.io.*;
import java.math.BigInteger;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String input = reader.readLine();
		
		BigInteger result = new BigInteger(input, 2);
				
		System.out.println(result.toString(8));
	}

}