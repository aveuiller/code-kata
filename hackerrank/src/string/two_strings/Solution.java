package string.two_strings;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/two-strings
 */
public class Solution {

    static String twoStrings(String s1, String s2) {
        return commonSubstring(s1, s2) ? "YES" : "NO";
    }

    private static boolean commonSubstring(String s1, String s2) {
        Map<Character, Boolean> letters = new HashMap<>();
        for (char c : s1.toCharArray()) {
            letters.put(c, true);
        }
        for (char c : s2.toCharArray()) {
            if (letters.containsKey(c)) {
                return true;
            }
        }
        return false;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s1 = scanner.nextLine();

            String s2 = scanner.nextLine();

            String result = twoStrings(s1, s2);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
