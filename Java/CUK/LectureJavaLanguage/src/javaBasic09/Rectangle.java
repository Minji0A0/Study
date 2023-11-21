package javaBasic09;
// 일반클래스
public class Rectangle extends Shape{
    double length;
    double width;

    public Rectangle(String color, double length, double width){
        super(color);
        System.out.println("Rectangle 클래스 생성자 호출");
        this.length = length;
        this.width = width;
    }

    double getArea(){
        return length * width;
    }

}
