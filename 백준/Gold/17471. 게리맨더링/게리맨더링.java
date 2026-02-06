import java.util.*;
import java.io.*;

public class Main {
  static int N;
  static int[] people;
  static boolean[][] graph;
  static int[] isSelected;
  static boolean[] isUsed;
  static List<int[][]> combination = new ArrayList<>();
  static int combinationSize = 0;
  static int min = Integer.MAX_VALUE;
  
  static void init() throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    N = Integer.parseInt(br.readLine());
    
    people = new int[N+1];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i=1; i<=N; i++) {
      people[i] = Integer.parseInt(st.nextToken());
    }
    
    graph = new boolean[N+1][N+1];
    for (int src=1; src<=N; src++) {
      st = new StringTokenizer(br.readLine());
      int count = Integer.parseInt(st.nextToken());
      
      for (int i=0; i<count; i++) {
        int dst = Integer.parseInt(st.nextToken());
        graph[src][dst] = true;
        graph[dst][src] = true;
      }
    }
  }
  
  static void createCombination(int start, int depth, int limit) {
    if (depth == limit && limit != N) {
      int[][] result = new int[2][N+1];
      int firstSize = 0;
      int secondSize = 0;
      for (int i=1; i<=N; i++) {
        if (isUsed[i]) result[0][firstSize++] = i;
        else result[1][secondSize++] = i;
      }
      int[] firstSet = Arrays.copyOf(result[0], firstSize);
      int[] secondSet = Arrays.copyOf(result[1], secondSize);
      combination.add(new int[][] { firstSet, secondSet });
      return;
    }
    for (int i=start; i<=N; i++) {
      if (isUsed[i]) continue;
      isUsed[i] = true;
      createCombination(i+1, depth+1, limit);
      isUsed[i] = false;
    }
  }
  
  static int travelConstituency(int[] constituencies, boolean isFirst) {
    int start = constituencies[0];
    int sum = people[start];
    Deque<Integer> dq = new ArrayDeque<>();
    dq.addLast(start);
    int visit = (isFirst ? 1 : 2);
    isSelected[start] = visit;
    
    while(!dq.isEmpty()) {
      int src = dq.pollLast();
      
      for (int dst=1; dst<=N; dst++) {
        boolean[] inGroup = new boolean[N+1];
        for (int x : constituencies) inGroup[x] = true;
        if (graph[src][dst] && isSelected[dst] == 0 && inGroup[dst]) {
          isSelected[dst] = visit;
          sum+=people[dst];
          dq.addLast(dst);
        }
      }
    }
    
    return sum;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    for (int i=1; i<=N/2; i++) {
      isUsed = new boolean[N+1];
      createCombination(1, 0, i);
    }
    for (int[][] constituencies: combination) {
      isSelected = new int[N+1];
      int first = travelConstituency(constituencies[0], true);
      int second = travelConstituency(constituencies[1], false);
      int diff = Math.abs(first-second);
      
      boolean isValid = true;
      for (int i=1; i<=N; i++) {
        if (isSelected[i] == 0) {
          isValid = false;
          break;
        }
      }
      
      if (isValid) min = Math.min(min, diff);
    }
    if (min == Integer.MAX_VALUE) min = -1;
    System.out.println(min);
  }
}