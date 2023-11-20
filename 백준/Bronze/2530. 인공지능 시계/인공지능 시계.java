import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int during = sc.nextInt();
        s += during;
        m += s / 60;
        s = (s >= 60) ? s % 60 : s;
        h += m / 60;
        m = (m >= 60) ? m % 60 : m;
        h = (h >= 24) ? h % 24 : h;
        System.out.printf("%d %d %d", h, m, s);
    }
}