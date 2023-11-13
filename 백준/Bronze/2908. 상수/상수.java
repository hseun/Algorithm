import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        num1 = ((num1 % 10) * 100) + ((num1 / 10 % 10) * 10) + (num1 / 100);
        num2 = ((num2 % 10) * 100) + ((num2 / 10 % 10) * 10) + (num2 / 100);
        int num;
        if(num1 > num2) num = num1;
        else num = num2;
        System.out.println(num);
    }
}