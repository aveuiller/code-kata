package sorting.fraudulent_activity_notifications;

import java.io.*;
import java.util.*;

/**
 * Challenge: https://www.hackerrank.com/challenges/fraudulent-activity-notifications
 */
public class Solution {

    private static Map<Integer, Integer> AMOUNT_ENTRIES;

    // Complete the activityNotifications function below.
    static int activityNotifications(int[] expenditure, int d) {
        int notifications_count = 0;
        for (int day = d; day < expenditure.length; day++) {
            double median = getMedian(expenditure, d, day);
            if (expenditure[day] >= 2 * median) {
                notifications_count++;
            }
        }
        return notifications_count;
    }

    private static double getMedian(int[] expenditure, int d, int day) {
        if (AMOUNT_ENTRIES == null) {
            init_count(expenditure, d, day);
        } else {
            update_count(expenditure, d, day);
        }

        double median = 0;
        long threshold = (int) Math.ceil((double) d / 2);
        long count = 0;
        for (final Map.Entry<Integer, Integer> entry : AMOUNT_ENTRIES.entrySet()) {
            count += entry.getValue();

            if (d % 2 == 0) {
                // First entry to add to the median
                if (count >= threshold && median == 0) {
                    median = entry.getKey();
                }
                // Second entry to add to the median + compute mean
                if (count > threshold) {
                    median += entry.getKey();
                    median = median / 2;
                    break;
                }
            } else {
                if (count >= threshold) {
                    median = entry.getKey();
                    break;
                }
            }
        }
        return median;
    }

    private static void init_count(int[] expenditure, int d, int day) {
        AMOUNT_ENTRIES = new TreeMap<>();
        for (int i = day - d; i < day; i++) {
            AMOUNT_ENTRIES.put(expenditure[i], AMOUNT_ENTRIES.getOrDefault(expenditure[i], 0) + 1);
        }
    }

    private static void update_count(int[] expenditure, int d, int day) {
        int removed_value = expenditure[day - d - 1];
        AMOUNT_ENTRIES.put(removed_value, AMOUNT_ENTRIES.get(removed_value) - 1);

        int added_value = expenditure[day - 1];
        AMOUNT_ENTRIES.put(added_value, AMOUNT_ENTRIES.getOrDefault(added_value, 0) + 1);

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nd = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nd[0]);

        int d = Integer.parseInt(nd[1]);

        int[] expenditure = new int[n];

        String[] expenditureItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int expenditureItem = Integer.parseInt(expenditureItems[i]);
            expenditure[i] = expenditureItem;
        }

        int result = activityNotifications(expenditure, d);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
