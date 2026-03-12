import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static final int HORSE_SIZE = 4;
  static final int ROLL_SIZE = 10;

  static int answer;

  static int[] dice = new int[ROLL_SIZE];
  static Node[] horse = new Node[HORSE_SIZE];
  static Node start;
  static Node finish;

  static class Node {
    int score;
    Node next;
    Node fork;

    Node(int score) {
      this.score = score;
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < ROLL_SIZE; i++) {
      dice[i] = Integer.parseInt(st.nextToken());
    }

    start = new Node(0);

    Node prev = start;
    Node[] main = new Node[21];

    for (int i = 1; i <= 20; i++) {
      Node cur = new Node(i * 2);
      main[i] = cur;
      prev.next = cur;
      prev = cur;
    }

    finish = new Node(0);
    prev.next = finish;

    Node n13 = new Node(13);
    Node n16 = new Node(16);
    Node n19 = new Node(19);

    Node n22 = new Node(22);
    Node n24 = new Node(24);

    Node n28 = new Node(28);
    Node n27 = new Node(27);
    Node n26 = new Node(26);

    Node n25 = new Node(25);
    Node n30 = new Node(30);
    Node n35 = new Node(35);

    main[5].fork = n13;
    main[10].fork = n22;
    main[15].fork = n28;

    n13.next = n16;
    n16.next = n19;
    n19.next = n25;

    n22.next = n24;
    n24.next = n25;

    n28.next = n27;
    n27.next = n26;
    n26.next = n25;

    n25.next = n30;
    n30.next = n35;
    n35.next = main[20];

    for (int i = 0; i < HORSE_SIZE; i++) {
      horse[i] = start;
    }
  }

  static void solve() {
    dfs(0, 0);
    sb.append(answer).append("\n");
  }

  static void dfs(int depth, int sum) {
    if (depth == ROLL_SIZE) {
      answer = Math.max(answer, sum);
      return;
    }

    int move = dice[depth];
    for (int i = 0; i < HORSE_SIZE; i++) {
      Node cur = horse[i];
      if (cur == finish)
        continue;

      Node next = move(cur, move);

      if (next != finish && isCollision(next)) {
        continue;
      }

      horse[i] = next;
      dfs(depth + 1, sum + next.score);
      horse[i] = cur;
    }
  }

  static Node move(Node cur, int move) {
    Node node = cur;

    if (node.fork != null) {
      node = node.fork;
    } else {
      node = node.next;
    }
    move--;

    while (move --> 0 && node != finish) {
      node = node.next;
    }
    return node;
  }

  static boolean isCollision(Node target) {
    for (Node h : horse) {
      if (h == target) {
        return true;
      }
    }
    return false;
  }

  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}