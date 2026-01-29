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
            Queue<Integer> valueQueue = new LinkedList<>();
            Queue<Integer> indexQueue = new LinkedList<>();

            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int N = Integer.parseInt(st.nextToken());
            int targetIndex = Integer.parseInt(st.nextToken());
            int targetValue = 0;

            st = new StringTokenizer(br.readLine().trim());
            for (int i=0; i<N; i++) {
                int currentValue = Integer.parseInt(st.nextToken());
                if (targetIndex == i) targetValue = currentValue;
                valueQueue.add(currentValue);
                indexQueue.add(i);
            }

            int count = 0;
            while (valueQueue.contains(targetValue) && indexQueue.contains(targetIndex)) {
                int valueFront = valueQueue.poll();
                int indexFront = indexQueue.poll();

                if (valueQueue.stream().anyMatch((priority) -> valueFront < priority)) {
                    valueQueue.offer(valueFront);
                    indexQueue.offer(indexFront);
                } else {
                    count++;
                }
            }
            System.out.println(count);
        }
    }
}
