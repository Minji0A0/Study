package javaBasic04;

public class MethodOverloadingCalc {
	public static void calculate(int x, int y) {
		for (int i = 0 ; i < 10 ; i ++ ) {
			if(i==4)
				break;
			System.out.println(x * y);
		}
	}
	public static void calculate (int x) {
		for (int i = 0; i< 10; i ++) {
			if(i==5)
				break;
			System.out.println(x*x);
		}
	}
	public static void main(String[] args) {
		calculate(2, 3);
		calculate(2);
	}
}
