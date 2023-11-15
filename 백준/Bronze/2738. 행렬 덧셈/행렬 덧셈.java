import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] arrA = new int[n][m];
        int[][] arrB = new int[n][m];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                arrA[i][j] = sc.nextInt();
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                arrB[i][j] = sc.nextInt();
        for(int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                System.out.printf("%d ", arrA[i][j] + arrB[i][j]);
            System.out.println();
        }
    }
}