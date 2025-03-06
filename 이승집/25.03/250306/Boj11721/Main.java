import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int n = 0;
        while (n + 10 < input.length()) {
            System.out.println(input.substring(n, n+10));
            n += 10;
        }
        System.out.println(input.substring(n));
        sc.close();
    }
}