import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++) {
            String name = br.readLine();
            switch(name.charAt(0)) {
                case 'A':
                    if (name.charAt(1) == 'l') System.out.println("204");
                    else System.out.println("302");
                    break;
                case 'D':
                    System.out.println("207");
                    break;
                case 'C':
                    System.out.println("B101");
                    break;
                case 'N':
                    System.out.println("303");
                    break;
                case 'S':
                    System.out.println("501");
                    break;
                case 'T':
                    System.out.println("105");
                    break;
            }
        }
    }
}