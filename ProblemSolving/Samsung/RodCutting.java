import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class RodCutting {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int rod;
		int[] cost;
		int [] max;
		int buf;
		
		rod = Integer.parseInt(br.readLine());
		cost = new int[rod+1];
		max = new int[rod+1];
		
		st = new StringTokenizer(br.readLine(), " ");
		for(int i=1 ; i<rod+1 ; i++) {
			cost[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i=1 ; i<rod+1 ; i++) {
			buf = 0;
			for(int j=1 ; j<i+1 ; j++)
				buf = Math.max(buf, cost[j]+max[i-j]);
			max[i] = buf;
		}
		
		System.out.println(max[rod]);
	}
}
