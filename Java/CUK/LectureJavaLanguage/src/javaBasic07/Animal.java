package javaBasic07;

public class Animal {
    protected String name;
    protected String getName()
    {
        return name;
    }

    public void eat(){
        System.out.println("먹이 먹음");
    }

    public void sound(){
        System.out.println("동물 울음");
    }

    public void sound(String str){
        System.out.println("메서드 오버로딩 동물 울음 str");
    }

}
