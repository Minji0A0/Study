package javaBasic03;

import java.util.Scanner;

public class DoWhileIteration {

	public static void main(String[] args) {
		double current = 30.0;
		Scanner scanner = new Scanner(System.in);
		double target = scanner.nextDouble();
		
		do {
			current -= 1.0;
			System.out.println("현재 온도 : " + current);
		}while (current > target );
		scanner.close();
	}
}
