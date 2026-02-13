import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int operandSize;
  static int operatorSize;
  static int[] operands;
  static int[] operators;
  static int minValue;
  static int maxValue;
  
  static void init() throws Exception {
    operandSize = Integer.parseInt(br.readLine());
    operatorSize = 4;
    
    operands = new int[operandSize];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i=0; i<operandSize; i++) {
      operands[i] = Integer.parseInt(st.nextToken());
    }
    
    operators = new int[operatorSize];
    st = new StringTokenizer(br.readLine());
    for (int i=0; i<operatorSize; i++) {
      operators[i] = Integer.parseInt(st.nextToken());
    }
    
    minValue = Integer.MAX_VALUE;
    maxValue = Integer.MIN_VALUE;
  }
  
  static void solve(int depth, int result) {
    if (depth == operandSize) {
      minValue = Math.min(minValue, result);
      maxValue = Math.max(maxValue, result);
      return;
    }
    
    for (int i=0; i<operatorSize; i++) {
      int remainCount = operators[i];
      int currentOperand = operands[depth];
      
      if (remainCount <= 0) continue;
      
      operators[i]--;
      
      // 더하기
      if (i == 0) {
        solve(depth+1, result + currentOperand);
      }
      // 빼기
      else if (i == 1) {
        solve(depth+1, result - currentOperand);
      }
      // 곱하기
      else if (i == 2) {
        solve(depth+1, result * currentOperand);
      }
      // 나누기
      else {
        solve(depth+1, (result < 0) ? (-1 * result / currentOperand) * -1 : result / currentOperand);
      }
      
      operators[i]++;
    }
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve(1, operands[0]);
    sb.append(maxValue).append("\n");
    sb.append(minValue).append("\n");
    System.out.print(sb.toString());
  }
}