package javaBasic10.com.javaprogram;

import java.util.StringTokenizer;

public class StringTokenizerProgram {
    public static void main(String[] args) {
        StringTokenizer st = new StringTokenizer("Java,C,Python,JSP",",");
        while (st.hasMoreTokens()){
            System.out.println(st.nextToken());
        }
    }
}
