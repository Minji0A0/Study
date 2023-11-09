package javaBasic03;

import java.util.Scanner;

public class WhileIteration {

	public static void main(String[] args) {
		double current = 30.0;
		Scanner scanner = new Scanner(System.in);
		double target = scanner.nextDouble();
		
		while(current > target ) {
			current -= 1.0;
			System.out.println("현재 온도 : " + current);
		}
		scanner.close();
	}
}
