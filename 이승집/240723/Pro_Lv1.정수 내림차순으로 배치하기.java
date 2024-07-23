import java.util.*;

public class Main {
    public static void main(String[] args) {

        long n = 118372;
        String[] list = String.valueOf(n).split("");

        Arrays.sort(list, Comparator.reverseOrder());
        System.out.println(Arrays.toString(list));

        StringBuilder sb = new StringBuilder();
        for (String a: list) sb.append(a);

        System.out.println(sb.toString());
    }
}
