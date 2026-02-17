import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  final static int PAPER_SIZE = 10;
  final static int COLOR_PAPER_SIZE = 5;
  final static int COLOR_PAPER_COUNT = 5;
  static int minUsed;
  static boolean[][] paper;
  static int[] colorPaper;
  
  static class Coordinate {
    int r, c;
    Coordinate(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
  
  static void init() throws Exception {
    paper = new boolean[PAPER_SIZE][PAPER_SIZE];
    for (int r=0; r<PAPER_SIZE; r++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int c=0; c<PAPER_SIZE; c++) {
        paper[r][c] = (Integer.parseInt(st.nextToken()) == 1);
      }
    }
    
    colorPaper = new int[COLOR_PAPER_SIZE+1];
    for (int i=1; i<=COLOR_PAPER_SIZE; i++) {
      colorPaper[i] = COLOR_PAPER_COUNT;
    }
    minUsed = Integer.MAX_VALUE;
  }
  
  static void solve() {
    backtracking(0);
    
    if (minUsed == Integer.MAX_VALUE) minUsed = -1;
  }
  
  static void backtracking(int used) {
    if (used >= minUsed) return;
    
    Coordinate coords = findNextCoords();
    if (coords == null) {
      minUsed = used;
      return;
    }
    
    int r = coords.r;
    int c = coords.c;
    for (int size=5; size>=1; size--) {
      if (canAttachAt(r, c, size)) {
        attachAt(r, c, size);
        backtracking(used+1);
        detachAt(r, c, size);
      }
    }
  }
  
  static Coordinate findNextCoords() {
    for (int r=0; r<PAPER_SIZE; r++) {
      for (int c=0; c<PAPER_SIZE; c++) {
        if (paper[r][c]) return new Coordinate(r, c);
      }
    }
    return null;
  }
  
  static boolean canAttachAt(int r, int c, int size) {
    int remainPaper = colorPaper[size];
    if (remainPaper <= 0) {
      return false;
    }
    
    for (int dr=0; dr<size; dr++) {
      for (int dc=0; dc<size; dc++) {
        int nr = r+dr;
        int nc = c+dc;
        if (!isInRange(nr, nc) || !paper[nr][nc]) return false;
      }
    }
    return true;
  }
  
  static void attachAt(int r, int c, int size) {
    colorPaper[size]--;
    for (int dr=0; dr<size; dr++) {
      for (int dc=0; dc<size; dc++) {
        paper[r+dr][c+dc] = false;
      }
    }
  }
  
  static void detachAt(int r, int c, int size) {
    colorPaper[size]++;
    for (int dr=0; dr<size; dr++) {
      for (int dc=0; dc<size; dc++) {
        paper[r+dr][c+dc] = true;
      }
    }
  }
  
  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < PAPER_SIZE && 0 <= nc && nc < PAPER_SIZE;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    sb.append(minUsed).append("\n");
    System.out.print(sb.toString());
  }
}