import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;

public class BFSPrac {
	private static int node;
	private static int line;
	private static int start;
	private static int[][] map;
	private static boolean[] visit;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] temp= br.readLine().trim().split(" ");
		node = Integer.parseInt(temp[0]);
		line = Integer.parseInt(temp[1]);
		start = Integer.parseInt(temp[2]);
		map = new int[node+1][node+1];
		visit = new boolean[node+1];
		for(int i=0 ; i<line ; i++) {
			temp = br.readLine().trim().split(" ");
			int x = Integer.parseInt(temp[0]);
			int y = Integer.parseInt(temp[1]);
			map[x][y] = map[y][x] = 1;
		}
		
		bfs(start, node);
	}
	
	private static void bfs(int st, int n) {
		Queue<Integer> queue = new<Integer> LinkedList();
		int buf;
		
		queue.offer(st);
		while(!queue.isEmpty()) {
			buf = queue.poll();
			visit[buf] = true;
			System.out.print(st+ " ");
			for(int i=1 ; i<= n ; i++) {
				if(map[buf][i]==1 && !visit[i]) {
					queue.offer(i);
					visit[i] = true;
				}
			}
		}
	}
}
