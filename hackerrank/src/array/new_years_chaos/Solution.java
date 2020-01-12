package array.new_years_chaos;


import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/new-year-chaos
 * <p>
 * TODO: Still timeout on submission
 */
public class Solution {
    private static final int MAX_BRIBES = 2;
    private static final String TOO_CHAOTIC_EXIT = "Too chaotic";

    // Complete the minimumBribes function below.
    static void minimumBribes(int[] q) {
    /* Max bribes == 2
        2 1 5 3 4 => 3
        2 5 1 3 4 => Too Chaotic
    */
        int queueSize = q.length;
        int totalBribes = 0;
        int currentInLine;
        int currentlyReplacing = 0;
        int numberOfBribes = 0;
        for (int i = queueSize - 1; i >= 0; i--) {
            currentInLine = q[i];
            if (currentInLine > i + 1) {
                // Tracking nb bribes
                if (currentlyReplacing != currentInLine) {
                    currentlyReplacing = currentInLine;
                    numberOfBribes = 1;
                } else {
                    if (++numberOfBribes > MAX_BRIBES) {
                        System.out.println(TOO_CHAOTIC_EXIT);
                        return;
                    }
                }

                // Shifting data
                q[i] = q[i + 1];
                q[i + 1] = currentInLine;
                totalBribes++;
                // Found an anomaly, reset array state
                i = queueSize - 1;
            }
        }
        System.out.println(totalBribes);

//        for (int i = 0; i < queueSize; i++) {
//            // Shifting people to 0..n-1 so that it matches the indexes
//            currentInLine = q[i] - 1;
//
//            // Person has advanced from his initial place
//            if (currentInLine > i) {
//                if (currentInLine - i > MAX_BRIBES) {
//                    System.out.println(TOO_CHAOTIC_EXIT);
//                    return;
//                }
//                totalBribes += currentInLine - i;
//            }
//        }
//        System.out.println(totalBribes);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] q = new int[n];

            String[] qItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int i = 0; i < n; i++) {
                int qItem = Integer.parseInt(qItems[i]);
                q[i] = qItem;
            }

            minimumBribes(q);
        }

        scanner.close();
    }
}
