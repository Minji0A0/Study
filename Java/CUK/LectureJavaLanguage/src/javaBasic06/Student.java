package javaBasic06;

public class Student {

	Student(){
		System.out.println("기본 생성자 호출");
	}
	
	Student(String stuId, String stuName){
		System.out.println("일반 생성자 호출");
		id = stuId;
		name = stuName;
	}
	
	String id, name;
	void insertInfo(String stuid, String stuName) {
		id = stuid;
		name = stuName;
	}
	void printInfo() {
		System.out.println("학번 : " + id);
		System.out.println("이름 : " + name);
	}
	
	

}
