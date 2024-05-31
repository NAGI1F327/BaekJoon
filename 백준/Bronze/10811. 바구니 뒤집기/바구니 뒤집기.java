import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        
        int[] baskets = new int[N];
        for (int i = 0; i < N; i++) {
            baskets[i] = i + 1;
        }
        
        for (int k = 0; k < M; k++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            
            for (int x = 0; x < (j - i + 1) / 2; x++) {
                int temp = baskets[i - 1 + x];
                baskets[i - 1 + x] = baskets[j - 1 - x];
                baskets[j - 1 - x] = temp;
            }
        }
        
        for (int num : baskets) {
            System.out.print(num + " ");
        }
    }
}