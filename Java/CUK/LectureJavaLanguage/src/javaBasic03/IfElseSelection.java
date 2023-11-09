package javaBasic03;

public class IfElseSelection {
	public static void main(String[] args) {
		int num = 20;
		if(num % 2 == 0) {
			System.out.println(num+"은 짝수입니다.");
		}
		else {
			System.out.println(num+"은 홀수입니다.");
		}
	
	
		int cost = 20000;
		if(cost >= 50000) {
			System.out.println("배송비 무료");
		}
		else if(cost >= 30000 ) {
			System.out.println("배송비 2000원");
		}
		else {
			System.out.println("배송비 3000원");
		}
		
		int num1 = 30, num2 = 20, num3 = 40;
		
		if(num1> num2) {
			if(num1 > num3) {
			System.out.println("num1은 가장 큰 수입니다.");
		}
		else {
			System.out.println("num1은 가장 큰 수가 아닙니다.");
		}
	}
	else {
		System.out.println("num1은 가장 큰 수가 아닙니다.");
		}
	}
}