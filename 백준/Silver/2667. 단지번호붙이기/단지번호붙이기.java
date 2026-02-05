import java.util.*;
import java.io.*;

// 단지별로 집의 수를 세야 한다.
// 1. dfs를 통해 단지 내 집의 수를 센다.
// 2. dfs 중에 확인한 집을 영구적으로 지워버려서 탐색에 걸리지 않게 한다.

// 이미 재귀 DFS로 풀었던 문제이므로 Stack으로 풀어보자.

public class Main {
    final static int[] dr = { -1, 1, 0, 0 };
    final static int[] dc = {  0, 0,-1, 1 };

    static int N;
    static int[] homes;
    static int villageCount;
    static boolean[][] canVisit;

    static void dfs(int r, int c) {
        int homeCount = 1;
        Deque<int[]> stack = new ArrayDeque<>();

        canVisit[r][c] = false;
        stack.addLast( new int[] { r, c } );
        while(!stack.isEmpty()) {
            int[] pos = stack.pollLast();
            int cr = pos[0];
            int cc = pos[1];

            for (int d=0; d<dr.length; d++) {
                int nr = cr + dr[d], nc = cc + dc[d];
                if (inRange(nr, nc) && canVisit[nr][nc]) {
                    canVisit[nr][nc] = false;
                    homeCount++;
                    stack.addLast( new int[] { nr, nc } );
                }
            }
        }

        homes[villageCount++] = homeCount;
    }

    static boolean inRange(int nr, int nc) {
        return (0 <= nr && nr < N) && (0 <= nc && nc < N);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        canVisit = new boolean[N][N];
        for (int r=0; r<N; r++) {
            char[] line = br.readLine().toCharArray();
            for (int c=0; c<N; c++) {
                canVisit[r][c] = line[c]-'0' == 1;
            }
        }

        villageCount = 0;
        homes = new int[N*N];
        for (int r=0; r<N; r++) {
            for (int c=0; c<N; c++) {
                if (canVisit[r][c]) dfs(r, c);
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(villageCount).append("\n");


        Arrays.sort(homes, 0, villageCount);
        for (int i = 0; i< villageCount; i++) {
            sb.append(homes[i]).append("\n");
        }
        System.out.print(sb.toString());
    }
}