import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int T;
  static int M, A;
  static int[] moveA, moveB;
  static BC[] bcList;
  
  // 방향: 0 정지, 1 상, 2 우, 3 하, 4 좌
  static int[] dr = {0, -1, 0, 1, 0};
  static int[] dc = {0, 0, 1, 0, -1};
  
  static class BC {
    int x, y, range, power;
    
    BC(int x, int y, int range, int power) {
      this.x = x;
      this.y = y;
      this.range = range;
      this.power = power;
    }
    
    boolean canCharge(int r, int c) {
      return Math.abs(x - c) + Math.abs(y - r) <= range;
    }
  }
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    M = Integer.parseInt(st.nextToken());
    A = Integer.parseInt(st.nextToken());
    
    moveA = new int[M + 1];
    moveB = new int[M + 1];
    
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= M; i++) moveA[i] = Integer.parseInt(st.nextToken());
    
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= M; i++) moveB[i] = Integer.parseInt(st.nextToken());
    
    bcList = new BC[A];
    for (int i = 0; i < A; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      int range = Integer.parseInt(st.nextToken());
      int power = Integer.parseInt(st.nextToken());
      bcList[i] = new BC(x, y, range, power);
    }
  }
  
  static int solve() {
    int ar = 1, ac = 1;
    int br = 10, bc = 10;
    int total = 0;
    
    for (int time = 0; time <= M; time++) {
      ArrayList<Integer> aBC = new ArrayList<>();
      ArrayList<Integer> bBC = new ArrayList<>();
      
      for (int i = 0; i < A; i++) {
        if (bcList[i].canCharge(ar, ac)) aBC.add(i);
        if (bcList[i].canCharge(br, bc)) bBC.add(i);
      }
      
      int max = 0;
      
      if (aBC.size() == 0 && bBC.size() == 0) {
        max = 0;
      } else if (aBC.size() == 0) {
        for (int b : bBC) {
          max = Math.max(max, bcList[b].power);
        }
      } else if (bBC.size() == 0) {
        for (int a : aBC) {
          max = Math.max(max, bcList[a].power);
        }
      } else {
        for (int a : aBC) {
          for (int b : bBC) {
            if (a == b) {
              max = Math.max(max, bcList[a].power);
            } else {
              max = Math.max(max, bcList[a].power + bcList[b].power);
            }
          }
        }
      }
      
      total += max;
      
      if (time == M) break;
      
      int aOrder = moveA[time+1];
      int bOrder = moveB[time+1];
      ar += dr[aOrder];
      ac += dc[aOrder];
      br += dr[bOrder];
      bc += dc[bOrder];
    }
    
    return total;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      int answer = solve();
      sb.append("#").append(t).append(" ").append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}