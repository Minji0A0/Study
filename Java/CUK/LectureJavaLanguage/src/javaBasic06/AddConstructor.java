package javaBasic06;

public class AddConstructor {
	AddConstructor(){
		System.out.println("기본 생성자 Add() 호출");
	}
	
	AddConstructor(int a, int b){
		System.out.println("일반 생성자 AddConstructor(int a, int b) 호출");
		System.out.println(a + "+" + b + " = " + (a+b));
	}
	
	AddConstructor(double a, double b){
		System.out.println("일반 생성자 AddConstructor(double a, double b) 호출");
		System.out.println(a + "+" + b + " = " + (a+b));
	}
	
	AddConstructor(int a, double b){
		System.out.println("일반 생성자 AddConstructor(int a, double b) 호출");
		System.out.println(a + "+" + b + " = " + (a+b));
	}
}
