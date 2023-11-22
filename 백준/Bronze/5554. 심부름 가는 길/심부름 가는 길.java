import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int second = 0, minute;
        for(int i = 0; i < 4; i++)
            second += Integer.parseInt(br.readLine());
        minute = second / 60;
        second = second % 60;
        System.out.println(minute);
        System.out.println(second);
    }
}