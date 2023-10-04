import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int t = sc.nextInt();

        m += t;
        while(m >= 60) {
            m -= 60;
            h++;
            if(h >= 24)
                h -= 24;
        }
        System.out.printf("%d %d", h, m);
    }
}