package javaBasic05;

public class SumOfTwoArray {
	public static void main(String[] args) {

		int rows = 2, columns = 3;
		int[][] firstMatrix = { { 2, 3, 4 }, { 3, 2, 1 } };
		int[][] secondMatrix = { { 1, 2, 3 }, { -2, -1, 1 } };

		int[][] sum = new int[rows][columns];
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				sum[i][j] = firstMatrix[i][j] + secondMatrix[i][j];
			}
		}
		System.out.println("두 행력의 합 : ");
		for (int i = 0; i < rows; i++) {
			for (int j = 0; j < columns; j++) {
				System.out.print(sum[i][j] + " ");
			}
			System.out.println();
		}

	}
}