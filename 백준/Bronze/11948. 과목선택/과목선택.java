import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] score = new int[4];
        for(int i = 0; i < 4; i++)
            score[i] = Integer.parseInt(br.readLine());
        int sum = 0;
        for(int i = 0; i < 2; i++) {
            int temp = Integer.parseInt(br.readLine());
            if(temp > sum) sum = temp;
        }
        Arrays.sort(score);
        for(int i = 1; i < 4; i++)
            sum += score[i];
        System.out.println(sum);
    }
}