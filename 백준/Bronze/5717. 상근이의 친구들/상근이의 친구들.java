import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int male = Integer.parseInt(st.nextToken());
        int female = Integer.parseInt(st.nextToken());
        while(male + female != 0) {
            System.out.println(male + female);
            str = br.readLine();
            st = new StringTokenizer(str);
            male = Integer.parseInt(st.nextToken());
            female = Integer.parseInt(st.nextToken());
        }
    }
}