import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

// 1. 여는 괄호를 스택에 넣는다.
// 2. 닫는 괄호를 만나면 여는 괄호까지 POP하여 계산을 시작한다.
//  2-1. 올바른 여는 괄호를 못 찾으면 0을 반환하고 종료한다.
// 3. 닫는 괄호부터 여는 괄호 사이에 숫자가 있다면, 여는 괄호 종류 * 숫자 합을 계산한다
// 4. 계산 결과를 다시 스택에 넣는다.
// 5. 2~4를 반복하면 결과적으로 스택에 숫자만 남는다.
    // 괄호가 남아있다면 0을 반환하고 종료한다.
// 6. 남은 숫자를 모두 더하여 출력한다.

// 반례
// 1. ]() -> line: 36
// 2. ())() -> line: 64

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Object> stack = new Stack<>();

        char[] line = br.readLine().toCharArray();
        for (int i=0; i<line.length; i++) {
            char ch = line[i];

            // 1. 여는 괄호 push
            if (ch == '(' || ch == '[') {
                stack.push(ch);
                continue;
            }

            // 처음인데 여는 괄호 못 찾음
            if (i == 0) {
                System.out.println(0);
                return;
            }

            // 2. 닫는 괄호 처리
            int base = (ch == ')') ? 2 : 3;
            char open = (ch == ')') ? '(' : '[';

            int sum = 0;

            // 여는 괄호까지 pop
            while (!stack.isEmpty()) {
                Object top = stack.pop();

                if (top instanceof Integer) {
                    sum += (int) top;
                } else if ((char) top == open) {
                    stack.push(sum == 0 ? base : sum * base);
                    break;
                } else {
                    // 괄호 불일치
                    System.out.println(0);
                    return;
                }
            }

            // 제일 앞에 여는 괄호가 없는 경우
            if (stack.isEmpty() && sum != 0) {
                System.out.println(0);
                return;
            }
        }

        // 3. 최종 합산
        int total = 0;
        for (Object obj : stack) {
            if (!(obj instanceof Integer)) {
                System.out.println(0);
                return;
            }
            total += (int) obj;
        }

        System.out.println(total);
    }
}