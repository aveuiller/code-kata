package search.pairs;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/pairs
 */
public class Solution {

    // Complete the pairs function below.
    static int pairs(int k, int[] arr) {
        Map<Integer, Integer> available = new HashMap<>();
        Map<Integer, Integer> targets = new HashMap<>();
        for (int i : arr) {
            int target = i - k;
            int tAmount = targets.get(target) != null ? targets.get(target) : 0;
            int aAmount = available.get(i) != null ? available.get(i) : 0;
            targets.put(target, tAmount + 1);
            available.put(i, aAmount + 1);
        }

        int validatedPairs = 0;
        for (Map.Entry<Integer, Integer> targetAmount : targets.entrySet()) {
            if (available.containsKey(targetAmount.getKey())) {
                validatedPairs += Math.min(available.get(targetAmount.getKey()), targetAmount.getValue());
            }
        }
        return validatedPairs;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int result = pairs(k, arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
