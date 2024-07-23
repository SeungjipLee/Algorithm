import java.util.*;

public class Main {
    public static void main(String[] args) {

        long n = 121;

        ArrayList list = new ArrayList();

        long sqrtN = (long) Math.sqrt(n);

        for (long i = 1; i < Math.sqrt(n) + 1; i++) list.add(i*i);

        if (list.contains(n)) {
            long answer = (sqrtN + 1) * (sqrtN + 1);
            System.out.println(answer);
        } else {
            System.out.println(-1);
        }
    }
}
