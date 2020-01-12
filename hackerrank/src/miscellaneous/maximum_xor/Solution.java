package miscellaneous.maximum_xor;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * https://www.hackerrank.com/challenges/maximum-xor/
 * <p>
 * TODO: Still timeout on submission
 */
public class Solution {
    private static final Map<Integer, Integer> CACHE = new HashMap<>();

    // Complete the maxXor function below.
    static int[] maxXor(int[] arr, int[] queries) {
        int[] result = new int[queries.length];
        int maxXor = Integer.MIN_VALUE;

        for (int i = 0; i < queries.length; i++) {
            int query = queries[i];

            if (!CACHE.containsKey(query)) {
                for (int j : arr) {
                    maxXor = Math.max(maxXor, query ^ j);
                }
                CACHE.put(query, maxXor);
                maxXor = Integer.MIN_VALUE;
            }

            result[i] = CACHE.get(query);
        }
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int m = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] queries = new int[m];

        for (int i = 0; i < m; i++) {
            int queriesItem = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
            queries[i] = queriesItem;
        }

        int[] result = maxXor(arr, queries);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
