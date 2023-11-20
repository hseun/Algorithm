import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[3];
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        for(int i = 0; i < 3; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        for(int i = 0; i < 2; i++) {
            for(int j = i + 1; j < 3; j++) {
                if(arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        for(int i = 0; i < 3; i++)
            System.out.print(arr[i] + " ");
    }
}