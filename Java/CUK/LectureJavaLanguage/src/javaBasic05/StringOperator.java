package javaBasic05;

public class StringOperator {
	
	public static void main(String[] args) {
		String name1 = new String("Minji");
		String name2 = new String("Minji");
		String name3 = new String("minji");
		String name4 = name2 + " " + name3;
		String name5 = name1;
		
		//1. name1는 name2와 별개의 객체임으로 false가 출력
		System.out.println("1. " + (name1 == name2));
		//2. name1과 name2는 new로 생성된 별개의 객체임으로 true가 출력 
		System.out.println("2. " + (name1 != name2));
		//3. name2와 name3는 별개의 객체임으로 false가 출력되며, 값 또한 대문자와 소문자로 다르다.
		System.out.println("3. " + (name2 == name3));
		//4. name2와 name3는 별개의 객체임으로 true가 출력되며, 값 또한 대문자와 소문자로 다르다.
		System.out.println("4. " + (name2 != name3));
		//5. name4는 문자열 객체 name2와 name3의 합산으로 순서대로 연달아 출력된다.
		System.out.println("5. " + name4);
		//6. name1과 name2는 별개의 객체이지만 값이 같으므로 true가 출력된다.
		System.out.println("6. " + name1.equals(name2));
		//7. name5와 name1은 같은 객체이므로 값이 출력된다.
		System.out.println("7. " + name5);
		
		
	}

}
