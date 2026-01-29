import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 1. Queue 가장 앞에 있는 문서의 중요도를 확인한다.
// 2. 이 문서보다 중요도가 더 높은 문서가 있다면 다시 큐에 넣는다.
// 3. 중요도가 가장 높은 문서라면 인쇄한다.
// 4. 주어진 인덱스의 문서가 인쇄되는 순번을 출력한다.

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim());
        for (int t=0; t<T; t++) {
            Queue<int[]> queue = new LinkedList<>();
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int targetIndex = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine().trim());
            for (int i=0; i<N; i++) {
                int currentValue = Integer.parseInt(st.nextToken());
                queue.add(new int[] {i, currentValue});
            }

            int count = 0;
            while (!queue.isEmpty()) {
                int[] front = queue.poll();
                int index = front[0];
                int priority = front[1];
                boolean hasHigher = false;

                for (int[] q: queue) {
                    if (priority < q[1]) {
                        hasHigher = true;
                        break;
                    }
                }

                if (hasHigher) {
                    queue.offer(front);
                } else {
                    count++;
                    if (index == targetIndex) {
                        break;
                    }
                }
            }
            System.out.println(count);
        }
    }
}
