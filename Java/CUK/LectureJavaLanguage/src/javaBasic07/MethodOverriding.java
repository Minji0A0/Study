package javaBasic07;

public class MethodOverriding {
    public static void main(String[] args) {
        Calculator addCalc = new Calculator();
        Calculator subCalc = new SubtractCalculator();
        Calculator multiCalc = new MultiplyCalculator();
        Calculator divCalc = new DivideCalculator();

        addCalc.calculate(10, 5);
        subCalc.calculate(10, 5);
        multiCalc.calculate(10,5);
        divCalc.calculate(10,5);
    }
}
