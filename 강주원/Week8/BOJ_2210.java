import java.io.*;
import java.util.*;

public class BOJ_2210 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] board;
    static Set<String> res;
    static int[][] directions = {{1,0}, {0,1}, {-1,0}, {0,-1}};
    public static void main(String[] args) throws IOException {
        board = new int[5][5];
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        res = new HashSet<>();
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                bfs(i,j);
            }
        }

        System.out.println(res.size());
        br.close();
    }

    static void bfs(int x, int y) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(x, y, 1, String.valueOf(board[x][y])));
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            x = node.x;
            y = node.y;
            int cnt = node.cnt;
            String s = node.s;
            if (cnt == 6) {
                res.add(s);
                continue;
            }
            for (int[] dir : directions) {
                int nx = x + dir[0];
                int ny = y + dir[1];
                if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5) {
                    continue;
                }
                String ns = s + board[nx][ny];
                queue.add(new Node(nx, ny, cnt+1, ns));
            }
        }
    }
    static class Node {
        int x, y, cnt;
        String s;

        Node(int x, int y, int cnt, String s) {
            this.x = x;
            this.y = y;
            this.cnt = cnt;
            this.s = s;
        }
    }
}
