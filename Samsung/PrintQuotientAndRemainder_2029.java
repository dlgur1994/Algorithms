import java.util.Scanner;

public class PrintQuotientAndRemainder_2029 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int test, num, div;
		
		test = sc.nextInt();
		for(int i=1 ; i<=test; i++) {
			num = sc.nextInt();
			div = sc.nextInt();
			System.out.println("#" + i + " " + num/div + " " +num%div);
		}
	}
}
