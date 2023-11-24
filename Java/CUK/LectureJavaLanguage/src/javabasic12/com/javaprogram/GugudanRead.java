package javabasic12.com.javaprogram;

import java.io.File;
import java.io.FileInputStream;

public class GugudanRead {
    public static void main(String[] args) {
        File file = new File("gugudan.txt");
        try {
            if (!file.exists()) ;
            file.createNewFile();
            FileInputStream fis = new FileInputStream(file);
            int i = 0;
            while ((i = fis.read()) != -1) { //파일 끝이 아닌 동안 반복함
                System.out.print((char) i);
            }
            fis.close();
            System.out.println("파일 읽기 성공");
        } catch (Exception e) {
            e.getMessage();
        }
    }
}
