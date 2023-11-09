package javaBasic03;

public class report03 {

	public static void main(String[] args) {
//		3주차 실습문제 :
//		조건문과 반복문을 활용하여 1~10까지 숫자 중에서 짝수를 출력함.
		
		for(int i = 1 ; i <= 10 ; i++) {
			if(i % 2 == 0) {
				System.out.println(i);
			}
		}
		
	}
}
