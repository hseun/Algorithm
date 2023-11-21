import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int plus = sc.nextInt();
        int minus = sc.nextInt();
        int r1 = (plus + minus) / 2;
        int r2 = plus - r1;
        if(r1 < 0 || r2 < 0 || r1 + r2 != plus || r1 - r2 != minus)
            System.out.println("-1");
        else System.out.printf("%d %d", r1, r2);
    }
}