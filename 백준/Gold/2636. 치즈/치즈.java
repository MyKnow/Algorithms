import java.io.*;
import java.util.*;

public class Main {
  static int R, C;
  static int[][] hasCheese;
  static int count;
  static int hour;
  static Queue<int[]> queue;
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = {  0, 0,-1, 1 };
  
  static boolean isItMeltable(int r, int c) {
    for (int d=0; d<dr.length; d++) {
      int nr = r + dr[d], nc = c + dc[d];
      if (isInbound(nr, nc) && hasCheese[r][c] == 1 && hasCheese[nr][nc] == 3) return true;
    }
    return false;
  }
  
  static boolean isInbound(int nr, int nc) {
    return (0<=nr && nr<R && 0<=nc && nc<C);
  }
  
  static void diffuseAir() {
    hour++;
    queue = new LinkedList();
    queue.offer(new int[] { 0, 0 });
    hasCheese[0][0] = 3;
    
    while (!queue.isEmpty()) {
      int[] currentPos = queue.poll();
      int cr = currentPos[0];
      int cc = currentPos[1];
      
      for (int d=0; d<dr.length; d++) {
        int nr = cr + dr[d], nc = cc + dc[d];
        if (isInbound(nr, nc) && hasCheese[nr][nc] == 0) {
          hasCheese[nr][nc] = 3;
          queue.offer(new int[] {nr, nc});
        } else if (isInbound(nr, nc) && isItMeltable(nr, nc)) {
          hasCheese[nr][nc] = 2;
          count++;
        }
      }
    }
  }
  
  static int countingCheese() {
    int sum = 0;
    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        int currentValue = hasCheese[r][c];
        if (currentValue == 1) sum ++;
        else if (currentValue == 2 || currentValue == 3) hasCheese[r][c] = 0;
      }
    }
    return sum;
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    
    hasCheese = new int[R][C];
    for (int r=0; r<R; r++) {
    st = new StringTokenizer(br.readLine());
      for (int c=0; c<C; c++) {
        hasCheese[r][c] = Integer.parseInt(st.nextToken());
      }
    }

    count = 0;
    hour = 0;
    if (countingCheese() == 0) System.out.println("0\n0");
    while(countingCheese() != 0) {
      count = 0;
      diffuseAir();
    }
    
    System.out.println(hour + "\n" + count);
  }
}