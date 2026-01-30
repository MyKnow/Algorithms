import java.util.*;
import java.io.*;

public class Main {
	static int N;
	static int M;
	static int R;
	static int K;
	static int[][] A;
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();
	
	static String readLine() throws Exception {
		String line = br.readLine().trim();
		st = new StringTokenizer(line);
		return line;
	}
	
	static int nextInt() {
		return Integer.parseInt(st.nextToken());
	}
	
	static void printMap() {
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				sb.append(A[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
		sb = new StringBuilder();
	}
	
	// 우, 하, 좌, 상
	static int[] dr = { 0, 1, 0, -1 };
	static int[] dc = { 1, 0,-1,  0 };
	static void rotate() {
		for (int k=0; k<K; k++) {
			int start_r = k;
			int start_c = k;
			int length = 2 * (N-2*k) + 2 * ((M-2*k) - 2);
			
			int d = 0;
			int r = start_r;
			int c = start_c;
			int temp = A[start_r][start_c];
			for (int i=0; i<length; i++) {
				int nr = r + dr[d];
				int nc = c + dc[d];
				
				if ((nr < start_r || N-k <= nr) || (nc < start_c || M-k <= nc)) {
					d = (d+1) % 4;
					i--;
					continue;
				} else if (d == 3 && nr == start_r && nc == start_c) {
					A[r][c] = temp;
					break;
				}
				
				A[r][c] = A[nr][nc];
				r = nr;
				c = nc;
			}
		}
	}

	public static void main(String[] args) throws Exception {
		readLine();
		N = nextInt();
		M = nextInt();
		R = nextInt();
		A = new int[N][M];
		K = Math.min(N, M) / 2;
		for (int r=0; r<N; r++) {
			readLine();
			for (int c=0; c<M; c++) {
				A[r][c] = nextInt();
			}
		}
		
		for (int r=0; r<R; r++) {
			rotate();
		}
		
		printMap();
	}
}
