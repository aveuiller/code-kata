package interviews.visa;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {
    /*
     * Complete the 'printAntiDiag' function below.
     *
     * The function accepts 2D_INTEGER_ARRAY matrix as parameter.
     */

    public static void printAntiDiag(List<List<Integer>> matrix) {
        int j;
        // The solution complexity will be O(n^2)
        // since we have to go through all elements of the matrix.
        for (int x = 0; x < matrix.size(); x++) {
            j = matrix.size() - x - 1;
            for (int i = 0; i <= x; i++) {
                System.out.println(matrix.get(i).get(j + i));
            }
        }

        for (int x = 0; x < matrix.size(); x++) {
            for (int i = 1; i < matrix.size() - x; i++) {
                System.out.println(matrix.get(x + i).get(i - 1));
            }
        }
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
//        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

//        int matrixRows = Integer.parseInt(bufferedReader.readLine().trim());
//        int matrixColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> matrix = new ArrayList<>();

//        IntStream.range(0, matrixRows).forEach(i -> {
//            try {
//                matrix.add(
//                        Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
//                                .map(Integer::parseInt)
//                                .collect(toList())
//                );
//            } catch (IOException ex) {
//                throw new RuntimeException(ex);
//            }
//        });

        matrix.add(Arrays.asList(1, 2 ,3));
        matrix.add(Arrays.asList(4, 5, 6));
        matrix.add(Arrays.asList(7, 8, 9));
        //
//        matrix.add(Arrays.asList(1, 2, 3, 4));
//        matrix.add(Arrays.asList(5, 6, 7, 8));
//        matrix.add(Arrays.asList(9, 10, 11, 12));
//        matrix.add(Arrays.asList(13, 14, 15, 16));

        Result.printAntiDiag(matrix);

//        bufferedReader.close();
    }
}
