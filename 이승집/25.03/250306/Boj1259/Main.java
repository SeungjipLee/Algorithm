import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        while (true) {
            int number = sc.nextInt();
            if (number == 0) {
                break;
            }
            String num = String.valueOf(number);
            String answer = "yes";
            for (int i=0; i<num.length()/2; i++) {
                if (num.charAt(i) != num.charAt(num.length()-i-1)) {
                    answer = "no";
                    break;
                }
            }
            System.out.println(answer);
        }
        sc.close();
    }
}