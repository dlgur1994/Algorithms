import java.util.Scanner;

public class PrintNumberBackward_1545 {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int num;
		
		num = sc.nextInt();
		
		for(int i=num ; i>=0 ; i--) {
			System.out.print(i + " ");
		}
	}
}
