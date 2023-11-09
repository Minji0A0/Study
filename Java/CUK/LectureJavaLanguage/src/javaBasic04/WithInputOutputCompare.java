package javaBasic04;

public class WithInputOutputCompare {

	public static int compare(int x, int y) {
		int result;
		
		if(x>y) {
			result = x;
		}else {
			result = y;}
		return result;
	}
	
	public static void main (String[] args) {
		int a = 5, b = 6;
		
		int num = compare(a, b);
		System.out.println(a + "와 " + b + " 중 " + num + "이 큽니다.");
	}
}
