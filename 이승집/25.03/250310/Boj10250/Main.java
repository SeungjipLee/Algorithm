import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i=0; i<T; i++) {
            String[] inputs = br.readLine().split(" ");
            int H = Integer.parseInt(inputs[0]);
            int W = Integer.parseInt(inputs[1]);
            int N = Integer.parseInt(inputs[2]);

            int floor = (N % H == 0) ? H : N % H;
            int room = (N - 1) / H + 1;

            System.out.printf("%d%02d\n", floor, room);
        }
    }
}