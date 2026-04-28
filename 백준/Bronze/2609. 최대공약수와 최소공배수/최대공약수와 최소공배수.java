import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static int new_gcd(int a, int b) {
		while (b != 0) {
			int tmp = a;
			a = b;
			b = tmp%b;
		}
		return a;
	}
	
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		int g = new_gcd(a, b);
		int l = a*b/g;
		
		System.out.println(g);
		System.out.println(l);
		
		br.close();
	}
}
