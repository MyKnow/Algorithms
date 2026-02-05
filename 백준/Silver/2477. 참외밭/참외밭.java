import java.util.*;
import java.io.*;

// 1. 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
// 2. 참외밭은 ㄱ-자가 회전한 모양이므로, 전체 넓이를 구하고 일부분을 빼면 된다.
//  2-1. 예제에서 전체 사각형의 넓이는 8000이고, 공백 사각형은 1200이므로 실 넓이는 6800이다.
// 3. 전체의 가로/세로 길이는 동/서, 남/북 중에서 한 번만 등장하는 것이다.
//  3-1. 예제에서는 4(북쪽), 2(서쪽)이 한 번씩 주어졌으므로, 4와 2의 길이를 곱하면 된다.
// 4. 공백의 길이는 방문 경로를 직렬화했을 때, 중복이 존재하는 4개의 이동경로 중 중간에 끼어있는 경로이다.
//  4-1. 예제에서는 4, 2, 3, 1, 3, 1로 이동하므로 3, 4번 인덱스의 경로 길이가 해당된다.
// 5. 따라서 중복이 존재하는 구간의 방향을 기록하고, 순회 시 해당 경로를 발견한다면,
//    본인 이전과 이후에 해당 방향이 존재하는 경로의 길이를 기록하고, 그 경로들의 길이를 곱하여 산출하면 된다.

public class Main {
  final static int rotateSize = 6;
  final static int routeSize = 4;
  
  static int melon;
  static int[][] routes = new int[rotateSize+2][2];
  static int[] routeDistances = new int[routeSize+1];
  static int[] count = new int[routeSize+1];
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    melon = Integer.parseInt(br.readLine());
    
    for (int i=0; i<rotateSize; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int route = Integer.parseInt(st.nextToken());
      int distance = Integer.parseInt(st.nextToken());
      routes[i] = new int[] { route, distance };
      count[route]++;
      routeDistances[route] = distance;
    }
    
    for (int i=0; i<2; i++) {
      routes[rotateSize+i] = routes[i];
    }
    
    int total = 1;
    for (int i=1; i<=routeSize; i++) {
      if (count[i] == 1) total *= routeDistances[i];
    }
    
    int sub = 1;
    for (int i=1; i<rotateSize+1; i++) {
      int route = routes[i][0];
      int distance = routes[i][1];
      if (count[route] == 2 && count[routes[i-1][0]] == 2 && count[routes[i+1][0]] == 2)  {
        sub *= distance;
      }
    }
    
    System.out.println((total-sub) * melon);
  }
}