import java.util.Scanner;

public class FindPasswordOneByOne_2043 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int password, firstNum, count;
		
		password = sc.nextInt();
		firstNum = sc.nextInt();
		
		count = password - firstNum+1;
		System.out.println(count);
	}
}
