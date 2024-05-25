import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int[] Box = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            Box[i] = i;
        }
        
        for (int m = 0; m < M; m++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int temp = Box[i];
            Box[i] = Box[j];
            Box[j] = temp;
        }
        
        for (int i = 1; i <= N; i++) {
            System.out.print(Box[i] + " ");
        }
        
        sc.close();
    }
}