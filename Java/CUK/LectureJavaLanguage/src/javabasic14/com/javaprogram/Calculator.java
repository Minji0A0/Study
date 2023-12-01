package javabasic14.com.javaprogram;

import javax.swing.*;
import java.awt.*;

public class Calculator extends JFrame {
    public Calculator() {
        setTitle("계산기"); //프레임의 제목 설정
        setSize(300, 250); // 프레임의 크기 설정

        //JLabel 객체(제목 레이블)를 세팅하여 JPanel에 추가함
        JPanel titlePanel = new JPanel();
        titlePanel.setBounds(0, 0, 300, 40);
        add(titlePanel);
        JLabel title = new JLabel("계산기", JLabel.CENTER);
        title.setFont(new Font("함초롬돋움", Font.BOLD, 20));
        titlePanel.add(title);
        //JTextField 객체 (입력 받는 두개 숫자)를 세팅하여 JPanel에 추가
        JPanel numPanel = new JPanel();
        numPanel.setBounds(0, 40, 300, 40);
        add(numPanel);
        JTextField num1 = new JTextField(5);
        numPanel.add(num1);
        JTextField num2 = new JTextField(5);
        numPanel.add(num2);

        //JButton 객체(+. - 버튼)를 세팅하여 JPanel에 추가함
        JPanel btPanel01 = new JPanel();
        btPanel01.setBounds(0, 80, 300, 40);
        add(btPanel01);
        JButton plus = new JButton("+");
        btPanel01.add(plus);
        JButton minus = new JButton("-");
        btPanel01.add(minus);

        //JButton 객체(*, / 버튼)를 세팅하여 JPanel에 추가함
        JPanel btPanel02 = new JPanel();
        btPanel02.setBounds(0, 120, 300, 40);
        add(btPanel02);
        JButton multiply = new JButton("*");
        btPanel02.add(multiply);
        JButton divide = new JButton("/");
        btPanel02.add(divide);

        //JLabel 객체(계산 결과 레이블)를 세팅하여 JPanel에 추가함
        JPanel resultPanel = new JPanel();
        resultPanel.setBounds(0, 160, 300, 40);
        add(resultPanel);
        JLabel label01 = new JLabel("계산결과 : ");
        JLabel label02 = new JLabel("");
        resultPanel.add(label01);
        resultPanel.add(label02);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //JFrame에 창 닫기를 추가함
        setLayout(null); //null 값을 넣어서 컴포넌트의 위치/크기 제약을 자유롭게함
        setVisible(true);
    }

    public static void main(String[] args) {
        new Calculator();
    }
}
