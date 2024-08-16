import java.io.*;
import java.util.*;

public class BOJ_24445 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st;
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    static boolean[] visited;
    static int[] result;
    static int count = 1;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        result = new int[n+1];

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
        visited = new boolean[n+1];

        bfs(r);
        for (int i = 1; i <= n; i++) {
            bw.write(result[i] + "\n");
        }
        bw.flush();
        bw.close();
        br.close();

    }

    static void bfs(int x) {
        Queue<Integer> queue = new LinkedList<>();
        visited[x] = true;
        result[x] = count++;
        queue.add(x);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            graph.get(node).sort(Collections.reverseOrder());
            for (Integer next : graph.get(node)) {
                if (!visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                    result[next] = count++;
                }
            }
        }

    }
}
