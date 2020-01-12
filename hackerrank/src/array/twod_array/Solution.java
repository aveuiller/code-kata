package array.twod_array;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/2d-array
 */
public class Solution {

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        int maxSum = Integer.MIN_VALUE;

        // We skip the first & last lines as they could not contain hourglasses
        for (int i = 1; i < arr.length - 1; i++) {
            for (int j = 1; j < arr[i].length - 1; j++) {
                maxSum = Math.max(maxSum, computeSum(arr, i, j));
            }
        }
        return maxSum;
    }

    /**
     * Compute a specific hourglass on the matrix.
     *
     * @param arr Matrix to compute from.
     * @param x   The initial row.
     * @param y   The initial column.
     * @return The computed sum.
     */
    private static int computeSum(int[][] arr, int x, int y) {
        int sum = 0;
        for (int i = x - 1; i <= x + 1; i++) {
            for (int j = y - 1; j <= y + 1; j++) {
                if (i != x || j == y) {
                    sum += arr[i][j];
                }
            }
        }
        return sum;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
