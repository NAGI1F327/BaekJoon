import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] array = new int[9];
        int max = 0, p = 0;

        Scanner scanner = new Scanner(System.in);
        
        for (int i = 0; i < 9; i++) {
            array[i] = scanner.nextInt();
            if (max < array[i]) {
                max = array[i];
                p = i + 1;
            }
        }
		
        System.out.println(max);
        System.out.println(p);
        scanner.close();
    }
}