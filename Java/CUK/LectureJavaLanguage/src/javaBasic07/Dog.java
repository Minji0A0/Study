package javaBasic07;

public class Dog extends Animal {
	public String breed;
	public String color;
	int age;
	String name;

	public void bowwow() {
		System.out.println("멍멍 짖다");
	}
	protected void run() {
		System.out.println("달리다");
	}
	void sleep(){System.out.println("잠자다");}

	public void sound(){System.out.println("강아지 멍멍");}
}
