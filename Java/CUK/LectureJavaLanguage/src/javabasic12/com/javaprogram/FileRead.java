package javabasic12.com.javaprogram;

import java.io.File;
import java.io.FileReader;

public class FileRead {
    public static void main(String[] args) {
        File file = new File("member.txt");
        try{
            if(!file.exists())
                file.createNewFile();
            FileReader fr = new FileReader(file);
            int i = 0;
            while ((i = fr.read()) != -1){
                System.out.print((char) i);
            }fr.close();
            System.out.println("파일 읽기 성공");
        }catch (Exception e){
            e.getMessage();
        }
    }
}
