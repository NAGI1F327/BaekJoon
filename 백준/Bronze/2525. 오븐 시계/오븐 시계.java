import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int H = sc.nextInt();
    int M = sc.nextInt();
    int m = sc.nextInt();
    
    H += m / 60;
	M += m % 60;
    
	if (M >= 60) {
		++ H;
		M -= 60;
	}
	if (H >= 24) {
		H -= 24;
	}
    System.out.println(H + " " + M);
    
    sc.close();
  }
}