package javaBasic06;

public class ConstructorCall {

	public static void main(String[] args) {
		AddConstructor addIntCons = new AddConstructor(1,2);
		AddConstructor addDoubleCons = new AddConstructor(2.4, 6.2);
		AddConstructor addMixCons = new AddConstructor(3, 5.5);
	}
}
