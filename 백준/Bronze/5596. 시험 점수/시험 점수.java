import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] sum = new int[2];
        for(int i = 0; i < 2; i++) {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            for(int j = 0; j < 4; j++)
                sum[i] += Integer.parseInt(st.nextToken());
        }
        if(sum[1] > sum[0]) System.out.println(sum[1]);
        else System.out.println(sum[0]);
    }
}