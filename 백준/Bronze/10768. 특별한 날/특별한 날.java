import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        int d = Integer.parseInt(br.readLine());
        if(m == 2 && d == 18)
            System.out.println("Special");
        else if(m < 2 || (m == 2 && d < 18))
            System.out.println("Before");
        else System.out.println("After");
    }
}