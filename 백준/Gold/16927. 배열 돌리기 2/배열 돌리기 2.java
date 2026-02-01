import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int R;
    static int C;
    static int RCOUNT;
    static int[][] MAP;

    public static void rotate(int k) {
        int top = k, left = k, bottom = R-1-k, right = C-1-k;
        int length = 2 * (bottom-top + right-left);

        int[] tmp = new int[length];
        int index = 0;
        // 좌 -> 우
        for (int c=left; c<right; c++) tmp[index++] = MAP[top][c];
        // 상 -> 하
        for (int r=top; r<bottom; r++) tmp[index++] = MAP[r][right];
        // 우 -> 좌
        for (int c=right; c>left; c--) tmp[index++] = MAP[bottom][c];
        // 하 -> 상
        for (int r=bottom; r>top; r--) tmp[index++] = MAP[r][left];


        index = RCOUNT % length;
        // 좌 -> 우
        for (int c=left; c<right; c++) MAP[top][c] = tmp[index++ % length];
        // 상 -> 하
        for (int r=top; r<bottom; r++)  MAP[r][right] = tmp[index++ % length];
        // 우 -> 좌
        for (int c=right; c>left; c--) MAP[bottom][c] = tmp[index++ % length];
        // 하 -> 상
        for (int r=bottom; r>top; r--) MAP[r][left] = tmp[index++ % length];
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        RCOUNT = Integer.parseInt(st.nextToken());

        MAP = new int[R][C];
        for (int r=0; r<R; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c=0; c<C; c++) {
                MAP[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        int K = Math.min(R, C) / 2;
        for (int k=0; k<K; k++) {
            rotate(k);
        }

        StringBuilder sb = new StringBuilder();
        for (int[] row: MAP) {
            for (int col: row) {
                sb.append(col).append(' ');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}