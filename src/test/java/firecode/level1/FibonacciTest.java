package firecode.level1;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static firecode.level1.Fibonacci.*;
import static org.junit.jupiter.api.Assertions.*;

class FibonacciTest {

    @ParameterizedTest(name = "fib({0}) = {1}")
    @CsvSource({"0, 0", "1, 1", "2, 1", "3, 2", "4, 3", "5, 5", "6, 8", "7, 13", "8, 21", "9, 34", "10, 55"})
    void testRecursiveFibonacci(int x, long e) {
        long y = recursiveFibonacci(x);
        assertEquals(e, y);
    }

}