import java.util.Scanner;

public class SubmutipleOfN_1933 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num;

		num = sc.nextInt();
		for(int i=1; i<=num ; i++) {
			if(num%i == 0)
				System.out.print(i + " ");
		}
	}
}
