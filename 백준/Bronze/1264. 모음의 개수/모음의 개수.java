import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        while(str.charAt(0) != '#') {
            int count = 0;
            int len = str.length();
            for(int i = 0; i < len; i++) {
                char c = str.charAt(i);
                if(c == 'A' || c == 'a' || c == 'E' || c == 'e' || c == 'I' || c == 'i' || c == 'O' || c == 'o' || c == 'U' || c == 'u')
                    count++;
            }
            System.out.println(count);
            str = br.readLine();
        }
    }
}