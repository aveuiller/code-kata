package greedy_algorithm.luck_balance;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/luck-balance
 */
public class Solution {
    // Complete the luckBalance function below.
    static int luckBalance(int k, int[][] contests) {
        List<Integer> importantLuck = new ArrayList<>(contests.length);
        int maxLuck = 0;
        int luckValue;
        int importance;
        // Losing non important contest + mapping important ones
        for (int[] contest : contests) {
            luckValue = contest[0];
            importance = contest[1];
            if (importance == 0) {
                maxLuck += luckValue;
            } else {
                importantLuck.add(luckValue);
            }
        }

        // Sort important contest luck in descending order
        Collections.sort(importantLuck);
        Collections.reverse(importantLuck);
        // Lose the k most rewarding in luck
        for (int i = 0; i < Math.min(k, importantLuck.size()); i++) {
            maxLuck += importantLuck.get(i);
        }
        // Win all required next contests.
        for (int i = k; i < importantLuck.size(); i++) {
            maxLuck -= importantLuck.get(i);
        }
        return maxLuck;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[][] contests = new int[n][2];

        for (int i = 0; i < n; i++) {
            String[] contestsRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 2; j++) {
                int contestsItem = Integer.parseInt(contestsRowItems[j]);
                contests[i][j] = contestsItem;
            }
        }

        int result = luckBalance(k, contests);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
