import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class DFSPrac {
	private static int node;
	private static int line;
	private static int start;
	private static boolean[] visit;
	private static int[][] map;
	private static int x;
	private static int y;
	
	public static void main(String[] args) throws NumberFormatException,IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] temp;
		
		temp = br.readLine().trim().split(" ");
		node = Integer.parseInt(temp[0]);
		line = Integer.parseInt(temp[1]);
		start = Integer.parseInt(temp[2]);
		map = new int[node+1][node+1];
		visit = new boolean[node+1];
		
		while(line>0) {
			temp = br.readLine().trim().split(" ");
			x = Integer.parseInt(temp[0]);
			y = Integer.parseInt(temp[1]);
			map[x][y] = map[y][x] = 1;
			line--;
		}
		 
		dfs(start, node);
	}
	
	private static void dfs(int st, int n) {
		if(visit[st]==true)
			return;
		
		visit[st]=true;
		System.out.print(st + " ");
		
		for(int i=0 ; i<=n ; i++) {
			if(map[st][i]==1)
				dfs(i,n);
		}
	}
}
