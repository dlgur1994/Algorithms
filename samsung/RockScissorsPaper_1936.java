import java.util.Scanner;

public class RockScissorsPaper_1936 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a,b;
		
		a = sc.nextInt();
		b = sc.nextInt();
		
		if(a>b || (a==1&&b==3)) {
			if(a==3 && b==1)
				System.out.println("B");
			else
				System.out.println("A");
		}
		else
			System.out.println("B");
	}
}
