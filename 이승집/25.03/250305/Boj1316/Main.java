import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        int cnt = N;

        for (int i = 0; i < N; i++) {
            String word = sc.nextLine();

            for (int j = 0; j < word.length() - 2; j++) {
                if (word.charAt(j) == word.charAt(j + 1)) {
                    continue;
                } else if (word.substring(j + 2).indexOf(word.charAt(j)) != -1) {
                    cnt--;
                    break;
                }
            }
        }

        System.out.println(cnt);
        sc.close();
    }
}
