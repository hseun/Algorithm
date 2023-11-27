import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int apple1 = sc.nextInt();
        int orange1 = sc.nextInt();
        int apple2 = sc.nextInt();
        int orange2 = sc.nextInt();
        if(apple1 + orange2 > apple2 + orange1)
            System.out.println(apple2 + orange1);
        else System.out.println(apple1 + orange2);
    }
}