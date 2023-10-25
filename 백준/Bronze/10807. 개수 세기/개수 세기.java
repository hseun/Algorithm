import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] str = br.readLine().split(" ");
        int[] arr = new int[n];
        for(int i = 0; i < n; i++)
            arr[i] = Integer.parseInt(str[i]);
        int key = Integer.parseInt(br.readLine());
        int count = 0;
        for(int i = 0; i < n; i++) {
            if(arr[i] == key)
                count++;
        }
        System.out.println(count);
    }
}