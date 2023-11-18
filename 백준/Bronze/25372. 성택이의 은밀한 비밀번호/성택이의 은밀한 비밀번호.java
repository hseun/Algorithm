import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            String code = br.readLine();
            if(code.length() >= 6 && code.length() <= 9)
                System.out.println("yes");
            else System.out.println("no");
        }
    }
}