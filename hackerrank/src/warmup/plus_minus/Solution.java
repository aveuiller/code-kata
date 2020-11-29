package warmup.plus_minus;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/plus-minus
 */
public class Solution {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        final double ratio_per_entry = 1.0d / arr.length;
        double percent_negative = 0;
        double percent_positive = 0;
        double percent_zero = 0;
        for (int i : arr) {
            if (i < 0) {
                percent_negative += ratio_per_entry;
            } else if (i > 0) {
                percent_positive += ratio_per_entry;
            } else {
                percent_zero += ratio_per_entry;
            }
        }

        System.out.printf("%.6f%n", percent_positive);
        System.out.printf("%.6f%n", percent_negative);
        System.out.printf("%.6f%n", percent_zero);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
