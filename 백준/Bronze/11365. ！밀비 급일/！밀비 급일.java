import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.StringBuffer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true) {
            String code = br.readLine();
            if(code.charAt(0) == 'E' && code.charAt(1) == 'N' && code.charAt(2) == 'D') break;
            StringBuffer sb = new StringBuffer(code);
            System.out.println(sb.reverse());
        }
    }
}