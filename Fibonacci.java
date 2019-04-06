import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Fivonacci {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num;
		int[] fiv;
		int sum = 0;
		
		num = Integer.parseInt(br.readLine());
		fiv = new int[num+1];
		
		fiv[1] = 1;
		fiv[2] = 1;
		sum += fiv[1]+fiv[2];
		for(int i=3 ; i<num+1 ; i++) {
			fiv[i] = fiv[i-1] + fiv[i-2];
			sum += fiv[i];
		}
		System.out.println(fiv[num]);
		System.out.println(sum);
	}
}
