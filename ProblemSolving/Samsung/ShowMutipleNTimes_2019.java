import java.util.Scanner;

public class ShowMutipleNTimes_2019 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num;
		int sum=1;
		
		num = sc.nextInt();
		
		for(int i=1 ; i<=num+1 ; i++) {
			System.out.print(sum + " ");
			sum *= 2;
		}
	}
}
