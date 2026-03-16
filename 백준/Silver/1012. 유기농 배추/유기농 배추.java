import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	final static int[] dr = { -1, 1, 0, 0 };
	final static int[] dc = {  0, 0,-1, 1 };
	
	static int C, R, K;
	static boolean[][] map;
	static int count;
	
	static void init() throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		C = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		map = new boolean[R][C];
		
		for (int k=0; k<K; k++) {
			st = new StringTokenizer(br.readLine());
			int c = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			
			map[r][c] = true;
		}
		
		count = 0;
	}
	
	static void solve() {
		for (int r=0; r<R; r++) {
			for (int c=0; c<C; c++) {
				if (map[r][c]) {
					count++;
					bfs(r, c);
				}
			}
		}
		
		sb.append(count).append("\n");
	}
	
	static boolean isInRange(int r, int c) {
		return 0 <= r && r < R && 0 <= c && c < C;
	}
	
	static void bfs(int r, int c) {
		ArrayDeque<int[]> q = new ArrayDeque<int[]>();
		q.addLast( new int[] { r, c } );
		map[r][c] = false;
		
		while(!q.isEmpty()) {
			int[] cur = q.pollFirst();
			int cr = cur[0];
			int cc = cur[1];
			
			for (int d=0; d<dr.length; d++) {
				int nr = cr + dr[d];
				int nc = cc + dc[d];
				
				if (!isInRange(nr, nc)) continue;
				if (!map[nr][nc]) continue;
				
				map[nr][nc] = false;
				q.addLast( new int[] { nr, nc } );
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		int T = Integer.parseInt(br.readLine());
		
		for (int t=0; t<T; t++) {
			init();
			solve();
		}
		System.out.print(sb.toString());
	}
}