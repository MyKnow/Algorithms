import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int R;
	static int C;
	static int[][] MAP;
	static int MAX;
	
	static void printMap() {
		for (int[] row: MAP) {
			for (int col: row) {
				System.out.printf("%d ", col);
			}
			System.out.println();
		}
		System.out.println();
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine().trim());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		MAP = new int[R][C];
		for (int r=0; r<R; r++) {
			char[] line = br.readLine().trim().toCharArray();
			for (int c=0; c<C; c++) {
				if (line[c] == '.') {
					MAP[r][c] = 0;
				} else {
					MAP[r][c] = 1;
				}
			}
		}
		
		MAX = 0;
		for (int r=0; r<R; r++) {
			gas(r, 0);
		}
//		printMap();
		System.out.println(MAX);
		
	}

	static int[] dr = { -1, 0, 1 };
	static int[] dc = {  1, 1, 1 };
	static boolean gas(int cr, int cc) {
		
		for (int d=0; d<dr.length; d++) {
			int nr = cr + dr[d];
			int nc = cc + dc[d];
			
			if (isInbounded(nr, nc) && MAP[nr][nc] == 0) {
				if (nc==C-1) {
					MAX += 1;
					return true;
				}
				MAP[nr][nc] = 1;
				if (gas(nr, nc)) return true;
			}
		}
		return false;
	}
	
	static boolean isInbounded(int nr, int nc) {
		if ( (0 <= nr && nr < R) && (0 <= nc && nc < C)) {
			return true;
		}
		return false;
	}
}
