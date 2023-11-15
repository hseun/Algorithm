import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String result = "";
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) >= 'A' && str.charAt(i) <= 'Z')
                result += (char)(str.charAt(i) + 32);
            else if (str.charAt(i) >= 'a' && str.charAt(i) <= 'z')
                result += (char)(str.charAt(i) - 32);
        }
        System.out.println(result);
    }
}