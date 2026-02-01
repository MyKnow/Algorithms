import java.io.*;
import java.util.*;

public class Main {

    static int N, M, R;
    static int[][] A;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        A = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int layers = Math.min(N, M) / 2;
        for (int k = 0; k < layers; k++) {
            rotateLayer(k);
        }

        StringBuilder sb = new StringBuilder();
        for (int[] row : A) {
            for (int v : row) {
                sb.append(v).append(' ');
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    static void rotateLayer(int k) {
        int top = k;
        int left = k;
        int bottom = N - 1 - k;
        int right = M - 1 - k;

        int len = 2 * (bottom - top + right - left);
        int[] tmp = new int[len];

        int idx = 0;

        // 위
        for (int j = left; j < right; j++) tmp[idx++] = A[top][j];
        // 오른쪽
        for (int i = top; i < bottom; i++) tmp[idx++] = A[i][right];
        // 아래
        for (int j = right; j > left; j--) tmp[idx++] = A[bottom][j];
        // 왼쪽
        for (int i = bottom; i > top; i--) tmp[idx++] = A[i][left];

        int rot = R % len;
        idx = rot;

        // 위
        for (int j = left; j < right; j++) A[top][j] = tmp[idx++ % len];
        // 오른쪽
        for (int i = top; i < bottom; i++) A[i][right] = tmp[idx++ % len];
        // 아래
        for (int j = right; j > left; j--) A[bottom][j] = tmp[idx++ % len];
        // 왼쪽
        for (int i = bottom; i > top; i--) A[i][left] = tmp[idx++ % len];
    }
}