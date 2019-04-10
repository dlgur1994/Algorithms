import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class DFSPrac {
	private static int node;
	private static int line;
	private static int start;
	private static int[][] map;
	private static boolean[] visit;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp = br.readLine().trim().split(" ");
		
		node = Integer.parseInt(temp[0]);
		line = Integer.parseInt(temp[1]);
		start = Integer.parseInt(temp[2]);
		map = new int[node+1][node+1];
		visit = new boolean[node+1];
		while(line>0) {
			temp = br.readLine().trim().split(" ");
			int x = Integer.parseInt(temp[0]);
			int y = Integer.parseInt(temp[1]);
			map[x][y] = map[y][x] = 1;
			line--;
		}
		
		dfs(start, node);
	}
	
	private static void dfs(int s, int n) {
		if(visit[s]==true)
			return;
		
		visit[s] = true;
		System.out.print(s+" ");
		
		for(int i=0 ; i<=n ;i++) {
			if(map[s][i] == 1)
				dfs(i, n);
		}
			
	}
}
