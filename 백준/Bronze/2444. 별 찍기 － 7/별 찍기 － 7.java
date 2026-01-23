import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static String repeat(char ch, int count) {
        StringBuilder sb = new StringBuilder(count);
        for (int i = 0; i < count; i++) {
            sb.append(ch);
        }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N;
        try {
            N = Integer.parseInt(br.readLine());
        } catch (Exception e) {
            N = 1;
        }

        // 위쪽 (중앙 포함)
        for (int i = 0; i < N; i++) {
            System.out.print(repeat(' ', N - i - 1));
            System.out.println(repeat('*', 2 * i + 1));
        }

        // 아래쪽
        for (int j = 0; j < N - 1; j++) {
            System.out.print(repeat(' ', j + 1));
            System.out.println(repeat('*', 2 * (N - j - 2) + 1));
        }
    }
}