import java.util.*;
import java.io.*;

// 단순 4중 반복문을 돌리면?
// N이 최대 4000이므로, 4000^4 = 2.56 x 10^14
// 1초에 10^9번 연산해도 약 3일이 소요된다.
// 아무리 머리를 굴려봐도 4개의 배열의 쌍을 검사할 방법이 생각나지 않는다.

// GPT 찬스
// 새로운 알고리즘: Meet In The Middle
// 탐색 공간을 절반으로 쪼개서, 각 절반의 결과를 미리 계산한 뒤 "중간에서 맞춘다".
//
// 형식
// f(a, b, c, d) = 0 -> f(a, b) + g(c, d) = 0
// 독립적인 두 부분으로 분리 가능한 경우에만 성립
//
// 적용
// 1. a + b + c + d = 0을 충족해야 한다.
// 2. (a + b) + (c + d) = 0과 같이 결합 법칙을 적용할 수 있다.
//
// 구현
// 1. A~D 배열을 담을 int[4][N] 선언
// 2. AB[N*N]과 CD[N*N]에 각 배열끼리의 합연산쌍을 저장
// 3. AB, CD의 요소를 오름차순 정렬
// 4. 투포인터를 통해서 쌍의 개수 업데이트(이 때 최대 2.56 x 10^14개의 쌍이 생성 될 수 있으므로 long 자료형 사용)

public class Main {
  static int N;
  static int[][] arr;
  static int[] AB;
  static int[] CD;
  
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    arr = new int[4][N];
    
    int size = N*N;
    AB = new int[size];
    CD = new int[size];
    
    for (int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      for (int j=0; j<4; j++) arr[j][i] = Integer.parseInt(st.nextToken());
    }
    
    int index = 0;
    for (int i=0; i<N; i++) {
      for (int j=0; j<N; j++) {
        AB[index] = arr[0][i] + arr[1][j];
        CD[index++] = arr[2][i] + arr[3][j];
      }
    }
    
    Arrays.sort(AB);
    Arrays.sort(CD);
    
    int left = 0;
    int right = size-1;
    long ans = 0;
    while(left < size && right >= 0) {
      int sum = AB[left] + CD[right];
      if (sum == 0) {
        int aValue = AB[left], bValue = CD[right];
        long aCount = 0, bCount = 0;
        
        while(left < size && AB[left] == aValue) {
          aCount++;
          left++;
        }
        while(right >= 0 && CD[right] == bValue) {
          bCount++;
          right--;
        }
        ans += aCount * bCount;
      }
      else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
    
    System.out.println(ans);
  }
}