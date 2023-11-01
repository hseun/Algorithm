import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[30];
        int a;
        for(int i = 0; i < 28; i++) {
            a = sc.nextInt();
            arr[a - 1]++;
        }
        for(int i = 0; i < 30; i++) {
            if(arr[i] == 0)
                System.out.println(i + 1);
        }
    }
}