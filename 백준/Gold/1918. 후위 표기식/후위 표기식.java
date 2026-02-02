import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

// 등장하는 피연산자는 알파벳 대문자(A~Z)이다.
// 등장하는 표기식은 +, -, *, /, (, ) 이다.
// 길이는 100을 넘지 않는다.
// -A나 AB 같은 수식은 주어지지 않는다.

// 입력을 순회하며 아래 로직을 실행한다.
// 1. 피연산자는 operand 스택에 넣는다.
// 2. 표기식은 다음 로직으로 나뉜다.
//  +, -: 우선순위 가장 낮음. operator 스택의 top이
//        존재하면서, 자신보다 우선순위가 높다면 operand를 모두
//        StringBuilder에 pop하고 operator도 모두 pop한 뒤 자신을 추가한다.
//  *, /: 두번째 우선 순위. 단순히 operator에 추가된다.
//  (, ): 우선순위 가장 높음. 닫힌 괄호는 열린 괄호를 만나기 전까지의
//         표기식 처리를 강제로 진행한 뒤, 결과를 operand에 다시 넣는다.

// 피연산자의 순서는 절대 변하지 않는다.
// 피연산자 사이에 어떤 표기식이 무슨 순서로 들어가게 되는 지가 중요하다.

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static Deque<String> operator = new ArrayDeque<>();
    
    static int getPriority(String str) {
      if (str == null) return 0;
      
      if (str.equals(")")) return 4;
      else if (str.equals("*") || str.equals("/")) return 3;
      else if (str.equals("+") || str.equals("-")) return 2;
      else if (str.equals("(")) return 1;
      return 0;
    }
    
    static void reformat(int priority) {
      while(
        !operator.isEmpty() 
        && getPriority(operator.peek()) >= priority
        && !operator.peek().equals("(")) {
        sb.append(operator.pop());
      }
    }
    
    public static void main(String[] args) throws Exception {
      for (char ch: br.readLine().trim().toCharArray()) {
        String str = Character.toString(ch);
        if (getPriority(str) == 0) {
          sb.append(str);
        }
        else if (getPriority(str) == 2) {
          reformat(2);
          operator.push(str);
        }
        else if (getPriority(str) == 3) {
          reformat(3);
          operator.push(str);
        }
        else if (getPriority(str) == 4) {
            while (!operator.isEmpty() && !operator.peek().equals("(")) {
                sb.append(operator.pop());
            }
            operator.pop();
        }
        else {
          operator.push(str);
        }
      }
      
      while(!operator.isEmpty()) {
        sb.append(operator.pop());
      }
      
      System.out.println(sb);
  }
}