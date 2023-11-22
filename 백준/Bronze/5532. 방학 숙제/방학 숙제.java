import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = Integer.parseInt(br.readLine());
        int korean = Integer.parseInt(br.readLine());
        int math = Integer.parseInt(br.readLine());
        int maxKor = Integer.parseInt(br.readLine());
        int maxMath = Integer.parseInt(br.readLine());
        int korDay = (korean % maxKor == 0) ? korean / maxKor : korean / maxKor + 1;
        int mathDay = (math % maxMath == 0) ? math / maxMath : math / maxMath + 1;
        if(korDay > mathDay) System.out.println(sum - korDay);
        else System.out.println(sum - mathDay);
    }
}