package javaBasic07;

public class DefaultAccess {
    public static void main(String[] args) {
        Dog dog = new Dog();

        dog.breed = "허스키";
        dog.color = "회색";
        dog.age = 2;

        System.out.println("강아지 품종 :" + dog.breed);
        System.out.println("강아지 색상 : " + dog.color);
        dog.bowwow();
        dog.run();
        dog.sleep();
    }
}
