package firecode.level1;

public class MissingNumber {

    // Find the Missing Number in a Set of Numbers from 1 to 10
    public static int sum_1toN(int n) {
        return (n + 1) * n / 2;
    }

    public static int findMissingNumber(int[] arr) {
        final int sum_10 = sum_1toN(10);
        int sum_arr = 0;
        for (int x: arr)
            sum_arr += x;
        return sum_10 - sum_arr;
    }

}