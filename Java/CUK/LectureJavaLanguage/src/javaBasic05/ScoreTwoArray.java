package javaBasic05;

public class ScoreTwoArray {
	
	public static void main(String[] args) {
		int[][] Score = {{50,60,70,80,90,},
				{55,65,75,85,95},
				{60,70,80,90,80}};
		for (int i = 0; i < 3; i++ ) {
			for (int j = 0 ; j < 5; j++) {
				System.out.print(Score[i][j]+" ");
			}
			System.out.println();
		}
	}

}
