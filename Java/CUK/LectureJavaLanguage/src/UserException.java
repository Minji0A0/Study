public class UserException {
    void check(int weight) throws InvalidException{
        if (weight < 100){
            throw new InvalidException("InvalidException 클래스 호출입니다.");
        }
    }

    public static void main(String[] args) {
        UserException ue = new UserException();
        try{
            ue.check(70);
        }
        catch (InvalidException e){
            System.out.println("예외 처리입니다.");
            System.out.println(e.getMessage());
        }
    }
}
