import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		
		int count_num = 0;
		int sum = 0;
		
		while(sum < x) {
			count_num++;
			sum += count_num;
		}
		
		sum -= count_num;
		
		int a = count_num % 2 == 0 ? x - sum : count_num + 1 - (x - sum);
		int b = count_num + 1 - a;
		
		System.out.println(a + "/" + b);
	}

}