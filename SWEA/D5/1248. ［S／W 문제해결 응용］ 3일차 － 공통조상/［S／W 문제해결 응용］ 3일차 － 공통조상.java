import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, answer_number, answer_size;

  static int V, E, target1, target2;
  static Node[] pool;

  static class Node {
    int number, subtreeSize;
    Node parent, left, right;

    Node(int number) {
      this.number = number;
      this.subtreeSize = 1;
    }

    void setChild(Node child) {
      if (left == null) left = child;
      else right = child;
      child.parent = this;
    }
  }

  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    V = Integer.parseInt(st.nextToken());
    E = Integer.parseInt(st.nextToken());
    target1 = Integer.parseInt(st.nextToken());
    target2 = Integer.parseInt(st.nextToken());

    pool = new Node[V+1];

    st = new StringTokenizer(br.readLine());
    for (int i=0; i<E; i++) {
      int parent = Integer.parseInt(st.nextToken());
      int child = Integer.parseInt(st.nextToken());

      if (pool[parent] == null) pool[parent] = new Node(parent);
      if (pool[child] == null) pool[child] = new Node(child);

      pool[parent].setChild(pool[child]);
    }
  }

  static int dfs(Node cur) {
    if (cur == null) return 0;

    int leftSize = dfs(cur.left);
    int rightSize = dfs(cur.right);

    cur.subtreeSize = leftSize + rightSize + 1;
    return cur.subtreeSize;
  }

  static Node findLCA(Node n1, Node n2) {
    boolean[] visited = new boolean[V+1];

    while (n1 != null) {
      visited[n1.number] = true;
      n1 = n1.parent;
    }

    while (n2 != null) {
      if (visited[n2.number]) return n2;
      n2 = n2.parent;
    }

    return null;
  }

  static void solve() {
    // 루트는 항상 1번
    Node root = pool[1];

    // subtree 계산
    dfs(root);

    // LCA 찾기
    Node lca = findLCA(pool[target1], pool[target2]);

    
    answer_number = lca.number;
    answer_size = lca.subtreeSize;
  }

  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    for (int t=1; t<=T; t++) {
      init();
      solve();
      sb.append("#").append(t).append(" ").append(answer_number).append(" ").append(answer_size).append("\n");
    }
    System.out.print(sb.toString());
  }
}