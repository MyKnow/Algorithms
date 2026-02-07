import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class Node {
  Node next;
  int value;

  Node(int value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  Node head, tail;
  int size;

  LinkedList() {
    head = tail = null;
    size = 0;
  }

  void addLast(int value) {
    Node node = new Node(value);
    if (head == null) {
      head = tail = node;
    } else {
      tail.next = node;
      tail = node;
    }
    size++;
  }

  void addAt(int index, int value) {
    Node node = new Node(value);

    if (index == 0) {
      node.next = head;
      head = node;
      if (size == 0) tail = node;
      size++;
      return;
    }

    Node cur = head;
    for (int i=0; i<index-1; i++) cur = cur.next;

    node.next = cur.next;
    cur.next = node;
    if (node.next == null) tail = node;
    size++;
  }

  void deleteAt(int index, int count) {
    if (count == 0) return;

    if (index == 0) {
      Node cur = head;
      for (int i = 0; i < count && cur != null; i++) {
        cur = cur.next;
        size--;
      }
      head = cur;
      if (head == null) tail = null;
      return;
    }

    Node cur = head;
    for (int i = 0; i < index - 1; i++) cur = cur.next;

    Node del = cur.next;
    for (int i = 0; i < count && del != null; i++) {
      del = del.next;
      size--;
    }
    cur.next = del;
    if (del == null) tail = cur;
  }
}

public class Solution {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static StringTokenizer st;
  static final int T = 10;
  static LinkedList list;
  
  static void initList() throws Exception {
    int N = Integer.parseInt(br.readLine());
    list = new LinkedList();

    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      list.addLast(Integer.parseInt(st.nextToken()));
    }
  }
  
  static void processCommands() throws Exception {
    int M = Integer.parseInt(br.readLine());
    st = new StringTokenizer(br.readLine());

    for (int i = 0; i < M; i++) {
      char cmd = st.nextToken().charAt(0);

      if (cmd == 'I') {
        processInsert();
      } else if (cmd == 'D') {
        processDelete();
      } else if (cmd == 'A') {
        processAppend();
      }
    }
  }
  
  static void processInsert() throws Exception {
    int x = Integer.parseInt(st.nextToken());
    int y = Integer.parseInt(st.nextToken());
    for (int j = 0; j < y; j++) {
      list.addAt(x + j, Integer.parseInt(st.nextToken()));
    }
  }
  
  static void processDelete() throws Exception {
    int x = Integer.parseInt(st.nextToken());
    int y = Integer.parseInt(st.nextToken());
    list.deleteAt(x, y);
  }
  
  static void processAppend() {
    int y = Integer.parseInt(st.nextToken());
    for (int j = 0; j < y; j++) {
      list.addLast(Integer.parseInt(st.nextToken()));
    }
  }
   
  static void appendResult(int tc) {
    sb.append("#").append(tc).append(" ");
    Node cur_attach = list.head;
    for (int i = 0; i < 10; i++) {
      sb.append(cur_attach.value).append(" ");
      cur_attach = cur_attach.next;
    }
    sb.append("\n");
  }

  static void solveTestCase(int tc) throws Exception {
    initList();
    processCommands();
    appendResult(tc);
  }

  public static void main(String[] args) throws Exception {
    for (int tc = 1; tc <= T; tc++) {
      solveTestCase(tc);
    }
    System.out.print(sb.toString());
  }
}