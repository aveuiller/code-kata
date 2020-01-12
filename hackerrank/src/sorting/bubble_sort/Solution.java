package sorting.bubble_sort;


import java.util.Scanner;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-bubble-sort
 */
public class Solution {

    // Complete the countSwaps function below.
    static void countSwaps(int[] a) {
        int nbSwap = 0;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < a.length; i++) {
            max = Math.max(max, a[i]);
            min = Math.min(min, a[i]);
            for (int j = i; j < a.length; j++) {
                if (a[j] < a[i]) {
                    nbSwap++;
                }
            }
        }
        System.out.println("Array is sorted in " + nbSwap + " swaps.");
        System.out.println("First Element: " + min);
        System.out.println("Last Element: " + max);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] a = new int[n];

        String[] aItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int aItem = Integer.parseInt(aItems[i]);
            a[i] = aItem;
        }

        countSwaps(a);

        scanner.close();
    }
}