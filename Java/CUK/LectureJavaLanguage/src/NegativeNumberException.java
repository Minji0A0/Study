import java.util.Scanner;

public class NegativeNumberException {
    static void check(int num) throws NumberFormatException{
        if(num<0)
            throw new NumberFormatException("0보다 작습니다");
        else
            System.out.println(num);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("숫자를 입력하세요");
        int num = scanner.nextInt();

    try {
        if(num < 0)
            throw new NumberFormatException("0보다 작습니다");
        else
            System.out.println(num);
        check(num);
        }
    catch (NumberFormatException e){
        System.out.println("예외 발생" + e);
        }
        scanner.close();
    }
}
