import java.io.*;
import java.util.*;

public class Main {
    static int R, C, N;
    static int perimeter;

    static int toPos(int dir, int dist) {
        switch (dir) {
            case 1: return dist; 
            case 4: return C + dist;  
            case 2: return C + R + (C - dist); 
            case 3: return C + R + C + (R - dist);
        }
        return 0;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        perimeter = 2 * (R + C);

        N = Integer.parseInt(br.readLine());
        int[] shops = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int dir = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());
            shops[i] = toPos(dir, dist);
        }

        st = new StringTokenizer(br.readLine());
        int startDir = Integer.parseInt(st.nextToken());
        int startDist = Integer.parseInt(st.nextToken());
        int start = toPos(startDir, startDist);

        int answer = 0;
        for (int shop : shops) {
            int d = Math.abs(shop - start);
            answer += Math.min(d, perimeter - d);
        }

        System.out.println(answer);
    }
}