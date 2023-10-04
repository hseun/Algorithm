import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        int n3 = sc.nextInt();
        int sum;

        if(n1 == n2 && n2 == n3) {
            sum = 10000 + n1 * 1000;
        } else if(n1 == n2 || n1 == n3) {
            sum = 1000 + n1 * 100;
        } else if(n2 == n3) {
            sum = 1000 + n2 * 100;
        } else {
            if(n1 > n2 && n1 > n3) {
                sum = n1 * 100;
            } else if(n2 > n1 && n2 > n3) {
                sum = n2 * 100;
            } else {
                sum = n3 * 100;
            }
        }
        System.out.println(sum);
    }
}