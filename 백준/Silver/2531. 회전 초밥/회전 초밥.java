import java.io.*;
import java.util.*;

public class Main {
    static int N, d, k, c;
    static int[] sushi;
    static int[] count;
    
    static int getBonus() {
      return (count[c] == 0 ? 1 : 0);
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        sushi = new int[N];
        for (int i = 0; i < N; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        count = new int[d + 1];
        int kind = 0;
        for (int i = 0; i < k; i++) {
            if (count[sushi[i]] == 0) kind++;
            count[sushi[i]]++;
        }
        int answer = kind + getBonus();

        for (int i = 1; i < N; i++) {
            int remove = sushi[i - 1];
            if (--count[remove] == 0) kind--;

            int add = sushi[(i + k - 1) % N];
            if (count[add]++ == 0) kind++;

            int current = kind + getBonus();
            answer = Math.max(answer, current);
        }

        System.out.println(answer);
    }
}