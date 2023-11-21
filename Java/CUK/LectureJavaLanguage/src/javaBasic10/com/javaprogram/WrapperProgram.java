package javaBasic10.com.javaprogram;

public class WrapperProgram {
    public static void main(String[] args) {
        Integer num1 = 100; // Integer 클래스를 사용하여 정수 값을 Wrapping 함
        Integer num2 = 200; // Integer 클래스를 사용하여 정수 값을 Wrapping 함
        System.out.println("num1 : " + num1);
        System.out.println("num2 : " + num2);
        String value1 = num1.toString(); // toString() 메서드를 사용하여 문자열로 변환함
        String value2 = num2.toString(num2);
        System.out.println("num1.toString(): " + value1);
        System.out.println("Integer.toString(num2) : "+ value2);
    }
}
