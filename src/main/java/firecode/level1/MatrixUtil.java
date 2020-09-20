package firecode.level1;

public class MatrixUtil {

    // Flip it!
    public static void flipItVerticalAxis(int[][] matrix) {
        for(int row_idx=0; row_idx<matrix.length; row_idx++) {
            int row_len = matrix[row_idx].length;
            for(int col_idx=0; col_idx < row_len/2; col_idx++)
                swap(matrix[row_idx], col_idx, row_len - col_idx - 1);
        }
    }

    public static void printMatrix(int[][] matrix) {
        for(int row_idx=0; row_idx<matrix.length; row_idx++) {
            StringBuilder builder = new StringBuilder();
            for(int col_idx=0; col_idx<matrix[row_idx].length; col_idx++) {
                builder.append(matrix[row_idx][col_idx]);
                builder.append(' ');
            }
            System.out.println(builder.toString());
        }
    }

    public static void swap(int[] arr, int idx_1, int idx_2) {
        int temp = arr[idx_1];
        arr[idx_1] = arr[idx_2];
        arr[idx_2] = temp;
    }
}