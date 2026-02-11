import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.Comparator;

public class Main {
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  static StringBuilder sb = new StringBuilder();
  static int T, answer;
  static int N;
  static Applicant[] applicants;
  
  static class Applicant {
    int dScore, iScore;
    
    Applicant(int dScore, int iScore) {
      this.dScore = dScore;
      this.iScore = iScore;
    }
    
    public String toString() {
      return "applicant: " + dScore + " " + iScore;
    }
  }
  
  static void init() throws Exception {
    N = Integer.parseInt(br.readLine());
    
    applicants = new Applicant[N];
    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int bScore = Integer.parseInt(st.nextToken());
      int iScore = Integer.parseInt(st.nextToken());
      applicants[i] = new Applicant(bScore, iScore);
    }
    
    Arrays.sort(applicants, (a1, a2) -> Integer.compare(a1.dScore, a2.dScore));
  }
  
  static void solve() {
    int count = 1;
    int minInterview = applicants[0].iScore;
    for (int i=1; i<N; i++) {
      if (applicants[i].iScore < minInterview) {
          count++;
          minInterview = applicants[i].iScore;
      }
    }
    answer = count;
  }
  
  public static void main(String[] args) throws Exception {
    T = Integer.parseInt(br.readLine());
    
    for (int t = 0; t < T; t++) {
      init();
      solve();
      sb.append(answer).append("\n");
    }
    System.out.print(sb.toString());
  }
}