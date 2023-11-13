import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int len = str.length();
        for(char c = 'a'; c <= 'z'; c++) {
            for(int i = 0; i < len; i++) {
                if(str.charAt(i) == c) {
                    System.out.print(i + " ");
                    i = len;
                } else if(i == len - 1) {
                    System.out.print("-1 ");
                }
            }
        }
    }
}