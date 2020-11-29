package dynamic_programming.abbreviation;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Challenge: https://www.hackerrank.com/challenges/abbr/
 * <p>
 * TODO: Still timeout on submission
 */
public class Solution {
    private static Map<String, Map<String, Boolean>> CACHE = new HashMap<>();

    static boolean areMatching(String a, String b) {
        if (b.isEmpty()) {
            for (char c : a.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    return false;
                }
            }
            return true;
        }
        if (a.isEmpty()) {
            return false;
        }

        Map<String, Boolean> aCache = CACHE.computeIfAbsent(a, k -> new HashMap<>());
        if (!aCache.containsKey(b)) {
            final char aChar = a.charAt(0);
            final String nextB = b.substring(1);
            final String nextA = a.substring(1);
            final boolean result;
            if (Character.isUpperCase(aChar)) {
                if (aChar == b.charAt(0)) {
                    result = areMatching(nextA, nextB);
                } else {
                    result = false;
                }
            } else {
                if (areMatching(nextA, b)) {
                    result = true;
                } else {
                    if (Character.toUpperCase(aChar) == b.charAt(0)) {
                        result = areMatching(nextA, nextB);
                    } else {
                        result = false;
                    }
                }
            }
            aCache.put(b, result);
        }

        return aCache.get(b);
    }

    // Complete the abbreviation function below.
    static String abbreviation(String a, String b) {
        return areMatching(a, b) ? "YES" : "NO";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String a = scanner.nextLine();

            String b = scanner.nextLine();

            String result = abbreviation(a, b);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
