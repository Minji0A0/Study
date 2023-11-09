package javaBasic04;

public class WithMethod {

	public static void addNumbers(int a, int b) {
		int sum = a +  b;
		System.out.println("두 숫자의 합 :" + sum);
		
	}
	
	public static void main(String[] args) {
		int num1 = 5, num2 = 3;
		
		int num9 = 2 , num10 = 7;
		
		addNumbers(num1, num2);
		addNumbers(num9, num10);
		
	}
}
