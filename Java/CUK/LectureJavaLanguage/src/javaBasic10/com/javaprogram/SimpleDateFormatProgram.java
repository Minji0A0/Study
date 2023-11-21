package javaBasic10.com.javaprogram;

import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateFormatProgram {
    public static void main(String[] args) {
        Date date = new Date();
        SimpleDateFormat formatter = new SimpleDateFormat("MM/dd/yyyy");
        String strDate = formatter.format(date);
        System.out.println("MM/dd/yyyy : " + strDate);
        formatter = new SimpleDateFormat("dd-MM-yyyy hh:mm:ss");
        strDate = formatter.format(date);
        System.out.println("dd-MM-yyyy hh:mm:ss : " + strDate);
        formatter = new SimpleDateFormat("dd MMMM yyyy");
        strDate = formatter.format(date);
        System.out.println("dd MMMM yyyy : " + strDate);
        formatter = new SimpleDateFormat("dd MMMM yyyy zzzz"); //zzzz 는 타임존
        strDate = formatter.format(date);
        System.out.println("dd MMMM yyyy zzzz : " + strDate);
    }
}
