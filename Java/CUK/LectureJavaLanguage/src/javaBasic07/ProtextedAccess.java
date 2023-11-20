package javaBasic07;

public class ProtextedAccess {
    public static void main(String[] args) {
        Dog dog = new Dog();

        dog.breed = "말티즈";
        dog.color = "빨간색";
        dog.age = 10;

        System.out.println("강아지 품종 : " + dog.breed);
        System.out.println("강아지 색상 : " + dog.color);
        dog.bowwow();

        System.out.println("강아지 나이 : " + dog.age);
        dog.run();

    }
}
