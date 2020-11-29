package graphs.roads_and_libraries;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;
import java.util.Set;

/**
 * Challenge: https://www.hackerrank.com/challenges/torque-and-development
 *
 * TODO: Not working yet...
 */
public class Solution {

    // Complete the roadsAndLibraries function below.
    static long roadsAndLibraries(int n, int c_lib, int c_road, int[][] cities) {
        // In case of a library costing less than a road, we won't even try
        // to connect the cities and build a library in every city.
        if (c_lib <= c_road) {
            return c_lib * n;
        }

        // Otherwise, we have to build 1 library per group of connected cities,
        // then connect all cities to the central one.
        List<Set<Integer>> links = new ArrayList<>();
        boolean linked;
        for (int[] cityLink : cities) {
            int firstCity = cityLink[0];
            int secondCity = cityLink[1];
            linked = false;
            for (Set<Integer> cityGroup : links) {
                if (cityGroup.contains(firstCity) || cityGroup.contains(secondCity)) {
                    cityGroup.add(firstCity);
                    cityGroup.add(secondCity);
                    linked = true;
                }
            }
            if (!linked) {
                Set<Integer> newLink = new HashSet<>();
                newLink.add(firstCity);
                newLink.add(secondCity);
                links.add(newLink);
            }
        }

        Set<Integer> intersection;
        Set<Integer> cityGroup = links.get(0);
        Set<Integer> otherGroup;
        for (int i = 1; i < links.size(); i++) {
            otherGroup = links.get(i);
            intersection = new HashSet<>(cityGroup);
            intersection.retainAll(otherGroup);
            if (!intersection.isEmpty()) {
                cityGroup.addAll(otherGroup);
                links.remove(otherGroup);
            }
        }

        Integer total_cities = links.stream().map(Set::size).reduce(Integer::sum).orElseGet(() -> 0);
        return links.size() * c_lib + (total_cities - 1) * c_road + c_lib * (n - total_cities);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String[] nmC_libC_road = scanner.nextLine().split(" ");

            int n = Integer.parseInt(nmC_libC_road[0]);

            int m = Integer.parseInt(nmC_libC_road[1]);

            int c_lib = Integer.parseInt(nmC_libC_road[2]);

            int c_road = Integer.parseInt(nmC_libC_road[3]);

            int[][] cities = new int[m][2];

            for (int i = 0; i < m; i++) {
                String[] citiesRowItems = scanner.nextLine().split(" ");
                scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

                for (int j = 0; j < 2; j++) {
                    int citiesItem = Integer.parseInt(citiesRowItems[j]);
                    cities[i][j] = citiesItem;
                }
            }

            long result = roadsAndLibraries(n, c_lib, c_road, cities);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
