package javaBasic09;
//추상클래스 - 추상메서드 , 일반메서드 모두 포함가능
public abstract class Animal {
    public abstract void sound();
    public void eat(){
        System.out.println("먹이 먹음");
    }
}
