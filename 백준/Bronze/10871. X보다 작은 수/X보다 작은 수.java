import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] arr = new int[n];
        int a, count = 0;
        for(int i = 0 ; i < n; i++) {
            a = sc.nextInt();
            if(a < x) {
                arr[count] = a;
                count++;
            }
        }
        for(int i = 0; arr[i] != 0; i++)
            System.out.print(arr[i] + " ");
    }
}
