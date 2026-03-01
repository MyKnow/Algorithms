import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static final int SIZE = 9;
  static final int BOX_SIZE = 3;
  
  static int[][] board;
  static List<Coords> targets;
  static int length;
  
  static boolean[][] rowUsed;
  static boolean[][] colUsed;
  static boolean[][] boxUsed;
  
  static class Coords {
    int r, c;
    Coords(int r, int c) {
      this.r = r;
      this.c = c;
    }
  }
  
  static void init() throws Exception {
    board = new int[SIZE][SIZE];
    targets = new ArrayList<>();
    rowUsed = new boolean[SIZE][SIZE+1];
    colUsed = new boolean[SIZE][SIZE+1];
    boxUsed = new boolean[SIZE][SIZE+1];
    
    for (int r = 0; r < SIZE; r++) {
      char[] row = br.readLine().toCharArray();
      for (int c = 0; c < SIZE; c++) {
        int value = row[c] - '0';
        board[r][c] = value;
        
        if (value == 0) {
          targets.add(new Coords(r, c));
        } else {
          rowUsed[r][value] = true;
          colUsed[c][value] = true;
          boxUsed[getBoxIndex(r, c)][value] = true;
        }
      }
    }
    length = targets.size();
  }
  
  static void solve() {
    backtracking(0);
    appendBoardToSB();
  }
  
  static boolean backtracking(int index) {
    if (index == length) return true;
    
    Coords current = targets.get(index);
    int r = current.r;
    int c = current.c;
    int box = getBoxIndex(r, c);
    
    for (int value = 1; value <= SIZE; value++) {
      if (!rowUsed[r][value] &&
          !colUsed[c][value] &&
          !boxUsed[box][value]) {
        
        board[r][c] = value;
        rowUsed[r][value] = true;
        colUsed[c][value] = true;
        boxUsed[box][value] = true;
        
        if (backtracking(index + 1)) return true;
        
        board[r][c] = 0;
        rowUsed[r][value] = false;
        colUsed[c][value] = false;
        boxUsed[box][value] = false;
      }
    }
    return false;
  }
  
  static int getBoxIndex(int r, int c) {
    return (r / BOX_SIZE) * BOX_SIZE + (c / BOX_SIZE);
  }
  
  static void appendBoardToSB() {
    for (int r = 0; r < SIZE; r++) {
      for (int c = 0; c < SIZE; c++) {
        sb.append(board[r][c]);
      }
      sb.append("\n");
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}