import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[42];
        int n, count = 0;
        for(int i = 0; i < 10; i++) {
            n = sc.nextInt();
            arr[n % 42]++;
        }
        for(int i = 0; i < 42; i++)
            if(arr[i] != 0) count++;
        System.out.println(count);
    }
}