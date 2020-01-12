package level1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static level1.Solution.*;
import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    @ParameterizedTest(name = "fib({0}) = {1}")
    @CsvSource({"0, 0", "1, 1", "2, 1", "3, 2", "4, 3", "5, 5", "6, 8", "7, 13", "8, 21", "9, 34", "10, 55"})
    void testRecursiveFibonacci(int x, long e) {
        long y = recursiveFibonacci(x);
        assertEquals(e, y);
    }

    @Test
    void testFindMissingNumber() {
        int[] arr = {1, 2, 4, 5, 6, 7, 8, 9, 10};
        int y = findMissingNumber(arr);
        assertEquals(3, y);
    }


    @ParameterizedTest
    @MethodSource("provideArgsForTestDeleteAtHead")
    @SuppressWarnings("unchecked")
    <T> void testDeleteAtHead(T[] arr_x, T[] arr_e) {
        ListNode<T> list_x =  arr_x.length > 0 ? ListNode.from(arr_x) : null;
        ListNode<T> list_y = deleteAtHead(list_x);

        if (arr_e.length > 0) {
            assertNotNull(list_y);
            int size_y = list_y.size();
            T[] arr_y = list_y.toArray();
            assertArrayEquals(arr_e, arr_y);
        } else {
            assertNull(list_y);
        }

    }

    private static Stream<Arguments> provideArgsForTestDeleteAtHead() {
        return Stream.of(
                Arguments.of(new Integer[]{}, new Integer[]{}),
                Arguments.of(new Integer[]{1}, new Integer[]{}),
                Arguments.of(new Integer[]{1, 2}, new Integer[]{2}),
                Arguments.of(new Integer[]{1, 2, 3, 4}, new Integer[]{2, 3, 4})
        );
    }

    @ParameterizedTest
    @MethodSource("provideArgsForTestInsertAtTail")
    @SuppressWarnings("unchecked")
    <T> void testInsertAtTail(T[] arr_x, int data, T[] arr_e) {
        ListNode<T> list_x =  arr_x.length > 0 ? ListNode.from(arr_x) : null;
        ListNode<T> list_y = insertAtTail(list_x, data);
        T[] arr_y = list_y.toArray();
        assertArrayEquals(arr_e, arr_y);
    }

    private static Stream<Arguments> provideArgsForTestInsertAtTail() {
        return Stream.of(
                Arguments.of(new Integer[]{}, 1, new Integer[]{1}),
                Arguments.of(new Integer[]{1}, 2, new Integer[]{1, 2}),
                Arguments.of(new Integer[]{1, 2}, 3, new Integer[]{1, 2, 3})
        );
    }

    @ParameterizedTest
    @MethodSource("provideArgsForTestFindMiddleNode")
    <T> void testFindMiddleNode(T[] arr_x, T e) {
        ListNode<T> list_x = arr_x.length > 0 ? ListNode.from(arr_x) : null;
        ListNode<T> y = findMiddleNode(list_x);
        if (e != null)
            assertEquals(e, y.data);
        else
            assertNull(y);
    }

    private static Stream<Arguments> provideArgsForTestFindMiddleNode() {
        return Stream.of(
                Arguments.of(new Integer[]{1}, 1),
                Arguments.of(new Integer[]{1, 2}, 1),
                Arguments.of(new Integer[]{1, 2, 3, 4, 5}, 3),
                Arguments.of(new Integer[]{}, null)
        );
    }
}
