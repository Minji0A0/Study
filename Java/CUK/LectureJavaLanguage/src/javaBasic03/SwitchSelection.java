package javaBasic03;

public class SwitchSelection {

	public static void main(String[] args) {
		char grade = 'B';
		switch (grade){
			case 'A' :
				System.out.println("매우 우수");
				break;
			case 'B' :
				System.out.println("우수");
				break;
			case 'C' :
				System.out.println("보통");
			default :
				System.out.println("파이팅");
		}
	}
}
