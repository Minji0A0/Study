package javaBasic07;

public class InheritancePolymorphismCalc {
    public static void main(String[] args) {
        Calculator addCalc = new Calculator();
        Calculator subCalc = new SubtractCalculator();

        addCalc.calculate(10, 5);
        subCalc.calculate(10, 5);
    }

}
