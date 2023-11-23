import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for(int i = 0; i < 3; i++) {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int startHour = Integer.parseInt(st.nextToken());
            int startMinute = Integer.parseInt(st.nextToken());
            int startSecond = Integer.parseInt(st.nextToken());
            int endHour = Integer.parseInt(st.nextToken());
            int endMinute = Integer.parseInt(st.nextToken());
            int endSecond = Integer.parseInt(st.nextToken());
            int second = (endSecond - startSecond >= 0) ? endSecond - startSecond : endSecond - startSecond + 60;
            int minute = (endMinute - startMinute >= 0) ? endMinute - startMinute : endMinute - startMinute + 60;
            int hour = (endMinute - startMinute >= 0) ? endHour - startHour : endHour - startHour - 1;
            minute = (endSecond - startSecond >= 0) ? minute : minute - 1;
            hour = (minute >= 0) ? hour : hour - 1;
            minute = (minute >= 0) ? minute : minute + 60;
            System.out.printf("%d %d %d\n", hour, minute, second);
        }
    }
}