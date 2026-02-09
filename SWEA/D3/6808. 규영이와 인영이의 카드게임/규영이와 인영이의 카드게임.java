import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T;
  
  static int[] gyu = new int[9];
  static int[] in = new int[9];
  static boolean[] used = new boolean[9];
  
  static int win, lose;
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    boolean[] exist = new boolean[19];
    for (int i = 0; i < 9; i++) {
      gyu[i] = Integer.parseInt(st.nextToken());
      exist[gyu[i]] = true;
    }
    
    int idx = 0;
    for (int i = 1; i <= 18; i++) {
      if (!exist[i]) {
        in[idx++] = i;
      }
    }
    
    win = 0;
    lose = 0;
  }
  
  static void dfs(int round, int gyuSum, int inSum) {
    if (round == 9) {
      if (gyuSum > inSum) win++;
      else if (gyuSum < inSum) lose++;
      return;
    }
    
    for (int i = 0; i < 9; i++) {
      if (used[i]) continue;
      
      used[i] = true;
      int score = gyu[round] + in[i];
      
      if (gyu[round] > in[i]) {
        dfs(round + 1, gyuSum + score, inSum);
      } else {
        dfs(round + 1, gyuSum, inSum + score);
      }
      
      used[i] = false;
    }
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      dfs(0, 0, 0);
      sb.append("#").append(t).append(" ").append(win).append(" ").append(lose).append("\n");
    }
    System.out.print(sb.toString());
  }
}
