package javaBasic04;

public class WithInputWithoutOutputCircle {

	public static void circle(int x, double y) {
		System.out.println(2*x*y);
	}
	
	public static void main(String[] args) {
		int radius = 4;
		double pi = 3.14;
		
		System.out.print("2 x "+ radius + " x " + pi + " = ");
		circle (radius, pi);
	}
	
}
