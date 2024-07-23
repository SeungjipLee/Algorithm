public class Main {
    public static void main(String[] args) {
        int n = 123;
        String mid = String.valueOf(n);
        int answer = 0;

        for (int i = 0; i < mid.length(); i ++) {
            answer += Integer.parseInt(String.valueOf(mid.charAt(i)));
        }

        System.out.println(answer);

    }
}