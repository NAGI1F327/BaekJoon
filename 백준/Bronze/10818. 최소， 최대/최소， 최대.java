import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int min = 1000000, max = -1000000;
        int N = scanner.nextInt();
        int[] array = new int[N];
		
        for (int i = 0; i < N; i++) {
            array[i] = scanner.nextInt();
            
			if (min > array[i]) { 
				min = array[i]; 
			} 
			if (max < array[i]) { 
			max = array[i]; 
			}
        }
		
        System.out.println(min + " " + max);
        scanner.close();
    }
}