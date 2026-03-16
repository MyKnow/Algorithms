import java.util.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
	static int N, M, X;
	static List<Edge>[] edge;
	static int[] times;
	static int answer;
	
	static class Edge implements Comparable<Edge> {
		int to, time;

		public Edge(int to, int time) {
			super();
			this.to = to;
			this.time = time;
		}

		public int compareTo(Edge o) {
			return Integer.compare(this.time, o.time);
		}
	}
	
	@SuppressWarnings("unchecked")
	static void init() throws Exception {
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken());
		
		edge = new ArrayList[N+1];
		for (int n=1; n<=N; n++) edge[n] = new ArrayList<Edge>();
		
		for (int m=0; m<M; m++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			
			edge[from].add( new Edge(to, time) );
		}
		
		times = new int[N+1];
		answer = 0; 
	}
	
	static void solve() {
		int[] dijkstraX = dijkstra(X);
		for (int n=1; n<=N; n++) {
			answer = Math.max(answer, dijkstra(n)[X] + dijkstraX[n]);
		}
		
	}
	
	static int[] dijkstra(int start) {
		int[] time = new int[N+1];
		Arrays.fill(time, Integer.MAX_VALUE);
		PriorityQueue<Edge> pq = new PriorityQueue<Edge>();
		pq.add( new Edge(start, 0) );
		time[start] = 0;
		
		while(!pq.isEmpty()) {
			Edge cur = pq.poll();
			
			if (cur.time > time[cur.to]) continue;
			
			for (Edge next: edge[cur.to]) {
				int nextTime = cur.time + next.time;
				
				if (nextTime > time[next.to]) continue;
				
				pq.add( new Edge(next.to, nextTime) );
				time[next.to] = nextTime; 
			}
		}
		
		return time;
	}
	
	public static void main(String[] args) throws Exception {
		init();
		solve();
		System.out.println(answer);
	}
}