import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int part1 = (int) (n * (78 / 100.0));
        int temp = (int) (n * (80 / 100.0));
        int part2 = (int) (temp + ((n - temp) * (78 / 100.0)));
        System.out.printf("%d %d", part1, part2);
    }
}