import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int Box[] = new int[N];
        
        for (int a = 0; a < M; a++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();
            
            for (int b = i - 1; b < j; b++) {
                Box[b] = k;
            }
        }
        
        for (int c = 0; c < Box.length; c++) {
            System.out.print(Box[c] + " ");
        }
        
        sc.close();
    }
}