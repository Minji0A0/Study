package javaBasic04;

public class WithoutInputWithOutputDivide {

	public static int divide() {
		int a = 10, b = 5;
		int result = a/b;
		
		return result;
	}
	
	public static void main(String[] args) {
		int num = divide();
		System.out.println("결과 : " + num );
	}
}
