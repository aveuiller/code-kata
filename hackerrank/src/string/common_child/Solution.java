package string.common_child;


import java.io.*;
import java.util.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/common-child
 * Cf. https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
 *
 * TODO: Still timeout on submission
 */
public class Solution {
    private static final Map<String, Map<String, Integer>> CACHE = new HashMap<>();

    // Complete the commonChild function below.
    static int commonChild(String s1, String s2) {
        // End condition solves problem for
        // len(s1) in [0, 1] or len(s2) in [0, 1]
        if (s1.isEmpty() || s2.isEmpty()) {
            return 0;
        }
        if (s1.length() == 1) {
            return s2.contains(String.valueOf(s1.charAt(0))) ? 1 : 0;
        }
        if (s2.length() == 1) {
            return s1.contains(String.valueOf(s2.charAt(0))) ? 1 : 0;
        }

        Map<String, Integer> s1Cache = fetchS1Cache(s1);
        // Compute solution if not cached.
        if (!s1Cache.containsKey(s2)) {
//            System.out.println("Comparing " + s1 + " - " + s2);
            String s1Cut = s1.substring(1);
            String s2Cut = s2.substring(1);
            int result;
            if (s1.startsWith(String.valueOf(s2.charAt(0)))) {
                result = 1 + commonChild(s1Cut, s2Cut);
            } else {
                int cutLeft = commonChild(s1Cut, s2);
                int cutRight = commonChild(s1, s2Cut);
                result = Math.max(cutLeft, cutRight);
            }
            s1Cache.put(s2, result);
        }
        return s1Cache.get(s2);
    }

    private static Map<String, Integer> fetchS1Cache(String s1) {
        return CACHE.computeIfAbsent(s1, k -> new HashMap<>());
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
//        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

//        String s1 = scanner.nextLine();

//        String s2 = scanner.nextLine();
        String s1 = "HARRY";
        String s2 = "SALLY";
        int result = commonChild(s1, s2);
        System.out.println(result);
//        bufferedWriter.write(String.valueOf(result));
//        bufferedWriter.newLine();

//        bufferedWriter.close();

//        scanner.close();
    }
}