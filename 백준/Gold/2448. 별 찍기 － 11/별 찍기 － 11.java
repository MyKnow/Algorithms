import java.util.Scanner;

public class Main {
	static int N;
	static int[][] map;
	
	public static void star(int r, int c, int n) {
		if (n == 3) {
			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 5; j++) {
					if (i==0 && j==2) map[r+i][c+j]=1;
					else if (i==1 && (j==1 || j==3)) map[r+i][c+j] = 1;
					else if (i==2) map[r+i][c+j] = 1;
				}
			}
		} else {
			star(r, c+n/2, n/2);
			star(r+n/2, c, n/2);
			star(r+n/2, c+n, n/2);
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		map = new int[N][N*2-1];
		star(0, 0, N);
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 2*N-1; j++) {
				sb.append(map[i][j]==1?"*":" ");
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
		
		
		sc.close();
	}

}