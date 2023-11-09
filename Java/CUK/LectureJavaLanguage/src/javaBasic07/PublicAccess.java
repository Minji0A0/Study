package javaBasic07;

public class PublicAccess {
public static void main(String[] args) {
	Dog dog = new Dog();
	
	dog.breed = "말티즈";
	dog.color = "흰색";
	
	System.out.println("강아지 품종 : " + dog.breed);
	System.out.println("강아지 색상 : " + dog.color);
	dog.bowwow();
	dog.run();
}
}
