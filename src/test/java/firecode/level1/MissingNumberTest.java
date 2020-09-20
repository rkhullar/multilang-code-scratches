package firecode.level1;

import org.junit.jupiter.api.Test;
import static firecode.level1.MissingNumber.*;
import static org.junit.jupiter.api.Assertions.*;

class MissingNumberTest {

    @Test
    void testFindMissingNumber() {
        int[] arr = {1, 2, 4, 5, 6, 7, 8, 9, 10};
        int y = findMissingNumber(arr);
        assertEquals(3, y);
    }
}