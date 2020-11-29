package sorting.merge_sort;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-merge-sort
 *
 * WARNING: Remove all System.out before submitting.
 *
 *
 * <p>
 * Example:
 * # Input
 * 2
 * 5
 * 1 1 1 2 2
 * 5
 * 2 1 3 1 2
 * <p>
 * # Output
 * 0
 * 4
 */
public class Solution {
    static class InversionCounter {
        private long count;
        private final int[] arr;

        public InversionCounter(int[] arr) {
            count = 0;
            this.arr = arr;
        }

        public int[] mergeSort() {
            this.count = 0;
            return this.mergeSort(this.arr);
        }

        private int[] mergeSort(int[] arr) {
            System.out.println("Calling mergeSort on array: " + printArray(arr));
            if (arr.length == 1) {
                return arr;
            } else {
                int separation = arr.length / 2;
                return merge(
                        mergeSort(Arrays.copyOfRange(arr, 0, separation)),
                        mergeSort(Arrays.copyOfRange(arr, separation, arr.length))
                );
            }
        }

        private String printArray(int[] arr) {
            StringBuilder sb = new StringBuilder();
            for (int i : arr) {
                sb.append(i).append(" ");
            }
            return sb.toString();
        }

        private int[] merge(int[] partA, int[] partB) {
            System.out.println("Merging arrays: " + printArray(partA) + " and " + printArray(partB));
            int[] merged = new int[partA.length + partB.length];
            int partBIndex = 0;
            for (int i = 0; i < partA.length; i++) {
                while (partBIndex < partB.length && partB[partBIndex] < partA[i]) {
                    merged[i + partBIndex] = partB[partBIndex];
                    this.count += partA.length - i;
                    partBIndex++;
                }
                merged[i + partBIndex] = partA[i];
            }

            // Complete array
            if (partB.length - partBIndex >= 0) {
                System.arraycopy(partB, partBIndex, merged, partA.length + partBIndex, partB.length - partBIndex);
            }
            System.out.println("Merged Array : " + printArray(merged));
            System.out.println("Permutation count: " + this.count);
            return merged;
        }

    }

    // Complete the countInversions function below.
    static long countInversions(int[] arr) {
        System.out.println();
        System.out.println();
        InversionCounter inversionCounter = new InversionCounter(arr);
        int[] sorted = inversionCounter.mergeSort();

        System.out.println("## Result: ");
        System.out.print("Sorted Array: ");
        for (int i : sorted) {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println("Permutation count: " + inversionCounter.count);

        return inversionCounter.count;
    }

    /**
     * Actually count the amount of permutations.
     * <p>
     * Warning: Time limit exceeded
     *
     * @param arr
     * @param count
     * @return
     */
    private static long bruteForceCount(int[] arr, long count) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] > arr[j]) {
                    count++;
                }
            }
        }
        return count;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] arr = new int[n];

            String[] arrItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int arrItem = Integer.parseInt(arrItems[i]);
                arr[i] = arrItem;
            }

            long result = countInversions(arr);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
