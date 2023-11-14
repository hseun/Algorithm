import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long n, m, result;
        n = sc.nextLong();
        m = sc.nextLong();
        result = n - m;
        if (result < 0) result *= -1;
        System.out.println(result);
    }
}
