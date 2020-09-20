package firecode.level1;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import java.util.stream.Stream;

import static firecode.level1.MatrixUtil.*;
import static org.junit.jupiter.api.Assertions.*;

class MatrixUtilTest {

    @ParameterizedTest
    @MethodSource("provideArgsForTestFlipItVerticalAxis")
    void testFlipItVerticalAxis(int[][] matrix, int[][] expected) {
        flipItVerticalAxis(matrix);
        assertArrayEquals(expected, matrix);
    }

    private static Stream<Arguments> provideArgsForTestFlipItVerticalAxis() {
        return Stream.of(
                Arguments.of(new int[][]{{1,0,0},{0,0,1}}, new int[][]{{0,0,1},{1,0,0}}),
                Arguments.of(new int[][]{{1,0,1},{1,0,1}}, new int[][]{{1,0,1},{1,0,1}}),
                Arguments.of(new int[][]{{1,2,3},{4,5,6},{7,8,9}}, new int[][]{{3,2,1},{6,5,4},{9,8,7}}),
                Arguments.of(new int[][]{{1,0}}, new int[][]{{0,1}}),
                Arguments.of(new int[][]{{1}}, new int[][]{{1}})
        );
    }
}