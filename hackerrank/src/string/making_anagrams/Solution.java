package string.making_anagrams;


import java.io.*;
import java.util.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/ctci-making-anagrams
 */
public class Solution {

    // Complete the makeAnagram function below.
    static int makeAnagram(String a, String b) {
        Map<Character, Integer> letterMap = new HashMap<>();
        for (char c : a.toCharArray()) {
            int count = letterMap.get(c) != null ? letterMap.get(c) : 0;
            letterMap.put(c, count + 1);
        }
        for (char c : b.toCharArray()) {
            int count = letterMap.get(c) != null ? letterMap.get(c) : 0;
            letterMap.put(c, count - 1);
        }
        Optional<Integer> reduce = letterMap.values()
                .stream()
                .reduce((x, y) -> Math.abs(x) + Math.abs(y));
        return reduce.orElse(0);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String a = scanner.nextLine();

        String b = scanner.nextLine();

        int res = makeAnagram(a, b);

        bufferedWriter.write(String.valueOf(res));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
