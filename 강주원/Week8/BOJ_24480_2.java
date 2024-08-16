import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class BOJ_24480_2 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> graph;
    static boolean[] visited;
    static int[] result;
    static int count = 1;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        visited = new boolean[n+1];
        result = new int[n+1];
        graph = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        dfs(r);
        for (int i = 1; i <= n; i++) {
            bw.write(result[i] + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int start) {
        visited[start] = true;
        result[start] = count++;
        Collections.sort(graph.get(start), Collections.reverseOrder());
        for (Integer value : graph.get(start)) {
            if (!visited[value]) {
                dfs(value);
            }
        }
    }
}
