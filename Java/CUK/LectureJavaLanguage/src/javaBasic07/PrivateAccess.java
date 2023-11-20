package javaBasic07;

public class PrivateAccess {
    public static void main(String[] args) {
        Dog dog = new Dog();

        dog.breed = "말라뮤트";
        dog.color = "흰색";
//        dog.age = 4; // age는 private이기 때문에 접근이 불가하다
//        dog.name = "자바"; // name은 private이기 때문에 접근이 불가하다

        System.out.println("강아지품종 : " + dog.breed);
        System.out.println("강아지색상 : "+ dog.color);
//        System.out.println("강아지나이 :" + dog.age); // age는 private이기 때문에 접근이 불가하다
//        System.out.println("강아지이름 : "+ dog.name); // name은 private이기 때문에 접근이 불가하다
        dog.bowwow();

    }
}
