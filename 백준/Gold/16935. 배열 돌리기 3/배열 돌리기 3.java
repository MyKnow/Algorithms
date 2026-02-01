import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    static int R;
    static int C;
    static int[][] MAP;
    static int MIDR;
    static int MIDC;

    static void tdTwist() {
        int[] tmp;
        for (int r=0; r<MIDR; r++) {
            tmp = MAP[r];
            MAP[r] = MAP[R-1-r];
            MAP[R-1-r] = tmp;
        }
    }

    static void lrTwist() {
        for (int r=0; r<R; r++) {
            int tmp;
            for (int c=0; c<MIDC; c++) {
                tmp = MAP[r][c];
                MAP[r][c] = MAP[r][C-1-c];
                MAP[r][C-1-c] = tmp;
            }
        }
    }

    static void clockRotate() {
        int[][] result = new int[C][R];
        for (int c=0; c<C; c++) {
            int[] temp = new int[R];
            int index = 0;
            for (int r=R-1; r>=0; r--) {
                temp[index++] = MAP[r][c];
            }
            result[c] = temp;
        }
        int temp = R, midTemp = MIDR;
        R = C; MIDR = MIDC;
        C = temp; MIDC = midTemp;
        MAP = result;
    }

    static void counterRotate() {
        int[][] result = new int[C][R];
        for (int c=C-1; c>=0; c--) {
            int[] temp = new int[R];
            int index = 0;
            for (int r=0; r<R; r++) {
                temp[index++] = MAP[r][c];
            }
            result[C-c-1] = temp;
        }
        int temp = R, midTemp = MIDR;
        R = C; MIDR = MIDC;
        C = temp; MIDC = midTemp;
        
        MAP = result;
    }

    static void move() {
        int[][] result = new int[R][C];
        for (int r=0; r<MIDR;r++) {
            for (int c=0; c<MIDC; c++) {
                result[r][c+MIDC] = MAP[r][c];
            }
        }
        for (int r=0; r<MIDR;r++) {
            for (int c=MIDC; c<C; c++) {
                result[r+MIDR][c] = MAP[r][c];
            }
        }
        for (int r=MIDR; r<R;r++) {
            for (int c=MIDC; c<C; c++) {
                result[r][c-MIDC] = MAP[r][c];
            }
        }
        for (int r=MIDR; r<R;r++) {
            for (int c=0; c<MIDC; c++) {
                result[r-MIDR][c] = MAP[r][c];
            }
        }
        MAP = result;
    }

    static void moveMore() {
        int[][] result = new int[R][C];
        for (int r=0; r<MIDR;r++) {
            for (int c=0; c<MIDC; c++) {
                result[r+MIDR][c] = MAP[r][c];
            }
        }
        for (int r=MIDR; r<R;r++) {
            for (int c=0; c<MIDC; c++) {
                result[r][c+MIDC] = MAP[r][c];
            }
        }
        for (int r=MIDR; r<R;r++) {
            for (int c=MIDC; c<C; c++) {
                result[r-MIDR][c] = MAP[r][c];
            }
        }
        for (int r=0; r<MIDR;r++) {
            for (int c=MIDC; c<C; c++) {
                result[r][c-MIDC] = MAP[r][c];
            }
        }
        MAP = result;
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        MIDR = R/2;
        MIDC = C/2;
        int order_length = Integer.parseInt(st.nextToken());

        MAP = new int[R][C];
        for (int r=0; r<R; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c=0; c<C; c++) {
                MAP[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        
        int[] orderList = new int[order_length];
        for (int i=0; i<order_length; i++) {
            orderList[i] = Integer.parseInt(st.nextToken());
        }

        for (int order: orderList) {
            if (order == 1) {
                tdTwist();
            } else if (order == 2) {
                lrTwist();
            } else if (order == 3) {
                clockRotate();
            } else if (order == 4) {
                counterRotate();
            } else if (order == 5) {
                move();
            } else {
                moveMore();
            } 
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