public class Main {
    public static void main(String[] args) {

        String s = "pPoooyY";
        boolean answer = true;
        int cntP = 0;
        int cntY = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'P' || s.charAt(i) == 'p') {
                cntP += 1;
            } else if (s.charAt(i) == 'Y' || s.charAt(i) == 'y') {
                cntY += 1;
            }
        }
        if (cntP != cntY) {
            answer = false;
        }
        System.out.println(answer);
    }
}