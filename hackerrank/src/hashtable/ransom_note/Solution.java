package hashtable.ransom_note;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-ransom-note/problem
 */
public class Solution {

    // Complete the checkMagazine function below.
    static boolean okMagazine(String[] magazine, String[] note) {
        Map<String, Integer> availableWords = new HashMap<>();
        for (String s : magazine) {
            Integer available = availableWords.get(s) == null ? 0 : availableWords.get(s);
            availableWords.put(s, available + 1);
        }
        for (String s : note) {
            if (availableWords.containsKey(s) && availableWords.get(s) > 0) {
                availableWords.put(s, availableWords.get(s) - 1);
            } else {
                return false;
            }
        }
        return true;
    }

    static void checkMagazine(String[] magazine, String[] note) {
        System.out.println(okMagazine(magazine, note) ? "Yes" : "No");
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] mn = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mn[0]);

        int n = Integer.parseInt(mn[1]);

        String[] magazine = new String[m];

        String[] magazineItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            String magazineItem = magazineItems[i];
            magazine[i] = magazineItem;
        }

        String[] note = new String[n];

        String[] noteItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String noteItem = noteItems[i];
            note[i] = noteItem;
        }

        checkMagazine(magazine, note);

        scanner.close();
    }
}
