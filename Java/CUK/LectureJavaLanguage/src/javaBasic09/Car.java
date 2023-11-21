package javaBasic09;

// 추상클래스
public class Car extends FourWheeler {
//    protected String model;
//    public abstract void drive();

    public void price(){
        System.out.println("가격 : 3000만원");
    }
    //brand() 메서드 재정의
    
    public void brand(){
        System.out.println("브랜드 : 한국 자동차");
    }
    public void color(){
        System.out.println("색상 : 흰색");
    }
}
