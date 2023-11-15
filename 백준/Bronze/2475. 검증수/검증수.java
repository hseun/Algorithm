import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int code, key = 0;
        for(int i = 0; i < 5; i++) {
            code = sc.nextInt();
            key += code * code;
        }
        key = key % 10;
        System.out.println(key);
    }
}