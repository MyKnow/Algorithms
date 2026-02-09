import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T;
  
  static int[][] magnet = new int[4][8];
  static int K;
  
  static void init() throws Exception {
    K = Integer.parseInt(br.readLine());
    
    for (int i = 0; i < 4; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j = 0; j < 8; j++) {
        magnet[i][j] = Integer.parseInt(st.nextToken());
      }
    }
  }
  
  static int process() throws Exception {
    for (int k = 0; k < K; k++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int idx = Integer.parseInt(st.nextToken()) - 1;
      int dir = Integer.parseInt(st.nextToken());
      simulate(idx, dir);
    }
    
    return calcScore();
  }
  
  static void simulate(int idx, int dir) {
    int[] rotateDir = new int[4];
    rotateDir[idx] = dir;
    
    // 왼쪽 전파
    for (int i = idx - 1; i >= 0; i--) {
      if (magnet[i][2] != magnet[i + 1][6]) {
        rotateDir[i] = -rotateDir[i + 1];
      } else {
        break;
      }
    }
    
    // 오른쪽 전파
    for (int i = idx + 1; i < 4; i++) {
      if (magnet[i - 1][2] != magnet[i][6]) {
        rotateDir[i] = -rotateDir[i - 1];
      } else {
        break;
      }
    }
    
    // 회전 실행
    for (int i = 0; i < 4; i++) {
      if (rotateDir[i] == 1) rotateClockwise(i);
      else if (rotateDir[i] == -1) rotateCounterClockwise(i);
    }
  }
  
  static void rotateClockwise(int idx) {
    int temp = magnet[idx][7];
    for (int i = 7; i > 0; i--) {
      magnet[idx][i] = magnet[idx][i - 1];
    }
    magnet[idx][0] = temp;
  }
  
  static void rotateCounterClockwise(int idx) {
    int temp = magnet[idx][0];
    for (int i = 0; i < 7; i++) {
      magnet[idx][i] = magnet[idx][i + 1];
    }
    magnet[idx][7] = temp;
  }
  
  static int calcScore() {
    int score = 0;
    for (int i = 0; i < 4; i++) {
      if (magnet[i][0] == 1) {
        score += (1 << i);
      }
    }
    return score;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 1; t <= T; t++) {
      init();
      int result = process();
      sb.append("#").append(t).append(" ").append(result).append("\n");
    }
    System.out.print(sb.toString());
  }
}
