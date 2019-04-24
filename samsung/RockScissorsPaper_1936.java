import java.util.Scanner;

public class RockScissorsPaper_1936 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a,b;
		
		a = sc.nextInt();
		b = sc.nextInt();
		
		if((b!=1&&a>b) || a==1 && b==3)
			System.out.println("A");
		else
			System.out.println("B");
	}
}
