import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a, b;
        for(int i = 0; i < n; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            System.out.printf("Case #%d: %d\n", i + 1, a + b);
        }
    }
}