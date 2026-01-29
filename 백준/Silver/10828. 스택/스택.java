import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
    final static int MAX_SIZE = 10_001;
    static StringBuilder sb = new StringBuilder();
    static int[] stack = new int[MAX_SIZE];
    static int pos;

    static void push(int X) {
        if (size() < MAX_SIZE) {
            stack[++pos] = X;
        }
    }

    static boolean empty() {
        return size() <= 0;
    }

    static int pop() {
        return empty() ? -1 : stack[pos--];
    }

    static int top() {
        return empty() ? -1 : stack[pos];
    }

    static int size() {
        return pos;
    }

    static void sbAppend(Object obj) {
        sb.append(obj).append("\n");
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine().trim());
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            String order = st.nextToken();
            switch (order) {
                case "push":
                    push(Integer.parseInt(st.nextToken()));
                    break;
                case "pop":
                    sbAppend(pop());
                    break;
                case "size":
                    sbAppend(size());
                    break;
                case "empty":
                    sbAppend(empty() ? 1 : 0);
                    break;
                case "top":
                    sbAppend(top());
                    break;
            }
        }
        System.out.print(sb.toString());
    }
}
