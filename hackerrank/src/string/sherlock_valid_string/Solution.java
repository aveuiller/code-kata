package string.sherlock_valid_string;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.stream.Collectors;

/**
 * Challenge: https://www.hackerrank.com/challenges/sherlock-and-valid-string
 */
public class Solution {

    // Complete the isValid function below.
    static String isValid(String s) {
        String result = "NO";
        Map<Character, Integer> charCount = new HashMap<>();
        int count;
        for (char c : s.toCharArray()) {
            count = charCount.getOrDefault(c, 0);
            charCount.put(c, count + 1);
        }

        Map<Integer, Integer> frequencyCount = new HashMap<>();
        for (Integer value : charCount.values()) {
            count = frequencyCount.getOrDefault(value, 0);
            frequencyCount.put(value, count + 1);
        }

        Set<Integer> frequencies = frequencyCount.keySet();
        if (frequencies.size() <= 1) {
            result = "YES";
        } else if (frequencies.size() == 2) {
            List<Integer> soloFrequencies = frequencyCount.entrySet().stream()
                    .filter(x -> x.getValue() == 1)
                    .map(Map.Entry::getKey)
                    .collect(Collectors.toList());

            if (soloFrequencies.size() == 1) {
                ArrayList<Integer> frequArray = new ArrayList<>(frequencies);
                int diffFrequency = Math.abs(frequArray.get(0) - frequArray.get(1));
                if (soloFrequencies.get(0).equals(1) || diffFrequency == 1) {
                    result = "YES";
                }
            } else if (soloFrequencies.size() > 1) {
                result = "YES";
            }
        }
        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        String result = isValid(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
