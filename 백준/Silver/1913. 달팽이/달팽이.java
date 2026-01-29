import java.util.Scanner;

public class Main {
	static int N;
	static int[][] MAP;
	static int TARGET;

	static int d;
	static int r;
	static int c;
	static int tr;
	static int tc;
	final static int[] dr = { -1, 0, 1, 0 };
	final static int[] dc = {  0, 1, 0,-1 };
	
	static void move(int i) {
		// 위치 기록
		MAP[r][c] = i;
		
		int nr = r + dr[d];
		int nc = c + dc[d];
		
		// 전진이 가능하다면
		if (isInbound(nr, nc) && MAP[nr][nc] == 0) {
			// 전진
			r = nr;
			c = nc;
			
			// 우측을 검사해보고
			int tmpD = (d+1) % 4;
			int tmpR = nr+dr[tmpD];
			int tmpC = nc+dc[tmpD];
			if (isInbound(tmpR, tmpC)) {
				// 우측이 비어있다면 회전
				if (MAP[tmpR][tmpC] == 0) {
					d = tmpD;
				}
			}
		}
	}
	
	static boolean isInbound(int nr, int nc) {
		if (0 <= nr && nr < N && 0 <= nc && nc < N) return true;
		return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();
		
		N = sc.nextInt();
		MAP = new int[N][N];
		r = N/2;
		c = N/2;
		TARGET = sc.nextInt();
		for (int i=1; i<=N*N; i++) {
			if (i == TARGET) {
				tr = r+1;
				tc = c+1;
			}
			move(i);
		}
		
		for (int[] row: MAP) {
			for (int col: row) {
				sb.append(col+" ");
			}
			sb.append("\n");
		}
		sb.append(tr + " " + tc);
		System.out.println(sb);
		sc.close();
	}

}
