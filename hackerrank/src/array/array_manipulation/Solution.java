package array.array_manipulation;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Challenge: https://www.hackerrank.com/challenges/crush
 */
public class Solution {
    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[][] queries) {
        return smartFill(n, queries);
    }

    private static long smartFill(int n, int[][] queries) {
        long[] values = new long[n];
        for (int[] query : queries) {
            int lowerLimit = query[0];
            int upperLimit = query[1];
            int value = query[2];

            values[lowerLimit - 1] += value;
            if (upperLimit < n) {
                values[upperLimit] -= value;
            }
        }

        long current = 0;
        long max = 0;
        for (long value : values) {
            current += value;
            max = Math.max(max, current);
        }
        return max;
    }

    private static long bruteforceFill(int n, int[][] queries) {
        long max = 0;
        long[] values = new long[n];
        for (int[] query : queries) {
            int lowerLimit = query[0];
            int upperLimit = query[1];
            int value = query[2];

            for (int j = lowerLimit - 1; j < upperLimit; j++) {
                values[j] += value;
                max = Math.max(max, values[j]);
            }
        }
        return max;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nm = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nm[0]);

        int m = Integer.parseInt(nm[1]);

        int[][] queries = new int[m][3];

        for (int i = 0; i < m; i++) {
            String[] queriesRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 3; j++) {
                int queriesItem = Integer.parseInt(queriesRowItems[j]);
                queries[i][j] = queriesItem;
            }
        }

        long result = arrayManipulation(n, queries);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
