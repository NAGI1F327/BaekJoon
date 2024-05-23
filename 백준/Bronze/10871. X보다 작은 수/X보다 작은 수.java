import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int anArray[] = new int[10000];
        int N = sc.nextInt();
        int X = sc.nextInt();
        
        for (int i = 0; i < N; i++) {
            anArray[i] = sc.nextInt();
                if (anArray[i] < X) {
                    System.out.print(anArray[i] + " ");
                }
        }
        sc.close();
    }
}