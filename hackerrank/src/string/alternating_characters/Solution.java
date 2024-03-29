package string.alternating_characters;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Challenge: https://www.hackerrank.com/challenges/alternating-characters
 */
public class Solution {

    // Complete the alternatingCharacters function below.
    static int alternatingCharacters(String s) {
        List<Character> remaining = IntStream
                .rangeClosed(1, s.length() - 1)
                .filter((i) -> s.charAt(i - 1) == s.charAt(i))
                .mapToObj(s::charAt)
                .collect(Collectors.toList());
        return remaining.size();
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            int result = alternatingCharacters(s);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
