import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        a = sc.nextInt();
        b = sc.nextInt();
        int c, d, e;
        c = a * (b % 10);
        d = a * ((b / 10) % 10);
        e = a * (b / 100);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(c + (d * 10) + (e * 100));

    }
}
