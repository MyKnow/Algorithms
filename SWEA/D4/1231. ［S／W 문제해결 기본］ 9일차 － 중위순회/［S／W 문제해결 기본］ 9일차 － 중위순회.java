import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();

  static int N;
  static Node[] pool;

  static class Node {
    int number;
    String value;
    Node parent, left, right;
    
    Node(int number, String value, Node parent) {
      this.number = number;
      this.value = value;
      this.parent = parent;
    }

    Node(int number, String value, Node parent, Node left, Node right) {
      this.number = number;
      this.value = value;
      this.parent = parent;
      this.left = left;
      this.right = right;
    }
  }

  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    pool = new Node[N+1];
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int number = Integer.parseInt(st.nextToken());
      String value = st.nextToken();
      
      if (pool[number] == null) {
        pool[number] = new Node(number, value, null);
      } else {
        pool[number].value = value;
      }
      
      int remainTokens = st.countTokens();
      if (remainTokens >= 1) {
        int left = Integer.parseInt(st.nextToken());
        if (pool[left] == null) pool[left] = new Node(left, null, pool[number]);
        pool[number].left = pool[left];
      }
      if (remainTokens == 2) {
        int right = Integer.parseInt(st.nextToken());
        if (pool[right] == null) pool[right] = new Node(right, null, pool[number]);
        pool[number].right = pool[right];
      }
    }
  }
  
  static void inorderTravelAt(Node node) {
    if (node == null) return;
    
    inorderTravelAt(node.left);
    sb.append(node.value);
    inorderTravelAt(node.right);
  }

  static void solve() {
    // 루트는 항상 1번
    Node root = pool[1];

    inorderTravelAt(root);
  }

  public static void main(String[] args) throws Exception {
    for (int t=1; t<=10; t++) {
      sb.append("#").append(t).append(" ");
      init();
      solve();
      sb.append("\n");
    }
    System.out.print(sb.toString());
  }
}