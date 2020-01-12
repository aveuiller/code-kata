package stacks.balanced_brackets;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/balanced-brackets/
 */
public class Solution {

    static private HashMap<Character, Character> charMap = new HashMap<>();

    static {
        charMap.put('(', ')');
        charMap.put('{', '}');
        charMap.put('[', ']');
    }

    // Complete the isBalanced function below.
    static String isBalanced(String s) {
        return balanceOk(s) ? "YES" : "NO";
    }

    private static boolean balanceOk(String s) {
        Stack<Character> charStack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (charMap.containsKey(c)) {
                charStack.push(c);
            } else {
                if (charStack.isEmpty() || charMap.get(charStack.pop()) != c) {
                    return false;
                }
            }
        }
        return charStack.isEmpty();
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String s = scanner.nextLine();

            String result = isBalanced(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
