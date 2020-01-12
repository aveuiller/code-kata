package recursion_backtracking.davis_staircase;

import java.io.*;
import java.util.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-recursive-staircase
 */
public class Solution {
    public static Map<Integer,Integer> cache = new HashMap<>();

    static int recurStepPerms(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        if (n == 3) return 4;
        if (!cache.containsKey(n)) {
            cache.put(n, recurStepPerms(n-3) + recurStepPerms(n-2) + recurStepPerms(n-1));
        }
        return cache.get(n);
    }

    // Complete the stepPerms function below.
    static int stepPerms(int n) {
        return recurStepPerms(n);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int s = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int sItr = 0; sItr < s; sItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int res = stepPerms(n);

            bufferedWriter.write(String.valueOf(res));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
