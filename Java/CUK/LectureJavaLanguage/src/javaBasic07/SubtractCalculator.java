package javaBasic07;

public class SubtractCalculator extends Calculator{
    public void calculate(int x, int y){
        for (int i = 0; i < 5 ; i++ ) {
            if (i == 3)
                continue;
            System.out.println(x - y);
        }
    }
}
