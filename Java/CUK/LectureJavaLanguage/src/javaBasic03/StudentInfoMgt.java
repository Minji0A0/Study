package javaBasic03;

public class StudentInfoMgt {

	public static void main(String[] args) {
		Student stuA = new Student();
		stuA.insertInfo("1234", "홍길동");
		stuA.printInfo();
		
		Student stuB = new Student("5678", "홍길순");
		stuB.printInfo();
	}
}
