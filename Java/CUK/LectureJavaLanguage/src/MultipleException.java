import java.util.Scanner;

public class MultipleException {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("숫자를 입력하세요");
        int num = scanner.nextInt();
        int arr[] = new int[5];

        try{
            arr[num] = 10/num;
            System.out.println(arr[num]);
        }
        catch (ArithmeticException e){
            System.out.println("0이 아닌 값을 입력하세요");
            System.out.println(e.getMessage());
        }
        catch (ArrayIndexOutOfBoundsException e){
            System.out.println("올바른 배열 인덱스를 입력하세요");
            System.out.println(e.getMessage());
        }
        scanner.close();
    }

}
