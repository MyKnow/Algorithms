import java.io.*;
import java.util.*;

public class Main {
  static int R, C, T;
  static int[][] before;
  static int[][] after;
  static int airPurifierR;
  static int airPurifierC;
  
  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = {  0, 0,-1, 1 };
  
  
  
  static boolean isInbound(int nr, int nc) {
    return ((0 <= nr && nr < R) && (0 <= nc && nc < C) && (before[nr][nc] != -1));
  }
  
  static int getDiffusionDust(int dust) {
    return (int) dust / 5;
  }
  
  static void spreadDust(int r, int c) {
    // 확산 사전조사
    int count = 0;
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d], nc = c+dc[d];
      if (isInbound(nr, nc)) count++;
    }
    
    // 확산
    int current = before[r][c];
    int diffusion = getDiffusionDust(current);
    int remain = current - diffusion * count;
    after[r][c] += remain;
    for (int d=0; d<dr.length; d++) {
      int nr = r+dr[d], nc = c+dc[d];
      if (isInbound(nr, nc)) after[nr][nc] += diffusion;
    }
  }
  
  static void counterClockwiseRotate() {
    int top = 0;
    int bottom = airPurifierR;
    int left = airPurifierC;
    int right = C-1;
    int length = 2 * (bottom-top+right-left);
    
    int[] flatMap = new int [length];
    after[bottom][left] = 0;
    int index = 0;
    for (int r=bottom; r>top; r--) flatMap[index++] = after[r][left];
    for (int c=left; c<right; c++) flatMap[index++] = after[top][c];
    for (int r=top; r<bottom; r++) flatMap[index++] = after[r][right];
    for (int c=right; c>left; c--) flatMap[index++] = after[bottom][c];
    
    index = 1 % length;
    for (int r=bottom; r>top; r--) after[r][left] = flatMap[index++ % length];
    for (int c=left; c<right; c++) after[top][c] = flatMap[index++ % length];
    for (int r=top; r<bottom; r++) after[r][right] = flatMap[index++ % length];
    for (int c=right; c>left; c--) after[bottom][c] = flatMap[index++ % length];
    
    after[bottom][left] = -1;
  }
  
  
  static void clockwiseRotate() {
    int top = airPurifierR+1;
    int bottom = R-1;
    int left = airPurifierC;
    int right = C-1;
    int length = 2 * (bottom-top+right-left);
    
    int[] flatMap = new int [length];
    after[top][left] = 0;
    int index = 0;
    for (int r=top; r<bottom; r++) flatMap[index++] = after[r][left];
    for (int c=left; c<right; c++) flatMap[index++] = after[bottom][c];
    for (int r=bottom; r>top; r--) flatMap[index++] = after[r][right];
    for (int c=right; c>left; c--) flatMap[index++] = after[top][c];
    
    index = 1 % length;
    for (int r=top; r<bottom; r++) after[r][left] = flatMap[index++ % length];
    for (int c=left; c<right; c++) after[bottom][c] = flatMap[index++ % length];
    for (int r=bottom; r>top; r--) after[r][right] = flatMap[index++ % length];
    for (int c=right; c>left; c--) after[top][c] = flatMap[index++ % length];
    
    after[top][left] = -1;
    
  }
  
  static int travelAfterMap() {
    int total = 0;
    for (int r=0; r<R; r++) {
      for (int c=0; c<C; c++) {
        int current = after[r][c];
        if (current == -1) continue;
        total += current;
      }
    }
    return total;
  }
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    StringTokenizer st = new StringTokenizer(br.readLine());
    R = Integer.parseInt(st.nextToken());
    C = Integer.parseInt(st.nextToken());
    T = Integer.parseInt(st.nextToken());
    
    before = new int[R][C];
    after = new int[R][C];
    
    boolean alreadyFound = false;
    for (int r=0; r<R; r++) {
      st = new StringTokenizer(br.readLine());
      for (int c=0; c<C; c++) {
        int current = Integer.parseInt(st.nextToken());
        if (current == -1 && !alreadyFound) {
          alreadyFound = true;
          airPurifierR = r; airPurifierC = c;
        } 
        before[r][c] = current;
      }
    }
    
    for (int t=0; t<T; t++) {
      after = new int[R][C];
      for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
          if (before[r][c] == -1) {
            after[r][c] = -1; continue;
          }
          spreadDust(r, c);
        }
      }
      counterClockwiseRotate();
      clockwiseRotate();
      before = after;
      
    }
    System.out.println(travelAfterMap());
  }
}