import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int len = str.length();
        int time = 0;
        for(int i = 0; i < len; i++) {
            char c = str.charAt(i);
            if(c >= 'A' && c <= 'C') {
                time += 1;
            } else if (c >= 'D' && c <= 'F') {
                time += 2;
            } else if (c >= 'G' && c <= 'I') {
                time += 3;
            } else if(c >= 'J' && c <= 'L') {
                time += 4;
            } else if(c >= 'M' && c <= 'O') {
                time += 5;
            } else if(c >= 'P' && c <= 'S') {
                time += 6;
            } else if(c >= 'T' && c <= 'V') {
                time += 7;
            } else if(c >= 'W' && c <= 'Z') {
                time += 8;
            }
            time += 2;
        }
        System.out.println(time);
    }
}