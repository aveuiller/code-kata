package search.ice_cream_parlor;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
 */
public class Solution {

    // Complete the whatFlavors function below.
    static void whatFlavors(int[] cost, int money) {
        int[] flavours = chooseFlavours(cost, money);
        // Ice cream are IDs 1 indexed.
        System.out.println((flavours[0] + 1) + " " + (flavours[1] + 1));
    }

    private static int[] chooseFlavours(int[] cost, int money) {
        Map<Integer, Integer> remainingMoney = new HashMap<>();
        int[] choices = new int[2];
        for (int i = 0; i < cost.length; i++) {
            if (remainingMoney.containsKey(cost[i])) {
                choices[0] = remainingMoney.get(cost[i]);
                choices[1] = i;
                break;
            }
            remainingMoney.put(money - cost[i], i);
        }
        return choices;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int money = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] cost = new int[n];

            String[] costItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int costItem = Integer.parseInt(costItems[i]);
                cost[i] = costItem;
            }

            whatFlavors(cost, money);
        }

        scanner.close();
    }
}
