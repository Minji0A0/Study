package javabasic12.com.javaprogram;

import java.io.File;
import java.io.IOException;

public class FileCreation {
    public static void main(String[] args) {
        File fileObj = new File("testfile.txt");
        try {
            boolean success = fileObj.createNewFile();
            if(success){
                System.out.println("파일 생성 성공");
            }else {
                System.out.println("파일 생성 실패");
            }
        } catch (IOException e){
            System.out.println(e);
            System.out.println(e.getMessage());
        }

    }
}
