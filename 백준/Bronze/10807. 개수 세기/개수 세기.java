import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int anArray[] = new int[100];
        int N = sc.nextInt();
        int cnt = 0;
        
        for (int i = 0; i < N; i++) {
            anArray[i] = sc.nextInt();
        }
        
        int v = sc.nextInt();
        for (int j = 0; j < N; j++) {
            if(anArray[j] == v)
                cnt++;
        }
        System.out.println(cnt);
        
        sc.close();
    }
}