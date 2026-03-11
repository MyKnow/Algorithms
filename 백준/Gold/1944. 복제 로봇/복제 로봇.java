import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Arrays;
import java.util.ArrayDeque;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  
  static int N, M;
  static int answer;
  
  static char[][] map;
  static int[][] id;
  
  static List<Node> nodes = new ArrayList<>();
  static List<Edge> edge = new ArrayList<>();
  
  static int[] parent;
  
  static int[] dr = {1,-1,0,0};
  static int[] dc = {0,0,1,-1};
  
  static class Node {
    int r, c;
    
    Node(int r, int c){
      this.r = r;
      this.c = c;
    }
  }
  
  static class Edge implements Comparable<Edge> {
    int u, v, w;
    
    Edge(int u, int v, int w){
      this.u = u;
      this.v = v;
      this.w = w;
    }
    
    @Override
    public int compareTo(Edge e){
      return this.w - e.w;
    }
  }
  
  static class State {
    int r, c, d;
    
    State(int r, int c, int d){
      this.r = r;
      this.c = c;
      this.d = d;
    }
  }
  
  static void init() throws Exception {
    StringTokenizer st = new StringTokenizer(br.readLine());
    
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    
    map = new char[N][N];
    id = new int[N][N];
    
    for(int i=0;i<N;i++) {
      Arrays.fill(id[i], -1);
    }
    
    for(int r=0;r<N;r++){
      String line = br.readLine();
      
      for(int c=0;c<N;c++){
        map[r][c] = line.charAt(c);
        
        if(map[r][c]=='S' || map[r][c]=='K'){
          id[r][c] = nodes.size();
          nodes.add(new Node(r,c));
        }
      }
    }
    
    parent = new int[nodes.size()];
    for(int i=0;i<parent.length;i++) {
      parent[i] = i;
    }
  }
  
  static void solve(){
    for(int i=0;i<nodes.size();i++) {
      bfs(i);
    }
    
    Collections.sort(edge);
    
    int cnt = 0;
    for(Edge e : edge){
      if(union(e.u,e.v)){
        answer += e.w;
        cnt++;
      }
    }
    
    if(cnt != nodes.size()-1) {
      answer = -1;
    }
    
    sb.append(answer).append("\n");
  }
  
  static void bfs(int idx){
    Node start = nodes.get(idx);
    
    boolean[][] visited = new boolean[N][N];
    visited[start.r][start.c] = true;
    
    ArrayDeque<State> q = new ArrayDeque<>();
    q.add(new State(start.r,start.c,0));
    
    while(!q.isEmpty()){
      State cur = q.poll();
      
      int r = cur.r;
      int c = cur.c;
      int d = cur.d;
      
      if(id[r][c] != -1 && id[r][c] != idx){
        edge.add(new Edge(idx, id[r][c], d));
      }
      
      for(int dir=0; dir<4; dir++){
        int nr = r + dr[dir];
        int nc = c + dc[dir];
        
        if(!isInRange(nr, nc)) continue;
        if(visited[nr][nc]) continue;
        if(map[nr][nc]=='1') continue;
        
        visited[nr][nc] = true;
        q.add(new State(nr,nc,d+1));
      }
    }
  }
  
  static boolean isInRange(int nr, int nc) {
    return 0 <= nr && nr < N && 0 <= nc && nc < N;
  }
  
  static int find(int x){
    if(parent[x]==x) return x;
    return parent[x] = find(parent[x]);
  }
  
  static boolean union(int a,int b){
    a = find(a);
    b = find(b);
    
    if(a==b) return false;
    
    parent[b] = a;
    return true;
  }
  
  public static void main(String[] args) throws Exception {
    init();
    solve();
    System.out.print(sb.toString());
  }
}