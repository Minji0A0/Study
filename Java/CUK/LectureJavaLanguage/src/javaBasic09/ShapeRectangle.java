package javaBasic09;

public class ShapeRectangle {
    public static void main(String[] args) {
        Shape rectangle = new Rectangle("노란색", 2,4);

        System.out.println("색상 : " + rectangle.getColor());
        System.out.println(("면적 : " + rectangle.getArea()));
    }
}
