import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	static int N, S;
	static int[] stones;
	static int answer;
	
	static void init() throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		
		stones = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int n=0; n<N; n++) stones[n] = Integer.parseInt(st.nextToken());
		
		answer = 0;
	}
	
	static void solve() {
		backtracking(0, 0, 0);
	}
	
	static void backtracking(int depth, int sum, int count) {
		if (depth == N) {
			if (sum == S && count != 0) answer++;
			return;
		}
		
		int stone = stones[depth];
		backtracking(depth+1, sum+stone, count+1);
		backtracking(depth+1, sum, count);
		return;
	}
	
	public static void main(String[] args) throws Exception {
		init();
		solve();
		System.out.println(answer);
	}
}